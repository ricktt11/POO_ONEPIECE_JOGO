# Projeto POO - One Piece Battle

## Descrição
Este projeto implementa um sistema de batalha baseado no universo de *One Piece* utilizando conceitos de **Programação Orientada a Objetos (POO)**. O jogo permite que o jogador controle personagens como **Luffy, Zoro e Sanji** para enfrentar inimigos poderosos como os **Gorosei e Imu-Sama**.

O código está modularizado em arquivos distintos para melhor organização:
- `pirata.py`: Classe base `Pirata` e encapsulamento de atributos.
- `heros.py`: Classes derivadas dos heróis (`UsuarioAkumaNoMi`, `Espadachim`, `Genetica_germa`).
- `boss.py`: Definição dos chefões (`Gorosei` e `ImuSama`).
- `main.py`: Lógica de batalha e execução do jogo.

---
## Funcionalidades
- **Herança**: Personagens herdam características da classe base `Pirata`.
- **Encapsulamento**: Uso de atributos privados e métodos para acesso seguro aos dados.
- **Polimorfismo**: Métodos sobrescritos para ataques especiais de cada personagem.
- **Interatividade**: O jogador pode escolher entre atacar ou defender.
- **Sistema de batalha**: Turnos entre heróis e inimigos, com vida e dano ajustáveis.

---
## Como Executar

### Pré-requisitos
- Python 3 instalado
- Clonar ou baixar o repositório

### Passos
1. No terminal, navegue até a pasta do projeto.
2. Execute o seguinte comando:
   ```bash
   python main.py
   ```
3. Siga as instruções na tela para participar da batalha!

---
## Estrutura do Código
```
📂 projeto_poo_one_piece
│── pirata.py   # Classe base dos personagens
│── heros.py    # Classes dos heróis
│── boss.py     # Classes dos chefões
│── main.py     # Execução do jogo
│── README.md   # Documentação do projeto
```

---
## Evidências de Resultados Esperados
### Exemplo de Execução
```
Inimigo Saturn apareceu!
Luffy: [1]Atacar / [2]Defender: 1
Luffy usa o poder do despertar da Gomu Gomu no Mi em Saturn, causando 35 de dano!
Saturn agora tem 165 de vida!
Saturn, um dos Gorosei, usa Controle da Gravidade em Luffy, causando 30 de dano!
Luffy agora tem 150 de vida!
```

O jogo continua até que todos os inimigos sejam derrotados ou os heróis percam.

---
## Autor
- Rick Theo - Desenvolvimento e implementação.

---
## Observação
Para uma experiência melhor, pode-se adicionar melhorias como cores no terminal usando `colorama`, salvar progresso em JSON ou criar um modo multiplayer.

Divirta-se na batalha pelo *One Piece*! ☠️🏴‍☠️

![Image](https://github.com/user-attachments/assets/64bb7485-f033-4d70-858d-a13de8275b4c)
