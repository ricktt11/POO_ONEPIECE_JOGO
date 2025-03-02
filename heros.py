from pirata import Pirata


class UsuarioAkumaNoMi(Pirata):
    def __init__(self, nome, bando, recompensa, vida, akuma_no_mi):
        super().__init__(nome, bando, recompensa, vida)
        self.akuma_no_mi = akuma_no_mi

    def usar_poder(self, alvo):
        dano = 35
        print(f"{self.nome} usa o poder do despertar da {self.akuma_no_mi} em {alvo.nome}, causando {dano} de dano!")
        alvo.receber_dano(dano)


class Espadachim(Pirata):
    def __init__(self, nome, bando, recompensa, vida, quantidade_espadas):
        super().__init__(nome, bando, recompensa, vida)
        self.quantidade_espadas = quantidade_espadas

    def ataque_com_espada(self, alvo):
        dano = 10 * self.quantidade_espadas
        print(f"{self.nome} ataca {alvo.nome} com {self.quantidade_espadas} espadas, causando {dano} de dano!")
        alvo.receber_dano(dano)


class Genetica_germa(Pirata):
    def poder_german(self, alvo):
        dano = 25
        print(
            f"{self.nome} usa o poder do seu fator de linhagem em {alvo.nome}, causando {dano} de dano!")
        alvo.receber_dano(dano)
