from pirata import Pirata


class Gorosei(Pirata):
    def __init__(self, nome, recompensa, vida, habilidade_especial):
        super().__init__(nome, "Gorosei", recompensa, vida)
        self.habilidade_especial = habilidade_especial

    def ataque_divino(self, alvo):
        dano = 30
        print(f"{self.nome}, um dos Gorosei, usa {self.habilidade_especial} em {alvo.nome}, causando {dano} de dano!")
        alvo.receber_dano(dano)

# Definição dos cinco Gorosei
Gorosei_1 = Gorosei("Saturn", "indeterminado", 200, "Controle da Gravidade")
Gorosei_2 = Gorosei("Mars", "indeterminado", 200, "Manipulação de Chamas")
Gorosei_3 = Gorosei("V. Nusjuro", "indeterminado", 200, "Espadachim Supremo")
Gorosei_4 = Gorosei("Warcury", "indeterminado", 200,
                    "Força Bruta Incomensurável")
Gorosei_5 = Gorosei("Ju Peter", "indeterminado", 200, "Manipulação Sombria")


class ImuSama(Pirata):
    def __init__(self, nome="Imu-sama", recompensa="indeterminado", vida=450):
        super().__init__(nome, "Governante Supremo", recompensa, vida)

    def ataque_sombra(self, alvo):
        dano = 45
        print(
            f"{self.nome} lança um ataque sombrio sobre {alvo.nome}, causando {dano} de dano!")
        alvo.receber_dano(dano)
