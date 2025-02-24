# Importa o módulo math, que contém funções matemáticas, como logaritmo.
import math

# Cria um dicionário que mapeia as faixas de artes marciais para um número inteiro, representando a ordem das faixas.
order_belt = {'Branca': 0, 'Azul': 1, 'Roxa': 2, 'Marrom': 3, 'Preta': 4}

# Define uma função chamada calculate_lesson_to_upgrade que recebe um número inteiro n como entrada.


def calculate_lesson_to_upgrade(n):
    # Esta função calcula o número de aulas necessárias para um aluno avançar para a próxima faixa, com base em sua faixa atual (representada por n).

    d = 1.47  # Define uma constante d com o valor 1.47.
    # Define uma constante k. O valor de k é calculado dividindo 30 pelo logaritmo natural de d.
    k = 30 / math.log(d)
    # Calcula o número de aulas necessárias. O número de aulas é calculado multiplicando k pelo logaritmo natural da soma de n e d.
    aulas = k * math.log(n + d)

    # Arredonda o número de aulas para o inteiro mais próximo e retorna o resultado.
    return round(aulas)
    # A função calculate_lesson_to_upgrade usa uma fórmula que envolve logaritmos para calcular o número de aulas necessárias para um aluno mudar de faixa. As constantes d e k são usadas nesta fórmula. A função retorna o número de aulas arredondado para o inteiro mais próximo.
