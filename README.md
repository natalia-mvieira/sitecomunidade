# *Comunidade NMV*

A Comunidade NMV é um site em que diferentes usuários da plataforma da Escola NMV - Treinamentos (fictícia) podem postar dúvidas e comentários sobre os cursos em que estão matriculados.

O site foi criado utilizando-se o *framework* Flask.

Para gerenciamento dos usuários e das postagens, foi criado um banco de dados por meio da biblioteca SQLAlchemy. Uma das tabelas armazena as informações das contas criadas (Usuario) e a outra (Post) armazena as informações dos posts criados.

Na criação da conta, para garantir a segurança da senha do usuário, ela é criptografada por meio da classe Bcrypt da biblioteca Flask-Bcrypt.

Para processos que envolvem o usuário estar logado (@login_required), sendo sua identificação feita por seu ID, foi utilizada a biblioteca Flask-Login, conectada à aplicação por meio da classe LoginManager. 

Para a criação de formulários no site, foi empregada a biblioteca WTForms, junto com as devidas validações (wtforms.validators) para cada campo.

Agora, uma breve apresentação de cada uma das páginas do site e suas funcionalidades:

### Homepage

Na página inicial (*homepage*) é possível ter acesso aos posts já criados pelos usuários, com título, corpo, nome do usuário, sua foto e data da criação da postagem.

Também é possível notar os links para as páginas 'Usuários', 'Contato' e 'Entrar'.

<div align="center">
    <img src="https://github.com/natalia-mvieira/sitecomunidade/assets/144560412/b9eb25f0-e2bf-417d-8233-9a728866aaa9" width="700px"/>
</div>

A página Usuários tem acesso permitido apenas com login. Ao tentar acessá-la antes de entrar no site, a página faz o direcionamento para a página 'Entrar', onde é possível realizar login ou criar conta.

### Contato

A página Contato contém informações simples de telefone e e-mail da comunidade e seu acesso é livre.

<div align="center">
    <img src="https://github.com/natalia-mvieira/sitecomunidade/assets/144560412/14aed3b2-cbec-435d-88d1-6b002ec6a35d" width="700px"/>
</div>

### Entrar

Ao tentar acesso na página Usuários ou ao clicar no botão 'Entrar' no canto superior direito da Homepage, temos o direcionamento para a página de Login ou Criar Conta.

<div align="center">
    <img src="https://github.com/natalia-mvieira/sitecomunidade/assets/144560412/234045bf-222a-48a8-9a40-2247d2e4cd15" width="700px"/>
</div>

Ao criar conta, as validações dos campos do formulário vão verificar se o e-mail já existe, já que ele deve ser único, se o nome de usuário está preenchido e se os campos de senha também. A senha deve ter de 6 a 20 caracteres e o campo de confirmação de senha verifica se o dado inserido é o mesmo do campo 'senha'. As informações incompatíveis com as validações serão informadas na tela.

Após criar conta, o usuário pode realizar o login, com todo o sistema de verificação de e-mail e senha. Automaticamente, o usuário será direcionado à página da homepage. Porém, agora, ele poderá criar, editar e deletar posts, além de poder ver o perfil de outros usuários.

<div align="center">
    <img src="https://github.com/natalia-mvieira/sitecomunidade/assets/144560412/597b851a-dcfe-4186-b672-ea588bd7c080" width="700px"/>
</div>

### Usuários

Essa página mostra todos os usuários existentes na plataforma, com informações do total de cursos matriculados, número de posts e os cursos da matrícula.

<div align="center">
    <img src="https://github.com/natalia-mvieira/sitecomunidade/assets/144560412/c37aca9b-00d8-4600-a945-b38dd2558faf" width="700px"/>
</div>

### Perfil

No botão 'Meu Perfil' na homepage, o usuário consegue visualizar o próprio perfil. Ele pode ver todos os posts que ele criou no botão 'Meus Posts', o qual direciona a página para a parte inferior, onde os posts aparecem dos mais recentes para os mais antigos. 

<div align="center">
    <img src="https://github.com/natalia-mvieira/sitecomunidade/assets/144560412/faa7a9b4-805c-4f3e-a0f9-3c2a12a0999f" width="700px"/>
