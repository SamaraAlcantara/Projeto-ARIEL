import sqlite3
from time import sleep
#Apresentação 
def id_Clientes():
    id_cliente = int(input("Por favor, informe o número do cliente: "))
    print("Olá, aqui é o Ariel, que bom conversar com você", id_cliente,", no que posso te ajudar hoje?")

#Menus código
def menu_Principal():
    print("COMPUTECH TECNOLOGIA")
    print("Menu de Opções \n 1. Resoluções de Problemas \n 2. Ocorrências e Reclamações \n 3. Atendimento Financeiro e Comercial \n 4. Encerrar atendimento")

def menu_Problemas():
    print(10*("*"))
    print("Menu Soluções")
    print(10*("*"))
    print(" 1. Conexão Intermitente \n 2. Erros de rede \n 3. Velocidade baixa \n 4. Problemas com o cabeamento \n 5. Retornar ao Menu Principal")

def menu_Ocorrencias():
    print(10*("*"))
    print("Ocorrências e Reclamações")
    print(10*("*"))
    print(" 1. Abrir ocorrência de chamado técnico \n 2. Realizar reclamação \n 5. Retornar ao Menu Principal")
   
def menu_FinanceiroComercial():
    print(10*("*"))
    print("Para atendimento referente ao departamento financeiro ou comercial, por favor entrar em contato pelo e-mail conputech@computech.com.br ou pelo telefone (88) 3333 3444")
    print(10*("*"))
    menu_Principal()

#Código
id_Clientes()
menu = 0
while menu != 4:
    print("\n")
    menu_Principal()
    menu = int(input("Hummm, o que você quer fazer agora? "))
    if menu == 1: #problemas
        menu_Problemas()
        cliente = int(input("Entendo, me diz no que posso te ajudar: "))
    elif menu == 2:
        menu_Ocorrencias()
        cliente = int(input("Uma pena que hoje não foi possível te ajudar, mas nossa equipe técnica tá a postos para resolver qualquer problema. O que você quer fazer agora? "))
    elif menu == 3:
        menu_FinanceiroComercial()
        sleep(2)
        menu_Principal()
    elif menu == 4:
        print("Haaaa, fim de jogo. Que bom pude te ajudar e te conhecer melhor! Vou estar sempre aqui, até á proxima!\n")
        sleep(1)
        print("Computech Tecnologia - Solução em Inovação")
    else:
        print("Hummm, não tenho essa opção, você pode me confirmar novamente qual caminho vamos seguir?")
        sleep(1)
        menu_Principal
   



