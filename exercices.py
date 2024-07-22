# 🚀 Exercício 1: Crie uma função que receba dois números e retorne o maior deles.


def two_numbers(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


result = two_numbers(10, 20)
print(f"O maior número é: {result}")


# 🚀 Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.
list_numbers = [1, 2, 3, 4, 5]
soma = sum(list_numbers)
qtde = len(list_numbers)

media = soma / qtde

print(f"A média aritmética da lista é: {media}")
# Exercício 3: Faça um programa que, dado um valor n qualquer, tal que n > 1, imprima na tela um quadrado feito de asteriscos de lado de tamanho n. Por exemplo:


def draw_square(n):

    for row in range(n):

        print(n * "*")


# 🚀 Exercício 4: Crie uma função que receba uma lista de nomes e retorne o nome com a maior quantidade de caracteres. Por exemplo, para ["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"], o retorno deve ser "Fernanda".
def finds_biggest_name(names):
    biggest_name = names[0]
    for name in names:
        if len(name) > len(biggest_name):
            biggest_name = name
    return biggest_name


# 🦜 Uma dica: Utilize a função len() para verificar o tamanho do nome.

# Exercício 5: Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Crie uma função que retorne dois valores em uma tupla contendo a quantidade de latas de tinta a serem compradas e o preço total a partir do tamanho de uma parede (em m²).

# Exercício 6: Crie uma função que receba os três lado de um triângulo e informe qual o tipo de triângulo formado ou "não é triangulo", caso não seja possível formar um triângulo.
