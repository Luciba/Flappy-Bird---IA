# Flappy Clone

Um clone simples do jogo Flappy Bird, desenvolvido em Python utilizando a biblioteca Pygame. O objetivo do projeto é permitir que o jogo seja jogado por uma Inteligência Artificial, que aprenderá a jogar e melhorará seu desempenho com o tempo.

## 📌 Funcionalidades
- Tela inicial com opção de iniciar ou sair do jogo. 
- Passáro animado que pula ao pressionar a tecla ESPAÇO.
- Obstáculos gerados aleatoriamente (canos) que o jogador deve desviar.
- Contador de pontos com base nos obstáculos ultrapassados.
- Tela de "Game Over" ao colidir com os canos, céu ou o chão. 
- Opção de reiniciar ou sair após o fim do jogo. 
- **Modo de treinamento com IA**: O algoritmo **NEAT** será utilizado para treinar redes neurais artificiais, permitindo que a IA aprenda a jogar melhor ao longo das gerações. (EM DESENVOLVIMENTO)

## 🎮 Controles
- **ESPAÇO**: Faz o pássaro pular.
- **R**: Reinicia o jogo após o "Game Over". 
- **ESC**: Sai do jogo na tela inicial ou de "Game Over". 

## 🛠️ Requisitos
- Python 3.x
- Biblioteca Pygame
- Biblioteca **NEAT-Python** para aprendizado de máquina

Para instalar as dependências, use:

```sh
pip install pygame neat-python
```

## 🚀 Como Executar
1. Clone este repositório ou baixe os arquivos.
2. Navegue até a pasta do projeto e execute o seguinte comando no terminal:
```sh
python main.py
```

## 📷 Capturas de Tela
(Tela inicial, gameplay e tela de game over ) (EM DESENVOLVIMENTO)

![Tela Inicial](imgs/Tela%20Inicial.PNG)
<!-- ![Gameplay](images/gameplay.png) -->
![Game Over](imgs/Game%20Over.PNG)


## 🤖 Objetivo com IA
O jogo será integrado com NEAT, um algoritmo de evolução de redes neurais artificiais. O objetivo é que, ao longo das gerações, a IA aprenda estratégias eficazes para maximizar a pontuação, ajustando os pesos das redes neurais para melhorar a tomada de decisão.

## 🏛️ Licença
Este projeto é de código aberto e pode ser utilizado livremente para aprendizado e modificação.

---
Criado por Luciano Junior 🎮

