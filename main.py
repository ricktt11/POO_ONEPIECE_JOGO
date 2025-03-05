from heros import UsuarioAkumaNoMi, Espadachim, Genetica_germa
from boss import Gorosei_1, Gorosei_2, Gorosei_3, Gorosei_4, Gorosei_5, ImuSama

def batalha(herois, inimigos):
    turno = 0  # Para alternar ataques dos Gorosei
    
    for inimigo in inimigos:
        print(f"\nInimigo {inimigo.nome} apareceu!")
        while inimigo.vida > 0 and any(h.vida > 0 for h in herois):
            for heroi in herois:
                if heroi.vida <= 0:
                    continue
                escolha = input(f"{heroi.nome}: [1]Atacar / [2]Defender: ").strip().lower()
                if escolha == '1':
                    if isinstance(heroi, UsuarioAkumaNoMi):
                        heroi.usar_poder(inimigo)
                    elif isinstance(heroi, Espadachim):
                        heroi.ataque_com_espada(inimigo)
                    elif isinstance(heroi, Genetica_germa):
                        heroi.poder_german(inimigo)
                elif escolha == '2':
                    heroi.defender()
                
                if inimigo.vida <= 0:  # Se o inimigo for derrotado, a batalha para
                    print(f"{inimigo.nome} foi derrotado!")
                    break
            
            if inimigo.vida > 0:
                heroi_alvo = herois[turno % len(herois)]
                while heroi_alvo.vida <= 0:  # Escolhe um herói vivo
                    turno += 1
                    heroi_alvo = herois[turno % len(herois)]
                
                if isinstance(inimigo, Gorosei_1.__class__):  # Verifica se é um Gorosei
                    inimigo.ataque_divino(heroi_alvo)
                elif isinstance(inimigo, ImuSama):  # Se for Imu-sama, usa o especial
                    inimigo.ataque_sombra(heroi_alvo)
                else:
                    inimigo.atacar(heroi_alvo)
                
                turno += 1

                if heroi_alvo.vida <= 0:  # Verifica se o herói foi derrotado
                    print(f"{heroi_alvo.nome} foi derrotado!")
                
            if all(h.vida <= 0 for h in herois):  # Se todos os heróis forem derrotados
                print("Todos os heróis foram derrotados! GAME OVER.")
                return
    
    print("\nVitória! Imu-Sama foi derrotados!")
    print("\nVamos pegar o ONE PIECEEE!!!")

herois = [ 
    UsuarioAkumaNoMi("Luffy", "Chapéu de Palha", 3000000000, 180, "Gomu Gomu no Mi"),
    Espadachim("Zoro", "Chapéu de Palha", 1500000000, 165, 3),
    Genetica_germa("Sanji", "Chapéu de Palha", 1000000000, 170)
]

inimigos = [Gorosei_1, Gorosei_2, Gorosei_3, Gorosei_4, Gorosei_5, ImuSama()]
batalha(herois, inimigos)

