# *Comunidade NMV*

A Comunidade NMV é um site em que diferentes usuários da plataforma da Escola NMV - Treinamentos (fictícia) podem postar dúvidas e comentários sobre os cursos em que estão matriculados.

O site foi criado utilizando-se o *framework* Flask.

Para gerenciamento dos usuários e das postagens, foi criado um banco de dados por meio da biblioteca SQLAlchemy. Uma das tabelas armaze as informações das contas criadas (Usuario) e a outra (Post) armazena as informações dos posts criados.

Na criação da conta, para garantir a segurança da senha do usuário, ela é criptografada por meio da classe Bcrytpt da biblioteca Flask-Bcrypt.

Para processos que envolvem o usuário estar logado (@login_required), sendo sua identificação feita por seu ID, foi utilizada a biblioteca Flask-Login, conectada à aplicação por meio da classe LoginManager. 

Para a criação de formulários no site, foi empregada a biblioteca WTForms, junto com as devidas validações (wtforms.validators) para cada campo.

Agora, uma breve apresentação de cada uma das páginas do site e suas funcionalidades:

### Homepage

Na página inicial (*homepage*) é possível ter acesso aos posts já criados pelos usuários, com título, corpo, nome do usuário, sua foto e data da criação da postagem.

Também é possível notar os links para a página 'Usuários', 'Contato' e 'Entrar'.

(IMAGEM HOMEPAGE)

A página Usuários tem acesso permitido apenas com login. Ao tentar acessá-la antes de entrar no site, a página faz o direcionamento para a página 'Entrar', onde é possível realizar login ou criar conta.

### Contato

A página Contato contém informações simples de telefone e e-mail da comunidade e seu acesso é livre.

(IMAGEM CONTATO)

### Entrar

Ao tentar acesso na página Usuários ou ao clicar no botão 'Entrar' no canto superior direito da Homepage, temos o direcionamento para a página de Login ou Criar Conta.

(IMAGEM ENTRAR)

Ao criar conta, as validações dos campos do formulário vão verificar se o e-mail já existe, já que ele deve ser único, se o nome de usuário está preenchido e se os campos de senha também. A senha deve ter de 6 a 20 caracteres e o campo de confirmação de senha verifica se o dado inserido é o mesmo do campo 'senha'. As informações incompatíveis com as validações serão informadas na tela.

Após criar conta, o usuário pode realizar o login, com todo o sistema de verificação se e-mail e senha. Automaticamente, o usuário senha direcionado à página da homepage. Porém, agora, ele poderá criar, editar e deletar posts, além de poder ver o perfil de outros usuários.

(IMAGEM HOMEPAGE LOGADO)

### Usuários

Essa página mostra todos os usuários existentes na plataforma, com informações do total de cursos matriculados, número de posts e os cursos da matrícula.

(IMAGEM USUÁRIOS)

### Perfil

No botão 'Meu Perfil' na homepage, o usuário consegue visualizar o próprio perfil. Ele pode ver todos os posts que ele criou no botão 'Meus Posts', o qual direciona a página para a parte inferior, onde os posts aparecem. 

(IMAGEM PERFIL)

Além disso, ele pode fazer a edição do perfil no botão 'Editar Perfil'.

### Editar perfil

Aqui, o usuário pode alterar informações de e-mail, usuário, senha, foto de perfil e cursos matriculados. O banco de dados recebe as atualizações.

(IMAGEM EDITAR PERFIL 1)

(IMAGEM EDITAR PERFIL 2)

Quando um usuário cria uma conta, sua foto de perfil é padrão do site (default). Para alterar a foto de perfil, ele pode escolher um arquivo do computador. Esse arquivo terá seu nome alterado, sendo adicionada uma chave aleatória ao final dele, utilizando-se a biblioteca *secrets*. Isso evita a sobreposição de arquivos no banco de dados no caso de usuários diferentes colocarem fotos com mesmo nome.

### Alterar senha

Caso o usuário opte por fazer alteração de sua senha, ele será direcionado à página que contém um formulário de alteração. Ele deve inserir a nova senha escolhida, fazer sua confirmação e adicionar, por segurança, a senha atual. Esta será verificada no banco de dados por meio do Bcrypt. Se for compatível com o usuário, e se os demais campos seguirem os critérios de validação, a alteração é feita.

(IMAGEM ALTERAR SENHA)

### Criar Post

Aqui, o usuário pode criar e postar um novo tópico. Ele adiciona um título e um corpo. 
Ao salvar, seu post aparecerá em seu perfil e na homepage, onde outros usuários poderão fazer a leitura.

(IMAGEM CRIAR POST)

### Editar ou Deletar Post

Ao clicar no título do próprio post, seja na homepage, seja no próprio perfil, o usuário pode realizar a sua edição ou deletá-lo. 

(IMAGEM EDITAR OU DELETAR POST)

### Outro Perfil

É possível ter acesso ao perfil de outro usuário. Basta clicar sobre a foto de perfil ao lado dos posts, tanto na homepage quanto na página 'Usuários'. Assim, é possível ver todos os posts daquele usuário, além das informações gerais.

(IMAGEM OUTRO PERFIL)

### Post

Ao clicar sobre o título de um post de outro uauário, é possível visualizar o post individualmente, em outra página.
É feita uma verificação se o criador do post é ou não o usuário atual. Se for, ele terá a opção de editar e deletar mencionada acima.

(IMAGEM POST)


