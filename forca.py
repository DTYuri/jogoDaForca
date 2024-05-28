#          Vinicius Radaelli da Silva (1135940)      Yuri Duarte Theisen (1125371)

import os, time
def limparTela():
    os.system("cls")
limparTela()

def saudacao():
    print('''
                          
                    ╔══╗───────  ─────╔╗─────╔╗───  ───────  ────────────  ─╔╗────  ╔═╗─────────────╔╗
                    ║╔╗║╔═╗╔══╗  ╔═╦═╗╠╣╔═╦╗╔╝║╔═╗  ╔═╗─╔═╗  ─╔╗╔═╗╔═╗╔═╗  ╔╝║╔═╗─  ║═╣╔═╗╔╦╗╔═╗╔═╗─║║
                    ║╔╗║║╩╣║║║║  ╚╗║╔╝║║║║║║║╬║║╬║  ║╬╚╗║╬║  ─╠╣║╬║║╬║║╬║  ║╬║║╬╚╗  ║╔╝║╬║║╔╝║═╣║╬╚╗║║
                    ╚══╝╚═╝╚╩╩╝  ─╚═╝─╚╝╚╩═╝╚═╝╚═╝  ╚══╝╚═╝  ╔╝║╚═╝╠╗║╚═╝  ╚═╝╚══╝  ╚╝─╚═╝╚╝─╚═╝╚══╝╠╣
                    ───────────  ─────────────────  ───────  ╚═╝───╚═╝───  ───────  ────────────────╚╝
Iniciando...
'''
    )
saudacao()

time.sleep(3)
limparTela()

def iniciar_jogo():
    desafiante = input("DESAFIANTE, qual o seu nome? ")
    competidor = input("COMPETIDOR, qual o seu nome? ")

    limparTela()
    palavraChave = input("Palavra Chave: ")
    dica1 = input("Digite a Dica1: ")
    dica2 = input("Digite a Dica2: ")
    dica3 = input("Digite a Dica3: ")
    dicas = [dica1, dica2, dica3]
    letras_reveladas = []
    for letra in palavraChave:
        if letra.isalpha():
            letras_reveladas.append('*')
        else:
            letras_reveladas.append(letra)
    letras_digitadas = []
    dicasPedidas = 0
    tentativas_erradas = 0
    
    while True: 
        limparTela()
        print("Descubra a palavra:", " ".join(letras_reveladas))
        print("Letras digitadas:", ' '.join(letras_digitadas))
        print(f"Erros: {tentativas_erradas} de 6")
        print("(0) Para sair ")
        print("(1) Jogar ")
        print("(2) Pedir dica ")
        escolha = input("Escolha: ")

        if escolha == "2":
            if dicasPedidas < 3:
                print(dicas[dicasPedidas])
                dicasPedidas = dicasPedidas + 1
                input()
            else:
                print("Você não tem mais dicas!")
                input()
        elif escolha == "1": 
            letra = input("Digite uma letra: ")
            letras_digitadas.append(letra) 
            if letra in palavraChave:
                for i in range(len(palavraChave)):
                    if palavraChave[i] == letra:
                        letras_reveladas[i] = letra
                if '*' not in letras_reveladas: 
                    limparTela()
                    print(f"{competidor} Parabéns, você venceu o jogo!!")
                    input('''
                          Aperte qualquer tecla para continuar: ''')
                    break 
            else:
                tentativas_erradas = tentativas_erradas + 1
                limparTela()
                print("Letras não encontradas na palavra chave.")
            
            if (tentativas_erradas == 6):
                print(f"{competidor} você perdeu ")
                print(f"{desafiante} ganhou o jogo!")
                input("Aperte qualquer tecla para continuar: ")
                break 
        elif escolha == "0":
            break

    limparTela()
    print("Digite (1) para reiniciar o jogo")
    print("Digite (2) para sair")
    opcao = input("Escolha: ")
    if opcao == "1":
        limparTela()
        iniciar_jogo() 
    elif opcao == "2":
        limparTela()
    else:
        limparTela()
        print("Opção inválida")

iniciar_jogo()