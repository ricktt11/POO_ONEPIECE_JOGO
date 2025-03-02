class Pirata:
    def __init__(self, nome, bando, recompensa, vida):
        self.nome = nome
        self.bando = bando
        self.recompensa = recompensa
        self.vida = vida
        self.defendendo = False  # Adicionando um atributo para controlar a defesa

    def atacar(self, alvo):
        dano = 10  # Dano base
        print(f"{self.nome} ataca {alvo.nome}, causando {dano} de dano!")
        alvo.receber_dano(dano)

    def defender(self):
        self.defendendo = True  # Ativa a defesa
        print(f"{self.nome} se defende, reduzindo o dano do próximo ataque!")

    def receber_dano(self, dano):
        if self.defendendo:
            dano = dano // 2  # Reduz o dano pela metade se estiver defendendo
            self.defendendo = False  # Desativa a defesa após o ataque
            print(f"{self.nome} defendeu e reduziu o dano para {dano}!")
        self.vida -= dano
        print(f"{self.nome} agora tem {self.vida} de vida!")
        