</div>

Além disso, ele pode fazer a edição do perfil no botão 'Editar Perfil'.

### Editar perfil

Aqui, o usuário pode alterar informações de e-mail, usuário, senha, foto de perfil e cursos matriculados. O banco de dados recebe as atualizações.

<div align="center">
    <img src="https://github.com/natalia-mvieira/sitecomunidade/assets/144560412/277fd994-1233-4dcb-8b80-6dc0b581c135" width="700px"/>
</div>

<div align="center">
    <img src="https://github.com/natalia-mvieira/sitecomunidade/assets/144560412/07a09d0e-36a9-441d-8437-cae756f6399f" width="700px"/>
</div>

Quando um usuário cria uma conta, sua foto de perfil é padrão do site (*default*). Para alterar a foto de perfil, ele pode escolher um arquivo do computador. Esse arquivo terá seu nome alterado, sendo adicionada uma chave aleatória ao final dele, utilizando-se a biblioteca *secrets*. Isso evita a sobreposição de arquivos no banco de dados no caso de usuários diferentes colocarem fotos com mesmo nome.

Exemplo de usuário com imagem de perfil padrão, ou seja, não escolheu uma foto de perfil:

<div align="center">
    <img src="https://github.com/natalia-mvieira/sitecomunidade/assets/144560412/08754a47-5892-4c5a-8083-02bc222e17e7" width="700px"/>
</div>

### Alterar senha

Caso o usuário opte por fazer alteração de sua senha, ele será direcionado à página que contém um formulário de alteração. Ele deve inserir a nova senha escolhida, fazer sua confirmação e adicionar, por segurança, a senha atual. Esta será verificada no banco de dados por meio do Bcrypt. Se for compatível com o usuário, e se os demais campos seguirem os critérios de validação, a alteração é feita.

<div align="center">
    <img src="https://github.com/natalia-mvieira/sitecomunidade/assets/144560412/6613fc13-d01f-405c-89a8-b5c7b114c2b0" width="700px"/>
</div>

### Criar Post

Aqui, o usuário pode criar e postar um novo tópico. Ele adiciona um título e um corpo. 
Ao salvar, seu post aparecerá em seu perfil e na homepage, onde outros usuários poderão fazer a leitura.

<div align="center">
    <img src="https://github.com/natalia-mvieira/sitecomunidade/assets/144560412/ef514487-9bc3-4b16-8e40-923de2b91e80" width="700px"/>
</div>

### Editar ou Deletar Post

Ao clicar no título do próprio post, seja na homepage, seja no próprio perfil, o usuário pode realizar a sua edição ou deletá-lo. 

<div align="center">
    <img src="https://github.com/natalia-mvieira/sitecomunidade/assets/144560412/fb213e7e-eada-4993-8dc4-85f6334d3259" width="700px"/>
</div>

Ao optar por deletar o post, uma mensagem de confirmação aparecerá na tela para que o processo seja completado.

<div align="center">
    <img src="https://github.com/natalia-mvieira/sitecomunidade/assets/144560412/12edec7f-dce3-4011-824b-dbae46f8e0f5" width="700px"/>
</div>

### Outro Perfil

É possível ter acesso ao perfil de outro usuário. Basta clicar sobre a foto de perfil ao lado dos posts na homepage ou na página 'Usuários'. Assim, é possível ver todos os posts daquele usuário, além das informações gerais.

<div align="center">
    <img src="https://github.com/natalia-mvieira/sitecomunidade/assets/144560412/cbe15ad4-0716-4fb4-a59c-f263eff49e41" width="700px"/>
</div>

### Post

Ao clicar sobre o título de um post de outro usuário, é possível visualizar o post individualmente, em outra página.
É feita uma verificação se o criador do post é ou não o usuário atual. Se for, ele terá as opções de editar e deletar mencionadas acima.

<div align="center">
    <img src="https://github.com/natalia-mvieira/sitecomunidade/assets/144560412/72314da2-1944-4c54-af24-17fee6748f00" width="700px"/>
</div>

