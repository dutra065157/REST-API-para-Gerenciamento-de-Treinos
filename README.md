Este projeto consiste em um aplicativo mobile integrado a uma API REST desenvolvida em Python com Django.
utilizando o framework Flet para a interface do usuário. O aplicativo permite o gerenciamento de treinos, incluindo cadastro de alunos,
listagem de alunos, acompanhamento do progresso e registro de aulas realizadas.

Funcionalidades

Cadastro de Aluno: Permite cadastrar novos alunos, informando nome, e-mail, faixa e data de nascimento.

Listagem de Alunos: Exibe a lista de todos os alunos cadastrados.

Progresso do Aluno: Permite acompanhar o progresso de cada aluno, incluindo a faixa atual,
total de aulas realizadas e aulas necessárias para a próxima faixa.

Aula Realizada: Permite registrar aulas realizadas, informando a quantidade e o aluno.
Atualização de Aluno: Permite atualizar os dados de um aluno, como nome, e-mail, faixa e data de nascimento.

Tecnologias

Front-end:

Flet: Framework para criação de interfaces de usuário em Python.

Requests: Biblioteca para realizar requisições HTTP à API REST.

Back-end:

Python: Linguagem de programação.

Django: Framework web de alto nível.

Django REST Framework: Framework para criação de APIs REST, ninja.

Arquitetura
O aplicativo mobile (front-end) comunica-se com a API REST (back-end) através de requisições HTTP. A API é responsável por interagir com o banco de dados e fornecer os dados para o aplicativo.
