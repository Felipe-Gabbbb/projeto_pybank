import os
from datetime import datetime
import pickle
from dados import *
from save import *
from receitas import menu_receitas
from despesas import menu_despesas
from metas import menu_metas
from resumo import menu_resumo
from extrato import menu_extrato

data_formatada = agora.strftime("%d/%m/%Y %H:%M")

carregar_dados()

r = ""
while r != "0":
    os.system("cls" if os.name == "nt" else "clear")
    print(f"""
---------------
--- Sigbank.4
--- Menu Principal
--- Data = {data_formatada}
--- 1 = Receitas
--- 2 = Despesas
--- 3 = Resumo financeiro
--- 4 = Metas
--- 5 = Extrato
--- 0 = Sair
---------------
    """)
    r = input("opção: ")
    if r == "1":
        menu_receitas(rec, meses, agora)
    elif r == "2":
        menu_despesas(desp, meses, agora)
    elif r == "3":
        menu_resumo(rec, desp)
    elif r == "4":
        menu_metas(metas, rec, meses, agora)
    elif r == "5":
        menu_extrato(rec, desp, meses)
    elif r == "0":
        print("--- Saindo do programa")
        input("--- Pressione Enter para sair: ")
    else:
        print("--- Opção inválida")
        input("--- Pressione Enter para voltar: ")
salvar_dados(rec, desp, metas)
