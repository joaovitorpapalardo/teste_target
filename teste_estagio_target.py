#TESTE 1:
indice = 13
soma = 0
k = 0

while k < indice:
    k = k + 1
    soma = soma + k

print(soma)
#O valor final da soma vai ser = 91.

print()

#TESTE 2:
#Calcula a sequencia de fibonacci ate o numero que antecede o valor que o usuario digitar
def calcular_fibonacci(n):
    fibonacci = [0, 1]
    while fibonacci[-1] < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[:-1]

#Verifica se o numero digitado pelo usuario esta na sequencia do calculo feito acima(calcular_fibonacci)
def verificar_sequencia(numero):
    sequencia_fibonacci = calcular_fibonacci(numero)
    if numero in sequencia_fibonacci:
        return True
    else:
        return False

num_user = int(input("Digite um número para verificar se esta presente na sequência de Fibonacci: "))

sequencia = calcular_fibonacci(num_user)

print("Sequência de Fibonacci:", sequencia)

#Exibe a mensagem na tela caso o numero esteja presente ou nao
if verificar_sequencia(num_user):
    print(f"O número {num_user} está presente na sequência de Fibonacci.")
else:
    print(f"O número {num_user} não está presente na sequência de Fibonacci.")


#TESTE 3)
# a) 1, 3, 5, 7, 9 / numeros impares
# b) 2, 4, 8, 16, 32, 64, 128 / dobro do anterior
# c) 0, 1, 4, 9, 16, 25, 36, 49 / sao os numero natural ao quadrado
# d) 4, 16, 36, 64, 100 / numero par ao quadrado
# e) 1, 1, 2, 3, 5, 8, 13 / sequencia de fibonacci
# f) 2, 10, 12, 16, 17, 18, 19, 20 / acredito que seja apenas uma continuacao

#TESTE 4)
#Primeiro iria ligar o primeiro interruptor e esperar alguns minutos, iria desligar e ligar outro interruptor,
#apos isso iria para a sala que contem as lampadas e saberia que a lampada acesa foi do interruptor que deixei ligado,
#a lampada apagada e quente seria do primeiro interruptor que liguei e esperei uns minutos, ja a que esta apagada e fria,
#seria do interruptor que não toquei.
    
print()

#Teste 5)
def inverter(string):
    inverted_string = ""
    for i in range(len(string) - 1, -1, -1):
        inverted_string += string[i]
    return inverted_string

string = "Hello world"
string_invertida = inverter(string)

print("String original:", string)
print("String invertida:", string_invertida)

    