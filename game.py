def mensagem(txt):
    colors = {
        'amarelo': '\033[33m',
        'azul': '\033[34m',
        'limpa': '\033[m'
    }
        
    tamanho = len(txt) + 4
    line = "-" * tamanho

    print(f"{colors['azul']}{line}{colors['limpa']}\n")
    print(f"  {colors['amarelo']}{txt}{colors['limpa']}\n")
    print(f"{colors['azul']}{line}{colors['limpa']}")

def is_number(n):
    try:
        int(n)
    except ValueError:
        return False
    return True


def computer_number_random():
    from random import randint
    c = randint(1, 6)
    return c


def magic_ball_number_random():
    from random import randint
    mg = randint(1, 6)
    return mg


def user_number_input(msg, mg, c):
    while True:
        print(msg)
        v = input().lower()
        if v == 'admin':
            print("\033[31mModo Administrador Ativo:\033[m")
            print("\033[34mValores Sorteados:\033[m")
            print(f"Valor do computador: {c}")
            print(f"Valor da bola magica: {mg}")
            continue
        elif not is_number(v):
            print("Valor digitado não é um número, tente novamente.")
            continue
        else:
            v = int(v)
            if v < 1 or v > 6:
                print("Numero não aceito, o número deve estar entre 1 e 100.")
                continue
            else:
                break
    return v


def main_1(d, mg):
    cc = bool()
    from os import system
    mensagem("RPG com Seth")
    print("Vamos escolher números e aquele que for igual a minha bola mágica ganha um ponto e ele é melhor de três.")
    print("Para Jogar custa R$ 5,00")
    print("Saldo: R$ 25,00")
    system('pause')
    print("Beleza! Prepare-se para sofrer hehehehe.")
    while d > 0:
        d -= 5
        c = computer_number_random()
        if d == 0 and cc == False:
            break
        if d == 0 and cc == True:
            mensagem("Resultado: Desafiante Sem Grana")
            print("Você não tem o dom para jogar esse jogo, mas se quiser, pode tentar.")
            exit(0)
        valor = user_number_input("Digite um valor", mg, c)
        if valor != mg and c != mg:
            system('pause')
            mensagem("Resultado: Empate")
            print("Inacreditável, nos não acertamos o valor de minha bola mágica")
            print(f"Seu saldo atual é R${d}")
            system('pause')
            cc = False
            mg = magic_ball_number_random()
            mensagem("RPG com Seth")
            continue
        elif valor != mg and c == mg:
            cc = True
            system('pause')
            mensagem("Resultado: Seth Venceu")
            print("Aha, perdeu seu ignorante, eu acertei.")
            while True:
                print("Deseja jogar de novo? Aposto que não ganha [S/N].")
                print(f"Lembrando que seu saldo é de R${d}")
                rs = input().upper().strip()
                if rs == 'S' or rs == 'N':
                    break
                else:
                    print("Digite uma escolha válida.\n")
                    continue
            if rs == 'S':
                print('Até que você é corajoso. Vamos jogar.')
                system('pause')
                continue
            else:
                print("Você desiste muito fácil. Espero-te na próxima vez para te massacrar.")
        else:
            system('pause')
            mensagem("Resultado: Desafiante Venceu")
            print("Caramba! Isso é impossível, você ganhou. Quero uma revanche!")
            d += 10
            while True:
                print("Deseja jogar de novo?! Certeza que foi sorte [S/N].")
                print(f"Lembrando que seu saldo é de R${d}.")
                r = input().upper().strip()
                if r == 'S' or r == 'N':
                    break
                else:
                    print("Digite uma escolha válida.\n")
                    continue
            if r == 'S':
                print("Vamos lá, agora se você ganhar você receberá R$20.")
                main_2(d, mg)
                exit(0)
            else:
                print("Bom, ainda penso que você trapaceou, se quiser minha consideração tem que ganhar de mim na"
                      "revanche")
                break
    mensagem("Resultado: Sem Grana")
    print("Bom apostamos toda nossa grana e não podemos continuar, provavelmente minha bola mágica está com problema."
          "Te vejo em breve para outra partida.")


def main_2(d, mg):
    from os import system
    mensagem("RPG com Seth, a Revanche")
    print("Vamos lá, agora se você ganhar você receberá R$20.")
    while True:
        c = computer_number_random()
        valor = user_number_input("Digite um valor", mg, c)
        if valor != mg and c != mg:
            system('pause')
            mensagem("Resultado: Empate")
            print("Inacreditável, nos não acertamos o valor de minha bola mágica")
            print(f"Seu saldo atual é {d}")
            system('pause')
            mg = magic_ball_number_random()
            mensagem("RPG com Seth")
            continue
        elif valor != mg and c == mg:
            system('pause')
            mensagem("Resultado: Seth Venceu")
            print("Aha, perdeu, eu sabia que você teve sorte.")
            break
        else:
            system('pause')
            mensagem("Resultado: Desafiante Venceu")
            print("Impressionante, você ganhou. Eu errei sobre você.")
            d += 20
            print(f"Seu saldo total é de R${d}.")
            break


# Programa Principal
if __name__ == '__main__':
    dinheiro_jogador = int(25)
    bola_magica = magic_ball_number_random()
    main_1(dinheiro_jogador, bola_magica)
