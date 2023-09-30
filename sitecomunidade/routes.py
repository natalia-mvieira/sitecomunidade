from flask import render_template, url_for, redirect, request, flash, abort
from sitecomunidade import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from sitecomunidade.forms import FormLogin, FormCriarConta, FormEditarPerfil, FormCriarPost, FormAlterarSenha
from sitecomunidade.models import Usuario, Post
import secrets
import os
from PIL import Image
from werkzeug.utils import secure_filename

@app.route('/')
def homepage():
    posts = Post.query.order_by(Post.id.desc())
    return render_template('homepage.html', posts=posts)

@app.route('/contato')
def contato():
    telefone = '(11) 99999-1234'
    email_comunidade = 'comunidade_nmv@teste.br'
    return render_template('contato.html', telefone=telefone, email_comunidade=email_comunidade)

@app.route('/usuarios')
@login_required
def usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/entrar', methods=['GET','POST'])
def entrar():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash(f'Login realizado com sucesso para {form_login.email.data}', 'alert-success')
            par_next = request.args.get('next')
            if par_next:
                return redirect(par_next)
            else:
                return redirect(url_for('homepage'))
        else:
            flash(f'E-mail ou senha incorretos.', 'alert-danger')
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_cript = bcrypt.generate_password_hash((form_criarconta.senha.data))
        usuario = Usuario(email=form_criarconta.email.data, username=form_criarconta.username.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        flash(f'Conta criada com sucesso para {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('entrar'))

    return render_template('entrar.html', form_login=form_login, form_criarconta = form_criarconta)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))

@app.route('/perfil/')
@login_required
def perfil():
    foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    cursos = current_user.cursos.split(';')
    posts_usuario = Post.query.filter(Post.id_usuario == current_user.id).order_by(Post.id.desc()).all()
    return render_template('perfil.html', foto_perfil=foto_perfil, cursos=cursos, posts=posts_usuario)

@app.route('/post/', methods=['GET', 'POST'])
@login_required
def criar_post():
    form_criar_post = FormCriarPost()
    if form_criar_post.validate_on_submit():
        post = Post(titulo=form_criar_post.titulo.data, corpo=form_criar_post.corpo.data, id_usuario=current_user.id)
        database.session.add(post)
        database.session.commit()
        flash('Post criado com sucesso!', 'alert-success')
        return redirect(url_for('homepage'))
    return render_template('criar_post.html', form_criar_post=form_criar_post)

@app.route('/post/<id>')
def exibir_post(id):
    post = Post.query.get(id)
    return render_template('exibir_post.html', post=post)

@app.route('/editarpost/<id>', methods=['GET', 'POST'])
@login_required
def editar_post(id):
    post = Post.query.get(id)
    form_criar_post = FormCriarPost()
    if post.autor.id == current_user.id:
        if form_criar_post.validate_on_submit():
            post.titulo = form_criar_post.titulo.data
            post.corpo = form_criar_post.corpo.data
            database.session.commit()
            flash('Post editado com sucesso!', 'alert-success')
            return redirect(url_for('homepage'))
        elif request.method == 'GET':
            form_criar_post.titulo.data = post.titulo
            form_criar_post.corpo.data = post.corpo
        return render_template('editar_post.html', form_criar_post=form_criar_post, post=post)

@app.route('/deletar/<id>', methods=['GET', 'POST'])
@login_required
def deletar_post(id):
    post = Post.query.get(id)
    if post:
        if post.autor.id == current_user.id:
            database.session.delete(post)
            database.session.commit()
            flash('Post excluído com sucesso!', 'alert-success')
            return redirect(url_for('homepage'))
        else:
            abort(403)
    else:
        abort(403)

def salvar_imagem(imagem):
    #altero o nome da imagem
    codigo = secrets.token_hex(8)
    nome, extensao = os.path.splitext(imagem.filename)
    nome_completo = nome + codigo + extensao
    nome_seguro = secure_filename(nome_completo)
    caminho_completo = os.path.join(app.root_path, 'static/fotos_perfil/', nome_seguro)

    #compacto a imagem e salvo
    tamanho = (400,400) #pixels de largura e comprimento
    imagem_reduzida = Image.open(imagem)
    imagem_reduzida.thumbnail(tamanho)
    imagem_reduzida.save(caminho_completo)
    return nome_seguro

def atualizar_cursos(form_editar_perfil):
    cursos = ''
    for campo in form_editar_perfil:
        if 'curso_' in campo.name and campo.data:
            cursos = cursos + ';' + campo.label.text
    return cursos

@app.route('/perfil/alterarsenha', methods=['GET', 'POST'])
@login_required
def alterar_senha():
    form_editar_senha = FormAlterarSenha()
    if form_editar_senha.validate_on_submit():
        if bcrypt.check_password_hash(current_user.senha, form_editar_senha.senha_atual.data):
            current_user.senha = bcrypt.generate_password_hash(form_editar_senha.senha_nova.data)
            database.session.commit()
            flash(f'Senha alterada com sucesso!', 'alert-success')
            return redirect(url_for('editar_perfil'))
        else:
            flash(f'Senha atual incorreta.', 'alert-danger')
    return render_template('alterar_senha.html', form_editar_senha=form_editar_senha)

@app.route('/perfil/editar', methods=['GET', 'POST'])
@login_required
def editar_perfil():
    form_editar_perfil = FormEditarPerfil()
    if form_editar_perfil.validate_on_submit():
        current_user.email = form_editar_perfil.email.data
        current_user.username = form_editar_perfil.username.data
        if form_editar_perfil.foto_perfil.data:
            nova_imagem = salvar_imagem(form_editar_perfil.foto_perfil.data)
            imagem_atual = current_user.foto_perfil
            if imagem_atual=='default.jpg':
                current_user.foto_perfil = nova_imagem
            if imagem_atual!= 'default.jpg':
                current_user.foto_perfil = nova_imagem
                os.remove(os.path.join(app.root_path,'static/fotos_perfil/', imagem_atual))
        current_user.cursos = atualizar_cursos(form_editar_perfil)
        database.session.commit()
        flash(f'Alterações salvas com sucesso.', 'alert-success')
        return redirect(url_for('perfil'))
    elif request.method == 'GET':
        form_editar_perfil.email.data = current_user.email
        form_editar_perfil.username.data = current_user.username
        for campo in form_editar_perfil:
            if campo.label.text in current_user.cursos:
                campo.data = True
    lista_cursos = current_user.cursos.split(';')
    foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    return render_template('editar_perfil.html', foto_perfil=foto_perfil, form_editar_perfil=form_editar_perfil, cursos=lista_cursos)

@app.route('/perfil/<id>')
@login_required
def outro_perfil(id):
    if id == current_user.id:
        return redirect(url_for('perfil'))
    else:
        usuario = Usuario.query.get(int(id))
        foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(usuario.foto_perfil))
        posts_usuario = Post.query.filter(Post.id_usuario == usuario.id).order_by(Post.id.desc()).all()
    return render_template('outro_perfil.html', usuario=usuario, foto_perfil=foto_perfil, posts=posts_usuario)
