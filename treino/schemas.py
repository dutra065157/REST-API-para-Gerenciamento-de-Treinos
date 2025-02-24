# Importa ModelSchema para criar schemas baseados em modelos e Schema para schemas genéricos.
from ninja import ModelSchema, Schema
from .models import Alunos  # Importa o modelo Alunos do arquivo models.py.
# Importa Optional do módulo typing para definir campos opcionais.
from typing import Optional


# Define um schema para o modelo Alunos, herdando de ModelSchema.
class AlunosSchema(ModelSchema):

    class Meta:  # Define metadados para o schema.
        model = Alunos  # Especifica o modelo base para o schema, que é Alunos.
        # Lista os campos do modelo que serão incluídos no schema.
        fields = ['nome', 'email', 'faixa', 'data_nascimento']
        # Isso significa que o schema AlunosSchema terá os campos 'nome', 'email', 'faixa' e 'data_nascimento' do modelo Alunos.


# Define um schema para representar o progresso de um aluno, herdando de Schema.
class ProgressoAlunoSchema(Schema):
    email: str  # Define o campo email como uma string.
    nome: str  # Define o campo nome como uma string.
    faixa: str  # Define o campo faixa como uma string.
    total_aulas: int  # Define o campo total_aulas como um inteiro.
    # Define o campo aulas_necessarias_para_proxima_faixa como um inteiro.
    aulas_necessarias_para_proxima_faixa: int
    # Este schema é usado para validar e serializar dados relacionados ao progresso do aluno.


# Define um schema para representar uma aula realizada, herdando de Schema.
class AulaRealizadaSchema(Schema):
    # Define o campo qtd (quantidade) como um inteiro opcional, com valor padrão 1.
    qtd: Optional[int] = 1
    email_aluno: str  # Define o campo email_aluno como uma string.
    # Este schema é usado para validar e serializar dados de aulas realizadas, incluindo a quantidade (opcional) e o email do aluno.
