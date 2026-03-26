import random

valores_dificuldades = {
    '1': 10,
    '2': 100,
    '3': 1000,
    '4': 10000,
    '5': 100000,
    '6': 1000000,
    '7': 10000000,
    '8': 100000000,
    '9': 1000000000,
    '10': 10000000000
}

while True:

    while True:
        dificuldade = input('''Qual dificuldade você quer jogar?
1- 0 a 10
2- 0 a 100
3- 0 a 1000
4- 0 a 10000
5- 0 a 100000
6- 0 a 1000000
7- 0 a 10000000
8- 0 a 100000000
9- 0 a 1000000000
10- 0 a 10000000000\n''')

        if dificuldade in valores_dificuldades:
            valor_maximo = valores_dificuldades[dificuldade]
            numero = random.randint(0,valor_maximo)
        else:
            print('Escolha uma opção de 1 a 10\n')
            continue
        
        tentativas = 0

        while True:
                try: 
                    respostas_user = int(input(f'Você acha que o valor sorteado de 0 a {valor_maximo} é quanto? \n'))
                except:
                    print('Somente números inteiros são aceitos')
                    continue

                if respostas_user > numero:
                    tentativas = tentativas + 1

                    print(f"""{respostas_user} é maior do que o número sorteado pelo sistema, tente novamente!
Número de tentativas até aqui: {tentativas}""")
                elif respostas_user < numero:
                    tentativas = tentativas + 1

                    print(f"""{respostas_user} é menor do que o número sorteado pelo sistema, tente novamente!
Número de tentativas até aqui: {tentativas}""")
                elif respostas_user == numero:
                    tentativas = tentativas + 1

                    print(f"""Parabéns!! Você acertou, o valor sorteado foi {numero}.
Número de tentativas até o acerto: {tentativas}""")
                    break
        

        while True:
            continuar_jogo = input("""Você quer jogar novamente?
    1- Sim
    2- Não \n""")
            if continuar_jogo == '1':
                print('Iniciando novo jogo...')
                break
            elif continuar_jogo == '2':
                print('Encerrando jogo...')
                exit()
            else:
                print('Escolha uma das opções fornecidas')
                continue
