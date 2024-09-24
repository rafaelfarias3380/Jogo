"""
Proposito: Criar um jogo de pedra, papel e tesoura
13/08/2024
De Rafael para professor Berssa
"""

# --> Biblioteca
from modules import clrScreen, displayLine, displayMsg, displayMsgCenter, displayHeader, getUserOption, validateUserOption, displayHeaderT #Importa funções do arquivo "modules.py"
from ppt import startPPT #Importa funções do arquivo "ppt.py"
from parimpar import startPI
# --> Constantes (👁️‍🗨️), Variáveis e Listas

# --> Funções

# --> Main
msgs = ["Seja bem-vinde aos jogos", "Pedra-Papel-Tesoura", "Par ou impár"]
displayHeader(msgs)
msgs = ["Digite 0 --> Sair",
        "Digite 1 --> Pedra-Papel-Tesoura",
        "Digite 2 --> Par ou ímpar"]
displayHeaderT(msgs)
opUser = getUserOption("Sua escolha")
while not validateUserOption(opUser, ["0", "1", "2"]):
  opUser = getUserOption("Sua escolha:")
if(opUser == "1"):
  startPPT()
elif(opUser == "2"):
  startPI()
else:
  displayMsg("Falou então 😔...")
  


