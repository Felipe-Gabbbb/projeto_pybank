from receitas import *
from despesas import *

def menu_resumo(rec, desp):
    print("--- Resumo financeiro")
    print('-' * 40)

    total_rec = 0
    for dados in rec.values():
        total_rec += dados['valor']

    despesas_pagas = 0
    despesas_pendentes = 0

    for categoria in desp.values():
        for gasto in categoria.values():
            if gasto['status'] == 'pago':
                despesas_pagas += gasto['fatura']
            else:
                despesas_pendentes += gasto['fatura']

    saldo_atual = total_rec - despesas_pagas
    saldo_final = saldo_atual - despesas_pendentes

    print(f'Receitas:                 R$ {total_rec:.2f}')
    print(f'Despesas pagas:          R$ {despesas_pagas:.2f}')
    print(f'Saldo atual:             R$ {saldo_atual:.2f}')
    print('-' * 40)
    print(f'Despesas pendentes:      R$ {despesas_pendentes:.2f}')
    print(f'Saldo após quitar tudo:  R$ {saldo_final:.2f}')
    print('-' * 40)

    input('Pressione Enter para voltar...')
