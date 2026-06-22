def menu_extrato(rec, desp, meses):
            
            print('--- Extrato do mês')
            print('--- Meses: Jan, Fev, Mar, Abr, Mai, Jun, Jul, Ago, Set, Out, Nov, Dez')
            jk = input('--- Qual mês deseja ver o extrato? ').capitalize()
            if jk not in meses:
                    print('--- Mês inválido. Voltando ao menu principal.')
                    input('--- Pressione Enter para voltar: ')
                    continue
            total_rec = 0
            for dados in rec.values():
                    if dados['mes'] == jk:
                            total_rec += dados['valor']
            total_desp = 0
            for categoria in desp.values():
                    for gasto in categoria.values():
                            if gasto['mes'] == jk:
                                    total_desp += gasto['fatura']
            print('-' * 15)
            print(f'--- Extrato do mês de {jk}')
            print(f'--- Receita: R$ {total_rec}')
            print(f'--- Despesas: R$ {total_desp}')
            print(f'--- Saldo: R$ {total_rec - total_desp}')
            nt = input('--- Deseja ver o saldo detalhado? (S/N) ')
            if (nt == 's') or (nt == 'S'):
                        print('--- Saldo detalhado')
                        print('-'*15)
                        print('--- Receitas ')
                        print('-'*15)
                        print()
                        for nome, dados in rec.items():
                                if dados['mes'] == jk:
                                    print(f"--- Nome: {nome}")
                                    print(f"--- Valor: {dados['valor']}")
                                    print(f"--- Mês: {dados['mes']}")
                                    print('-'*15)
                        print('--- Despesas ')
                        print('-'*15)
                        print()
                        for categoria, itens in desp.items():
                            print(f"--- Categoria: {categoria}")
                            for nome, dados in itens.items():
                                    if dados['mes'] == jk:
                                        print(f"--- Nome: {nome}")
                                        print(f"--- Fatura: {dados['fatura']}")
                                        print(f"--- Status: {dados['status']}")
                                        print(f"--- Mês: {dados['mes']}")
                                        print('-'*15)
                        print('--- Voltando')
                        input('--- Pressione Enter para voltar: ')
            else:
                print('--- Voltando')
                input('--- Pressione Enter para voltar: ')