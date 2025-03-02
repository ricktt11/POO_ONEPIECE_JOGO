class Pirata:
    def __init__(self, nome, bando, recompensa, vida):
        self.nome = nome
        self.bando = bando
        self.recompensa = recompensa
        self.vida = vida
        self.defendendo = False
        self.__dano_base = 10  # Agora é uma variável privada

    def atacar(self, alvo):
        print(f"{self.nome} ataca {alvo.nome}, causando {self.__dano_base} de dano!")
        alvo.receber_dano(self.__dano_base)

    def defender(self):
        self.defendendo = True
        print(f"{self.nome} se defende, reduzindo o dano do próximo ataque!")

    def receber_dano(self, dano):
        if self.defendendo:
            dano //= 2
            self.defendendo = False
            print(f"{self.nome} defendeu e reduziu o dano para {dano}!")
        self.vida -= dano
        print(f"{self.nome} agora tem {self.vida} de vida!")

    # Getter e Setter para dano_base
    def get_dano_base(self):
        return self.__dano_base

    def set_dano_base(self, novo_dano):
        self.__dano_base = novo_dano
