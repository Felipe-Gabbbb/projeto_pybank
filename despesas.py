def exibir_despesas(desp):
    print("-" * 70)
    print(f'{"Nome":<15}{"Fatura":<15}{"Status":<15}{"Mês":<10}')
    print("-" * 70)

    for categoria, itens in desp.items():
        if categoria == "outros":
            continue
        print(f"[{categoria.upper()}]")
        for chave, dados in itens.items():
                print(
                    f'{dados["nome"]:<15}R$ {dados["fatura"]:<12.2f}{dados["status"]:<15}{dados["mes"]:<10}'
                )

    print("-" * 70)
def exibir_gastos_variados(desp):
    print("-" * 60)
    print(f'{"Nome":<20}{"Fatura":<15}{"Status":<15}{"Mês":<10}')
    print("-" * 60)

    for chave, dados in desp["outros"].items():
        print(
            f'{dados["nome"]:<20}R$ {dados["fatura"]:<12.2f}{dados["status"]:<15}{dados["mes"]:<10}'
        )

    print("-" * 60)
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
                                            return
                                        fatura = float(input('digite o valor total da fatura:  '))
                                        if fatura <= 0:
                                            print('--- Valor inválido. Voltando.')
                                            input('--- Pressione Enter para voltar: ')
                                            return
                                        mes_ano = agora.strftime("%Y_%m")
                                        chave = f'{c}_{mes_ano}'
                                        desp['contas'][chave]= {
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
                                            return
                                        fatura = float(input('digite o valor total da fatura:  '))
                                        if fatura <= 0:
                                            print('--- Valor inválido. Voltando.')
                                            input('--- Pressione Enter para voltar: ')
                                            return
                                        mes_ano = agora.strftime("%Y_%m")
                                        chave = f'{c}_{mes_ano}'
                                        desp['cartões'][chave]= {
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
                                    exibir_despesas(desp)

                                    a = input('--- Digite o registro que deseja atualizar: ')

                                    if a in desp['contas']:
                                        valor = float(input('--- Novo valor da fatura: '))

                                        if valor <= 0:
                                            print('--- Valor inválido.')
                                        else:
                                            desp['contas'][a]['fatura'] = valor
                                            print('--- Conta atualizada.')

                                    elif a in desp['cartões']:
                                        valor = float(input('--- Novo valor da fatura: '))

                                        if valor <= 0:
                                            print('--- Valor inválido.')
                                        else:
                                            desp['cartões'][a]['fatura'] = valor
                                            print('--- Cartão atualizado.')

                                    else:
                                        print('--- Registro não encontrado.')
                                elif gt == '3':
                                    print('--- Ver contas e cartões')
                                    print('-'*15)
                                    exibir_despesas(desp)
                                    input('--- Pressione Enter para voltar: ')
                                elif gt == '4':
                                    print('--- Deletar conta ou cartão')
                                    print('-'*15)
                                    exibir_despesas(desp)

                                    d = input('--- Digite o registro que deseja excluir: ')

                                    if d in desp['contas']:

                                        confirma = input('Tem certeza? (S/N) ')

                                        if confirma.upper() == 'S':
                                            del desp['contas'][d]
                                            print('--- Conta removida.')

                                    elif d in desp['cartões']:

                                        confirma = input('Tem certeza? (S/N) ')

                                        if confirma.upper() == 'S':
                                            del desp['cartões'][d]
                                            print('--- Cartão removido.')

                                    else:
                                        print('--- Registro não encontrado.')
                                    input('--- Pressione Enter para voltar: ')
                                elif gt == '5':
                                    print('--- Realizar pagamento')
                                    print('-'*15)
                                    exibir_despesas(desp)

                                    p = input('--- Qual registro deseja pagar? ')

                                    if p in desp['contas']:

                                        if desp['contas'][p]['status'] == 'pago':
                                            print('--- Conta já paga.')
                                        else:
                                            desp['contas'][p]['status'] = 'pago'
                                            print('--- Conta paga.')

                                    elif p in desp['cartões']:

                                        if desp['cartões'][p]['status'] == 'pago':
                                            print('--- Cartão já pago.')
                                        else:
                                            desp['cartões'][p]['status'] = 'pago'
                                            print('--- Cartão pago.')

                                    else:
                                        print('--- Registro não encontrado.')
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
                                mes_ano = agora.strftime("%Y_%m")
                                chave = f'{c}_{mes_ano}'
                                if chave in desp['outros']:
                                    print('--- Gasto já existe. Voltando.')
                                    input('--- Pressione Enter para voltar: ')
                                    continue
                                fatura = float(input('--- Digite o valor total do gasto:  '))
                                if fatura <= 0:
                                    print('--- Valor inválido. Voltando.')
                                    input('--- Pressione Enter para voltar: ')
                                    continue
                                desp['outros'][chave]= {
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
                                exibir_gastos_variados(desp)
                                input('--- Pressione Enter para voltar: ')
                            elif bt == '3':
                                print('--- Atualizar gasto variado')
                                print('-'*15)
                                exibir_gastos_variados(desp)

                                a = input('Registro: ')

                                if a in desp['outros']:

                                    valor = float(input('Novo valor: '))

                                    if valor > 0:
                                        desp['outros'][a]['fatura'] = valor
                            elif bt == '4':
                                print('--- Deletar gasto variado')
                                print('-'*15)
                                exibir_gastos_variados(desp)

                                d = input('Registro: ')

                                if d in desp['outros']:
                                    del desp['outros'][d]
                                else:
                                    print('--- Registro não encontrado.')
                                input('--- Pressione Enter para voltar: ')
                            elif bt == '5':
                                print('--- Realizar pagamento de gasto variado')
                                print('-'*15)
                                exibir_gastos_variados(desp)

                                p = input('Registro: ')

                                if p in desp['outros']:
                                    desp['outros'][p]['status'] = 'pago'
                                else:
                                    print('--- Registro não encontrado.')
                                input('--- Pressione Enter para voltar: ')
                            elif bt == '0':
                                print('--- Voltando')
                                input('--- Pressione Enter para voltar: ')
