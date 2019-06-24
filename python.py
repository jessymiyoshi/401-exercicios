# #PROGRAMA QUE CALCULA A MÉDIA
n1 = int(input("Digite a sua N1: "))
n2 = int(input("Digite a sua N2: "))
n3 = int(input("Digite a sua N3: "))
n4 = int(input("Digite a sua N4: "))

media = (n1+n2+n3+n4)/4
print("Sua média é {}" .format(media))

# #PROGRAMA ESTATISTICA DE LETRA
frase = input("Digite uma frase: ")
letra = input("Digite uma letra: ")

procura = frase.count(letra)
print(procura)

#PROGRAMA MEDIA E ESTATISTICA
qutd = int(input("Digite a quantidade de notas que você tem: "))
soma = 0


for i in range(qutd):
    notas = int(input("Digite uma nota: "))
    soma += notas 

media = soma/qutd
print(media)

#PROGRAMA QUE MOSTRA TUDO
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

soma = numero1+numero2
subtracao = numero1-numero2
multiplicacao = numero1*numero2
divisao = numero1/numero2

resultado = (input("O resultado da soma é {}, subtração {}, multiplicação {}, divisão {}." .format(soma, subtracao, multiplicacao, divisao)))
print(resultado)
