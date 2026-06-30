from receitas import *
from despesas import *
from metas import *
def menu_extrato(rec, desp, meses):

    print("--- Extrato do mês")
    print("--- Meses: Jan, Fev, Mar, Abr, Mai, Jun, Jul, Ago, Set, Out, Nov, Dez")
    jk = input("--- Qual mês deseja ver o extrato? ").capitalize()
    if jk not in meses:
        print("--- Mês inválido. Voltando ao menu principal.")
        input("--- Pressione Enter para voltar: ")
        return
    total_rec = 0

    for dados in rec.values():
        if dados["mes"] == jk:
            total_rec += dados["valor"]
    total_desp = 0

    for categoria in desp.values():
        for gasto in categoria.values():
            if gasto["mes"] == jk and gasto["status"] == "pendente":
                total_desp += gasto["fatura"]
    saldo = total_rec

    for categoria in desp.values():
        for gasto in categoria.values():
            if gasto["mes"] == jk and gasto["status"] == "pago":
                saldo -= gasto["fatura"]
    saldo_final = saldo - total_desp
    print("--- Extrato do mês")
    print("-" * 15)
    print(f"--- Receitas: R$ {total_rec:.2f}")
    print(f"--- Saldo atual: R$ {saldo:.2f}")
    print(f"--- Pendências: R$ {total_desp:.2f}")
    print(f"--- Saldo após quitar tudo: R$ {saldo_final:.2f}")
    nt = input("--- Deseja ver o saldo detalhado? (S/N) ")
    if (nt == "s") or (nt == "S"):
        print("--- Saldo detalhado")
        receitas_mes = 0
        despesas_pagas = 0
        despesas_pendentes = 0

        for dados in rec.values():
            if dados["mes"] == jk:
                receitas_mes += dados["valor"]

        for categoria in desp.values():
            for gasto in categoria.values():
                if gasto["mes"] == jk:
                    if gasto["status"] == "pago":
                        despesas_pagas += gasto["fatura"]
                    else:
                        despesas_pendentes += gasto["fatura"]

        saldo_atual = receitas_mes - despesas_pagas
        saldo_final = saldo_atual - despesas_pendentes
        print("-" * 40)
        print(f"--- Receitas:             R$ {receitas_mes:.2f}")
        print(f"--- Despesas pagas:       R$ {despesas_pagas:.2f}")
        print(f"--- Despesas pendentes:   R$ {despesas_pendentes:.2f}")
        print(f"--- Saldo atual:          R$ {saldo_atual:.2f}")
        print(f"--- Saldo após quitar:    R$ {saldo_final:.2f}")
        print("-" * 40)
        input("--- Pressione Enter para voltar: ")
    else:
        print("--- Voltando")
        input("--- Pressione Enter para voltar: ")
