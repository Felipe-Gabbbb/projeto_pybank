def menu_resumo(rec, desp):
        print('--- Resumo financeiro')
        total_rec = 0
        for dados in rec.values():
            total_rec += dados['valor']
        total_desp = 0
        for categoria in desp.values():
                for gasto in categoria.values():
                        if gasto['status'] == 'pendente':
                                total_desp += gasto['fatura']
        print('--- Situação financeira')
        print(f'--- Receitas: R$ {total_rec:.2f}')
        print(f'--- Contas pendentes: R$ {total_desp:.2f}')
        print(f'--- Valor disponível após quitar as pendências: R$ {total_rec - total_desp:.2f}')
        input('--- Pressione Enter para voltar: ')
