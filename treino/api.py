# Importa a classe Router do módulo ninja para criar rotas de API.
from ninja import Router
# Importa os schemas definidos para validação de dados.
from .schemas import AlunosSchema, ProgressoAlunoSchema, AulaRealizadaSchema
# Importa os modelos de dados Alunos e AulasConcluidas.
from .models import Alunos, AulasConcluidas
# Importa a classe HttpError para tratamento de erros HTTP.
from ninja.errors import HttpError
# Importa a classe List do módulo typing para tipagem de listas.
from typing import List
# Importa todas as funções e variáveis do módulo graduacao.
from .graduacao import *
# Importa o módulo date do datetime para trabalhar com datas.
from datetime import date


# Cria um objeto Router para agrupar as rotas relacionadas a treinos.
treino_router = Router()


# Decorador para definir uma rota POST na raiz do router.
@treino_router.post('/', response={200: AlunosSchema})
# Define a função para criar um novo aluno.
def criar_aluno(request, aluno_schema: AlunosSchema):
    # Os dados do aluno são esperados no corpo da requisição e devem corresponder ao schema AlunosSchema.

    # Extrai o nome do aluno do dicionário do schema.
    nome = aluno_schema.dict()['nome']
    # Extrai o email do aluno do dicionário do schema.
    email = aluno_schema.dict()['email']
    # Extrai a faixa do aluno do dicionário do schema.
    faixa = aluno_schema.dict()['faixa']
    # Extrai a data de nascimento do aluno do dicionário do schema.
    data_nascimento = aluno_schema.dict()['data_nascimento']

    # Verifica se já existe um aluno com o mesmo email.
    if Alunos.objects.filter(email=email).exists():

        # Se o email já existe, retorna um erro 400.
        raise HttpError(400, "E-mail já cadastrado.")

    aluno = Alunos(nome=nome, email=email, faixa=faixa,  # Cria um novo objeto Aluno com os dados fornecidos.
                   data_nascimento=data_nascimento)
    aluno.save()  # Salva o novo aluno no banco de dados.

    return aluno  # Retorna o objeto aluno criado.


# Decorador para definir uma rota GET em /alunos/.
@treino_router.get('/alunos/', response=List[AlunosSchema])
def listar_alunos(request):  # Define a função para listar todos os alunos.

    alunos = Alunos.objects.all()  # Busca todos os alunos no banco de dados.
    return alunos  # Retorna a lista de alunos.


# Rota GET para obter o progresso de um aluno.
@treino_router.get('/progresso_aluno/', response={200: ProgressoAlunoSchema})
# Função que retorna o progresso do aluno com base no email.
def progresso_aluno(request, email_aluno: str):

    aluno = Alunos.objects.get(email=email_aluno)  # Busca o aluno pelo email.
    faixa_atual = aluno.get_faixa_display()  # Obtém a faixa atual do aluno.
    n = order_belt.get(faixa_atual, 0)  # Obtém a ordem da faixa atual.
    # Calcula o número de aulas para a próxima faixa.
    total_aulas_proxima_faixa = calculate_lesson_to_upgrade(n)
    total_aulas_concluidas_faixa = AulasConcluidas.objects.filter(
        # Conta as aulas concluídas na faixa atual.
        aluno=aluno, faixa_atual=aluno.faixa).count()

    # Calcula as aulas faltantes.
    aulas_faltantes = total_aulas_proxima_faixa - total_aulas_concluidas_faixa

    return {  # Retorna um dicionário com o progresso do aluno.
        "email": aluno.email,
        "nome": aluno.nome,
        "faixa": faixa_atual,
        "total_aulas": total_aulas_concluidas_faixa,
        "aulas_necessarias_para_proxima_faixa": aulas_faltantes
    }


# Rota POST para marcar aulas realizadas.
@treino_router.post('/aula_realizada/', response={200: str})
# Função para marcar aulas realizadas.
def aula_realizada(request, aula_realizada: AulaRealizadaSchema):
    # Obtém a quantidade de aulas do schema.
    qtd = aula_realizada.dict()['qtd']
    # Obtém o email do aluno do schema.
    email_aluno = aula_realizada.dict()['email_aluno']

    if qtd <= 0:  # Verifica se a quantidade de aulas é válida.
        # Retorna erro se a quantidade for inválida.
        raise HttpError(400, "Quantidade de aulas dever ser maior que zero")

    aluno = Alunos.objects.get(email=email_aluno)  # Busca o aluno pelo email.

    for _ in range(0, qtd):  # Loop para criar as aulas realizadas.
        ac = AulasConcluidas(  # Cria um objeto AulasConcluidas para cada aula realizada.
            aluno=aluno,
            faixa_atual=aluno.faixa
        )

        ac.save()  # Salva a aula realizada no banco de dados.
    # Retorna mensagem de sucesso.
    return 200, f"Aula marcada com Sucessor para aluno {aluno.nome}"


# Rota PUT para atualizar os dados de um aluno.
@treino_router.put('/alunos/{aluno_id}', response=AlunosSchema)
# Função para atualizar os dados do aluno.
def update_aluno(request, aluno_id: int, aluno_data: AlunosSchema):
    aluno = Alunos.objects.get(id=aluno_id)  # Busca o aluno pelo ID.
    idade = date.today() - aluno.data_nascimento  # Calcula a idade do aluno.

    # Verifica se o aluno é menor de idade e se a faixa é válida.
    if int(idade.days / 365) < 18 and aluno_data.dict()['faixa'] in ('A', 'R', 'M', 'P',):
        # Retorna erro se a faixa for inválida para a idade.
        raise HttpError(400, 'Menores de 18 anos poder receber essa faixa')

    # Itera sobre os atributos do schema.
    for attr, value in aluno_data.dict().items():
        if value:  # Verifica se o valor do atributo foi fornecido.
            # Define o valor do atributo no objeto aluno.
            setattr(aluno, attr, value)
    aluno.save()  # Salva as alterações no banco de dados.
    return aluno  # Retorna o objeto aluno atualizado.
