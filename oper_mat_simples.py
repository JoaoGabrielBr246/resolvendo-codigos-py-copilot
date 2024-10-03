n1 = int(input('Digite 1 número: '))
n2 = int(input('Digite outro número: '))

op = input('Você deseja somar ou subtrair? Ex.: + ou -  ')

if op == '+':
    resultado = n1 + n2
    print(resultado)
elif op == '-':
    resultado = n1 - n2
    print(resultado)
else:
    print('Opção inválida!')