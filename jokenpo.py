# Olá, pessoal, escolhi Python porque fui influenciado pelo Professor Secco 😅, quando ele mencionou no vídeo da etapa atual que faria em Py este desafio. 😂

# Eu estudo Py com uma certa regularidade nas disciplinas da universidade, tendo em vista que meu curso superior é centrado em dev. back-end e tenho contato com Py, C e Java nos projetos do curso.  

# Aceito feedback no que precisa melhorar. Ficarei grato e me ajudará a evoluir. 

# linkedin: https://www.linkedin.com/in/welber-nogueira-7705031b2/

# Bom game! Quem vencer 3 partidas, sai vencedor! Boa sorte. 😁



import random

opcoes = ("pedra", "papel", "tesoura")
jogando = True

placar_jogador = 0
placar_computador = 0
placar_empate = 0
total_partidas = 0

while jogando:
    jogador = None
    computador = random.choice(opcoes)
    
    while jogador not in opcoes:
        jogador = input("Escolha uma opção digitando a sua escolha (pedra, papel ou tesoura): ").lower()

    print(f"Jogador: {jogador}")
    print(f"Computador: {computador}")

    if jogador == computador:
        print("Houve um empate!")
        placar_empate += 1
    elif (jogador == "pedra" and computador == "tesoura") or \
         (jogador == "papel" and computador == "pedra") or \
         (jogador == "tesoura" and computador == "papel"):
        print("Você ganhou esta rodada!")
        placar_jogador += 1
    else:
        print("Poxa, cara. O computador venceu!")
        placar_computador += 1
    
    total_partidas += 1

    
    print("\nPlacar Atual:")
    print(f"Jogador: {placar_jogador}")
    print(f"Computador: {placar_computador}")
    print(f"Empates: {placar_empate}")
    print("-" * 20)

    
    if placar_jogador == 3 or placar_computador == 3:
        if placar_jogador == 3:
            print("\nParabéns! Você venceu o melhor de 3!")
        else:
            print("\nQue pena! O computador venceu o melhor de 3!")

       
        print(f"\nEstatísticas finais:")
        print(f"Total de partidas jogadas: {total_partidas}")
        print(f"Vitórias do jogador: {placar_jogador} ({(placar_jogador/total_partidas)*100:.2f}%)")
        print(f"Vitórias do computador: {placar_computador} ({(placar_computador/total_partidas)*100:.2f}%)")
        print(f"Empates: {placar_empate} ({(placar_empate/total_partidas)*100:.2f}%)")
        
        resposta = None
        while resposta not in ("sim", "não"):
            resposta = input("Deseja jogar novamente? (sim/não): ").lower()
        
        if resposta == "não":
            jogando = False
            print("Até logo. Valeu!")
        else:
            placar_jogador = 0
            placar_computador = 0
            placar_empate = 0
            total_partidas = 0
    else:
        resposta = None
        while resposta not in ("sim", "não"):
            resposta = input("Deseja continuar para a próxima partida? (sim/não): ").lower()
        
        if resposta == "não":
            jogando = False
            print("Até logo. Valeu!")
