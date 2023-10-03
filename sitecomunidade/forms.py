from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from sitecomunidade.models import Usuario
from flask_login import current_user

class FormLogin(FlaskForm):
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha:', validators=[DataRequired(), Length(6,20)])
    lembrar_dados = BooleanField('Lembrar dados de acesso')
    botao_submit_login = SubmitField('Fazer Login')

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError('Usuário inexistente, crie uma conta.')

    def validate_password(self, senha):
        senha = Usuario.query.filter_by(senha=senha.data).first()
        if not senha:
            raise ValidationError('Senha incorreta.')

class FormCriarConta(FlaskForm):
    email = StringField("E-mail:", validators=[DataRequired(), Email()])
    username = StringField("Nome de Usuário:", validators=[DataRequired()])
    senha = PasswordField("Senha:", validators=[DataRequired(), Length(6,20)])
    confirmacao_senha = PasswordField("Confirmação de Senha:", validators=[DataRequired(), EqualTo("senha")])
    botao_submit_criarconta = SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("E-mail já cadastrado, faça login para continuar.")

class FormEditarPerfil(FlaskForm):
    email = StringField("E-mail:", validators=[DataRequired(), Email()])
    username = StringField("Nome de Usuário:", validators=[DataRequired()])
    foto_perfil = FileField("Editar foto de perfil:", validators=[FileAllowed(['jpg', 'png'])])
    curso_python = BooleanField('Python')
    curso_sql = BooleanField('SQL')
    curso_powerbi = BooleanField('PowerBI')
    curso_html = BooleanField('HTML')
    curso_css = BooleanField('CSS')
    curso_javascrypt = BooleanField('JavaScrypt')
    curso_csharp = BooleanField('C#')
    curso_vba = BooleanField('VBA')
    botao_submit_editarperfil = SubmitField("Salvar")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario and usuario.id != current_user.id:
            raise ValidationError("E-mail já cadastrado.")

class FormAlterarSenha(FlaskForm):
    senha_nova = PasswordField('Nova senha:', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmar nova senha:', validators=[DataRequired(), EqualTo("senha_nova")])
    senha_atual = PasswordField('Senha atual:', validators=[DataRequired(), Length(6, 20)])
    botao_submit_alterarsenha = SubmitField('Salvar')

class FormCriarPost(FlaskForm):
    titulo = StringField('Título:', validators=[DataRequired(), Length(2,140)])
    corpo = TextAreaField('Escreva seu post aqui:', validators=[DataRequired()])
    botao_submit_criarpost = SubmitField('Salvar Post')