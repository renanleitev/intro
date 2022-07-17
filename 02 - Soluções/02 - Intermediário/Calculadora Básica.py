print('Olá, eu sou a calculadora! Usando dois números, você pode somar, multiplicar ou descobrir qual é o maior número.')
lista = [1, 2, 3, 4, 5]
while True:
    A = float(input('Primeiro número: '))
    B = float(input('Segundo número: '))
    print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair do Programa')
    C = input('Selecione uma das opções: ')
    try:
        if int(C) == lista[0]:
            print(f'A soma entre {A} e {B} é {int(A + B)}.')
            C = input('Selecione uma das opções: ')
        if int(C) == lista[1]:
            print(f'{A} vezes {B} é igual a {int(A * B)}.')
            C = input('Selecione uma das opções: ')
        if int(C) == lista[2]:
            if A > B:
                print(f'{A} é maior que {B}.')
                C = input('Selecione uma das opções: ')
            if B > A:
                print(f'{B} é maior que {A}.')
                C = input('Selecione uma das opções: ')
        if int(C) == lista[4]:
            print('Fim do programa. ')
            break
        elif int(C) == lista[3]:
            continue
    except Exception:
        print('Opção inválida. Fim do programa.')
        break
        





