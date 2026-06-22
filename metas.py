def menu_metas(metas, rec, meses, agora):
        import os
        mt = ''
        while mt != '0':
            print('''
---------------
--- Metas
--- 1 = Definir meta
--- 2 = Adicionar valor a meta
--- 3 = Ver metas
--- 4 = Remover meta
--- 0 = Voltar
---------------
            ''')
            mt = input('--- Opção: ')
            if mt == '1':
                m = input('--- Definir meta: ')
                if m in metas:
                    print('--- Meta já existe. Voltando.')
                    input('--- Pressione Enter para voltar: ')
                    continue
                total = float(input('--- Digite o valor total da meta:  '))
                if total <= 0:
                    print('--- Valor inválido. Voltando.')
                    input('--- Pressione Enter para voltar: ')
                    continue
                metas[m]= {'nome': m, 'total': total, 'valor': 0.0, 'estado': True}
                print('--- Meta definida')
            elif mt == '2':
                print('--- Adicionar valor a meta')
                print('-'*15)
                for nome, dados in metas.items():
                    print(f"--- Nome: {nome}")
                    print(f"--- Total: {dados['total']}")
                    print(f"--- Valor atual: {dados['valor']}")
                    print(f"--- Estado: {'Ativa' if  dados['estado'] else 'Inativa'}")
                    print('-'*15)
                a = input('--- Qual meta adicionar o valor: ')
                if a in metas:
                    a2= float(input('--- Digite o valor a ser adicionado:  '))
                    if a2 <= 0:
                        print('--- Valor inválido. Voltando.')
                        input('--- Pressione Enter para voltar: ')
                        continue
                    if metas[a]['valor'] + a2 >= metas[a]['total']:
                        metas[a]['valor'] = metas[a]['total']
                        print('--- Valor adicionado ultrapassa o total da meta. Meta atingida.')
                        print('--- Meta', a, 'atingida!')
                        print(f'--- Objetivo: {metas[a]["total"]}')
                        print(f'--- Valor atual: {metas[a]["valor"]}')
                        a3 = input('--- Deseja sacar o dinheiro? (S/N)')
                        if a3 == 's' or a3 == 'S':
                            rec[f'Meta_{a}'] = {'valor': metas[a]['valor'], 'mes': meses[agora.month-1]}
                            metas[a]['estado'] = False
                            print(f'--- Meta {a} desativada')
                            print(f'--- Dinheiro da meta {a} adicionado às receitas como Meta_{a}')
                        input('--- Pressione Enter para voltar: ')
                    else:
                        metas[a]['valor'] += a2
                        print('--- Valor adicionado a meta')
                        print(f'--- Meta: {a}')
                        print(f'--- Objetivo: {metas[a]["total"]}')
                        print(f'--- Valor atual: {metas[a]["valor"]}')
                        input('--- Pressione Enter para voltar: ')
                else:
                    print('--- Meta não encontrada')
                    input('--- Pressione Enter para voltar: ')
            elif mt == '3':
                print('--- Ver metas')
                print('-'*15)
                for nome, dados in metas.items():
                    if dados['estado']:
                        print(f"--- Nome: {nome}")
                        print(f"--- Total: {dados['total']}")
                        print(f"--- Valor atual: {dados['valor']}")
                        print(f"--- Estado: {'Ativa' if dados['estado'] else 'Inativa'}")
                        print('-'*15)
                b = input('--- Deseja ver as metas inativas? (S/N) ')
                if (b == 's') or (b == 'S'):
                            for nome, dados in metas.items():
                                if not dados['estado']:
                                    print(f"--- Nome: {nome}")
                                    print(f"--- Total: {dados['total']}")
                                    print(f"--- Valor atual: {dados['valor']}")
                                    print(f"--- Estado: {'Ativa' if dados['estado'] else 'Inativa'}")
                                    print('-'*15)
                input('--- Pressione Enter para voltar: ')
            elif mt == '4':
                print('--- Desativar meta')
                j = input('--- Qual meta desativar: ')
                if j in metas:
                    print(f'--- Meta {j} encontrada')
                    print(f'--- Objetivo da meta era {metas[j]["total"]} e o valor atual é {metas[j]["valor"]}')
                    j1 = input('--- Tem certeza? ')
                    if (j1 == 's') or (j1 == 'S'):
                        print(f'--- Meta {j} desativada')
                        rec[f'Meta_{j}'] = {'valor': metas[j]['valor'], 'mes': meses[agora.month-1]}
                        print(f'--- Dinheiro da meta {j} adicionado às receitas como Meta_{j}')
                        metas[j]['estado'] = False
                        input('--- Pressione Enter para voltar: ')
                    else:
                        print('--- Voltando.')
                        input('--- Pressione Enter para voltar: ')
                else:
                    print('--- Meta não encontrada.')
                    print('--- Voltando.')
                    input('--- Pressione Enter para voltar: ')
            elif mt == '0':
                print('--- Voltando')
                input('--- Pressione Enter para voltar: ')