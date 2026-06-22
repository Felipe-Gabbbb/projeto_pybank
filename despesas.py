def menu_despesas(desp, meses, agora):
    mt = ''
    while mt != '0':
                print('''
---------------
--- Adicionar despesas
--- 1 = Contas e Cartões
--- 2 = Gastos variados
--- 0 = voltar
---------------
        ''')
                mt = input('--- Opção: ')
                if mt == '1':
                        gt = ''
                        while gt!= '0':
                                print('''
---------------
--- Contas
--- 1 = Cadastrar Conta/Cartão
--- 2 = Atualizar Conta/Cartão
--- 3 = Ver Contas e Cartões
--- 4 = Deletar Conta/Cartão
--- 5 = Realizar pagamentos                      
--- 0 = Voltar
---------------
         ''')
                                gt = input('--- Opção')
                                if gt =='1':
                                    print('-'*15)
                                    m = input('--- Cadastrar conta ou cartão? (1- Conta/2- Cartão')
                                    if m == '1':
                                        print('--- Cadastrar conta')           
                                        c = input('--- Definir nome da conta: ')
                                        if c in desp['contas']:
                                            print('--- Conta já existe. Voltando.')
                                            input('--- Pressione Enter para voltar: ')
                                            continue
                                        fatura = float(input('digite o valor total da fatura:  '))
                                        if fatura <= 0:
                                            print('--- Valor inválido. Voltando.')
                                            input('--- Pressione Enter para voltar: ')
                                            continue
                                        desp['contas'][c]= {
                                            'nome': c, 
                                            'fatura': fatura, 
                                            'status': 'pendente', 
                                            'mes': meses[agora.month-1]}
                                        print('--- Conta definida')
                                        input('--- Pressione Enter para voltar: ')
                                    elif m == '2':
                                        print('--- Cadastrar cartão')           
                                        c = input('--- Definir nome do cartão: ')
                                        if c in desp['cartões']:
                                            print('--- Cartão já existe. Voltando.')
                                            input('--- Pressione Enter para voltar: ')
                                            continue
                                        fatura = float(input('digite o valor total da fatura:  '))
                                        if fatura <= 0:
                                            print('--- Valor inválido. Voltando.')
                                            input('--- Pressione Enter para voltar: ')
                                            continue
                                        desp['cartões'][c]= {
                                            'nome': c, 
                                            'fatura': fatura, 
                                            'status': 'pendente', 
                                            'mes': meses[agora.month-1]}
                                        print('--- Cartão definido')
                                        input('--- Pressione Enter para voltar: ')
                                    else:
                                        print('digite uma opção válida')
                                        input('--- Pressione Enter para voltar: ')
                                elif gt == '2':
                                    print('--- Atualizar conta ou cartão')
                                    print('-'*15)
                                    for categoria, itens in desp.items():
                                        print(f"--- Categoria: {categoria}")
                                        print('-'*15)
                                        for nome, dados in itens.items():
                                            print(f"--- Nome: {nome}")
                                            print(f"--- Fatura: {dados['fatura']}")
                                            print(f"--- Status: {dados['status']}")
                                            print(f"--- Mês: {dados['mes']}")
                                            print('-'*15)
                                    a = input('--- Qual conta ou cartão atualizar: ')
                                    if a in desp['contas']:
                                        a2 = float(input('--- Digite o novo valor da fatura:  '))
                                        if a2 <= 0:
                                            print('--- Valor inválido. Voltando.')
                                            input('--- Pressione Enter para voltar: ')
                                            continue
                                        desp['contas'][a]['fatura'] = a2
                                        print('--- Conta atualizada')
                                        input('--- Pressione Enter para voltar: ')
                                    elif a in desp['cartões']:
                                        a2 = float(input('--- Digite o novo valor da fatura:  '))
                                        if a2 <= 0:
                                            print('--- Valor inválido. Voltando.')
                                            input('--- Pressione Enter para voltar: ')
                                            continue
                                        desp['cartões'][a]['fatura'] = a2
                                        print('--- Cartão atualizado')
                                        input('--- Pressione Enter para voltar: ')
                                    else:
                                        print('--- Conta ou cartão não encontrado')
                                        input('--- Pressione Enter para voltar: ')
                                elif gt == '3':
                                    print('--- Ver contas e cartões')
                                    print('-'*15)
                                    for categoria, itens in desp.items():
                                        print(f"--- Categoria: {categoria}")
                                        print('-'*15)
                                        for nome, dados in itens.items():
                                            print(f"--- Nome: {nome}")
                                            print(f"--- Fatura: {dados['fatura']}")
                                            print(f"--- Status: {dados['status']}")
                                            print(f"--- Mês: {dados['mes']}")
                                            print('-'*15)
                                    input('--- Pressione Enter para voltar: ')
                                elif gt == '4':
                                    print('--- Deletar conta ou cartão')
                                    print('-'*15)
                                    for categoria, itens in desp.items():
                                        print(f"--- Categoria: {categoria}")
                                        for nome, dados in itens.items():
                                            print(f"--- Nome: {nome}")
                                            print(f"--- Fatura: {dados['fatura']}")
                                            print(f"--- Status: {dados['status']}")
                                            print(f"--- Mês: {dados['mes']}")
                                            print('-'*15)
                                    d = input('--- Qual conta ou cartão deletar: ')
                                    if d in desp['contas']:
                                        print(desp['contas'][d])
                                        d1 = input('--- Tem certeza? (S/N) ')
                                        if (d1 == 's') or (d1 == 'S'):
                                            del desp['contas'][d]
                                            print(f'--- Conta {d} deletada')
                                        else:
                                            print('--- Voltando.')
                                            input('--- Pressione Enter para voltar: ')
                                    elif d in desp['cartões']:
                                        print(desp['cartões'][d])
                                        d1 = input('--- Tem certeza? (S/N) ')
                                        if (d1 == 's') or (d1 == 'S'):
                                            del desp['cartões'][d]
                                            print(f'--- Cartão {d} deletado')
                                            input('--- Pressione Enter para voltar: ')
                                        else:
                                            print('--- Voltando.')
                                            input('--- Pressione Enter para voltar: ')
                                    else:
                                        print('--- Conta ou cartão não encontrado.')
                                        input('--- Pressione Enter para voltar: ')
                                elif gt == '5':
                                    print('--- Realizar pagamento')
                                    print('-'*15)
                                    for categoria, itens in desp.items():
                                        print(f"--- Categoria: {categoria}")
                                        for nome, dados in itens.items():
                                            print(f"--- Nome: {nome}")
                                            print(f"--- Fatura: {dados['fatura']}")
                                            print(f"--- Status: {dados['status']}")
                                            print(f"--- Mês: {dados['mes']}")
                                            print('-'*15)
                                    p = input('--- Qual conta ou cartão deseja pagar: ')
                                    if p in desp['contas']:
                                        if desp['contas'][p]['status'] == 'pago':
                                            print('--- Conta já está paga. Voltando.')
                                            input('--- Pressione Enter para voltar: ')
                                            continue
                                        desp['contas'][p]['status'] = 'pago'
                                        print(f'--- Conta {p} paga')
                                        input('--- Pressione Enter para voltar: ')
                                    elif p in desp['cartões']:
                                        if desp['cartões'][p]['status'] == 'pago':
                                            print('--- Cartão já está pago. Voltando.')
                                            input('--- Pressione Enter para voltar: ')
                                            continue
                                        desp['cartões'][p]['status'] = 'pago'
                                        print(f'--- Cartão {p} pago')
                                        input('--- Pressione Enter para voltar: ')
                                    else:
                                        print('--- Conta ou cartão não encontrado.')
                                        input('--- Pressione Enter para voltar: ')
                                elif gt == '0':
                                    print('--- Voltando')
                                    input('--- Pressione Enter para voltar: ')
                elif mt == '2':
                        bt = ''
                        while bt != '0':
                            print('''
---------------
--- Gastos Variados
--- 1 = Cadastrar Gasto
--- 2 = Ver Gastos do mês
--- 3 = Atualizar gasto
--- 4 = Deletar gasto
--- 5 = Realizar pagamento
--- 0 = Voltar
---------------
                ''')
                            bt = input('--- Opção: ')
                            if bt == '1':
                                print('--- Cadastrar gasto variado')
                                print('-'*15)
                                c = input('--- Definir nome do gasto: ')
                                if c in desp['outros']:
                                    print('--- Gasto já existe. Voltando.')
                                    input('--- Pressione Enter para voltar: ')
                                    continue
                                fatura = float(input('--- Digite o valor total do gasto:  '))
                                if fatura <= 0:
                                    print('--- Valor inválido. Voltando.')
                                    input('--- Pressione Enter para voltar: ')
                                    continue
                                desp['outros'][c]= {
                                    'nome': c, 
                                    'fatura': fatura, 
                                    'status': 'pendente', 
                                    'mes': meses[agora.month-1]
                                }
                                print('--- Gasto definido')
                                input('--- Pressione Enter para voltar: ')
                            elif bt == '2':
                                print('--- Ver gastos variados do mês')
                                print('-'*15)
                                for nome, dados in desp['outros'].items():
                                    print(f"--- Nome: {nome}")
                                    print(f"--- Fatura: {dados['fatura']}")
                                    print(f"--- Status: {dados['status']}")
                                    print(f"--- Mês: {dados['mes']}")
                                    print('-'*15)
                                input('--- Pressione Enter para voltar: ')
                            elif bt == '3':
                                print('--- Atualizar gasto variado')
                                print('-'*15)
                                for nome, dados in desp['outros'].items():
                                    print(f"--- Nome: {nome}")
                                    print(f"--- Fatura: {dados['fatura']}")
                                    print(f"--- Status: {dados['status']}")
                                    print(f"--- Mês: {dados['mes']}")
                                    print('-'*15)
                                a = input('--- Qual gasto atualizar: ')
                                if a in desp['outros']:
                                    a2 = float(input('--- Digite o novo valor do gasto:  '))
                                    if a2 <= 0:
                                        print('--- Valor inválido. Voltando.')
                                        input('--- Pressione Enter para voltar: ')
                                        continue
                                    desp['outros'][a]['fatura'] = a2
                                    print('--- Gasto atualizado')
                                    input('--- Pressione Enter para voltar: ')
                                else:
                                    print('--- Gasto não encontrado')
                                    input('--- Pressione Enter para voltar: ')
                            elif bt == '4':
                                print('--- Deletar gasto variado')
                                print('-'*15)
                                for nome, dados in desp['outros'].items():
                                    print(f"--- Nome: {nome}")
                                    print(f"--- Fatura: {dados['fatura']}")
                                    print(f"--- Status: {dados['status']}")
                                    print(f"--- Mês: {dados['mes']}")
                                    print('-'*15)
                                d = input('--- Qual gasto deletar: ')
                                if d in desp['outros']:
                                    print(desp['outros'][d])
                                    d1 = input('--- Tem certeza? (S/N) ')
                                    if (d1 == 's') or (d1 == 'S'):
                                        del desp['outros'][d]
                                        print(f'--- Gasto {d} deletado')
                                    else:
                                        print('--- Voltando.')
                                        input('--- Pressione Enter para voltar: ')
                                else:
                                    print('--- Gasto não encontrado.')
                                    input('--- Pressione Enter para voltar: ')
                            elif bt == '5':
                                print('--- Realizar pagamento de gasto variado')
                                print('-'*15)
                                for nome, dados in desp['outros'].items():
                                    print(f"--- Nome: {nome}")
                                    print(f"--- Fatura: {dados['fatura']}")
                                    print(f"--- Status: {dados['status']}")
                                    print(f"--- Mês: {dados['mes']}")
                                    print('-'*15)
                                p = input('--- Qual gasto deseja pagar: ')
                                if p in desp['outros']:
                                        if desp['outros'][p]['status'] == 'pago':
                                                print('--- Gasto já está pago. Voltando.')
                                                input('--- Pressione Enter para voltar: ')
                                                continue
                                        desp['outros'][p]['status'] = 'pago'
                                        print(f'--- Gasto {p} pago')
                                        input('--- Pressione Enter para voltar: ')
                                else:
                                    print('--- Gasto não encontrado.')
                                    input('--- Pressione Enter para voltar: ')
                            elif bt == '0':
                                print('--- Voltando')
                                input('--- Pressione Enter para voltar: ')