
import os
def menu_receitas(rec, meses, agora):
        mt = ''
        while mt != '0':
                os.system('cls' if os.name=='nt' else 'clear')
                print('--- Receitas')
                print('-'*15)
                print(f'''
--- 1 Adicionar receita
--- 2 Atualizar receita
--- 3 Ver receitas
--- 4 Deletar receita
--- 0 Voltar          
                            ''')
                mt = input('--- Opção: ')
                if mt == '1':
                    print('--- Adicionar receita')
                    print('-'*15)
                    c = input('--- Definir nome da receita: ')
                    if c in rec:
                        print('--- Receita já existe. Voltando.')
                        input('--- Pressione Enter para voltar: ')
                        continue
                    valor = float(input('--- Digite o valor da receita:  '))
                    if valor <= 0:
                        print('--- Valor inválido. Voltando.')
                        input('--- Pressione Enter para voltar: ')
                        continue
                    rec[c]= {'valor': valor, 'mes': meses[agora.month-1]}
                    print('--- Receita definida')
                    input('--- Pressione Enter para voltar: ')
                elif mt == '2':
                    print('--- Atualizar receita')
                    print('-'*15)
                    for nome, dados in rec.items():
                        print(f"--- Nome: {nome}")
                        print(f"--- Valor: {dados['valor']}")
                        print(f"--- Mês: {dados['mes']}")
                        print('-'*15)
                    a = input('--- Qual receita atualizar: ')
                    if a in rec:
                        a2 = float(input('--- Digite o novo valor da receita:  '))
                        if a2 <= 0:
                            print('--- Valor inválido. Voltando.')
                            input('--- Pressione Enter para voltar: ')
                            continue
                        rec[a]['valor'] = a2
                        print('--- Receita atualizada')
                        input('--- Pressione Enter para voltar: ')
                    else:
                        print('--- Receita não encontrada')
                        input('--- Pressione Enter para voltar: ')
                elif mt == '3':
                    print('--- Ver receitas')
                    print('-'*15)
                    for nome, dados in rec.items():
                        print(f"--- Nome: {nome}")
                        print(f"--- Valor: {dados['valor']}")
                        print(f"--- Mês: {dados['mes']}")
                        print('-'*15)
                    input('--- Pressione Enter para voltar: ')
                elif mt == '4':
                    print('--- Deletar receita')
                    for nome, dados in rec.items():
                        print(f"--- Nome: {nome}")
                        print(f"--- Valor: {dados['valor']}")
                        print(f"--- Mês: {dados['mes']}")
                        print('-'*15)
                    d = input('--- Qual receita deletar: ')
                    if d in rec:
                        print(rec[d])
                        d1 = input('--- Tem certeza? (S/N) ')
                        if (d1 == 's') or (d1 == 'S'):
                            del rec[d]
                            print(f'--- Receita {d} deletada')
                            input('--- Pressione Enter para voltar: ')
                        else:
                            input('--- Pressione Enter para voltar: ')
                    else:
                        print('--- Receita não encontrada.')
                        input('--- Pressione Enter para voltar: ')