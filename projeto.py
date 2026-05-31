import os
from datetime import datetime
os.system('cls')
agora = datetime.now()
data_formatada = agora.strftime("%d/%m/%Y %H:%M")

print(data_formatada)
meses = 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'
rec = [30,400,23,41]
desp = [50,42,4,120]
metas = ['carro', 40000, [36500]]
print('sig bank')

r = ''
while r!= '0':  
  mt = ''
  bt = ''
  os.system('cls')
  print(f'''
  ---------------
  --- sigbank.0
  --- Menu Principal
  --- Data = {data_formatada}
  --- 1 = Adicionar Receitas
  --- 2 = Adicionar Despesas
  --- 3 = Saldo
  --- 4 = Metas
  --- 5 = Extrato
  --- 0 = Sair
  ---------------
  ''')
  r =input('opção: ')
  if r == '1':
    print('adicionar receitas')
    rec.append(int(input('valor: ')))


    
  elif r == '2':
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
            while != 0:
                print('''
        ---------------
        --- Contas
        --- 1 = Cadastrar Conta/Cartão
        --- 2 = Atualizar Conta/Cartão
        --- 3 = Ver Contas e Cartões
        --- 4 = Deletar Conta/Cartão
        --- 0 = Voltar
        ---------------
         ''')
        elif mt == '2':
            while bt != 0:
                print('''
        ---------------
        --- Gastos Variados
        --- 1 = Cadastrar Gasto
        --- 2 = Ver Gastos do mês
        --- 0 = Voltar
        ---------------
        ''')
  elif r == '3':
    print('saldo')
    print(sum(rec) - sum(desp))
  elif r == '4':
    while mt != '0':
      print('''
      ---------------
      --- metas
      --- 1 = definir meta
      --- 2 = adicionar valor a meta
      --- 3 = ver metas
      --- 4 = remover meta
      --- 0 = voltar
      ---------------
      ''')
      mt = input('opção: ')
      if mt == '1':
        m = input('definir meta: ')
        metas.append(m)
        total = int(input('digite o valor total da meta:  '))
        metas.append(total)
        metas.append([])
        print('meta definida')
      elif mt == '2':
        print('adicionar valor a meta')
        a = input('qual meta adicionar o valor: ')
        print(metas[0])
        if a in metas:
          b= int(input('digite o valor a ser adicionado:  '))
          metas[2].append(b)
          print('valor adicionado')
          print(f'meta = {metas[1]}, valor atual = {sum(metas[2])} ')
          if sum(metas[2]) >= metas[1]:
            print('meta atingida')
        else:
          print('meta não encontrada')
      elif mt == '3':
        print('ver metas')
        print(f'meta: {metas[0]}, valor total: {metas[1]}, valor atual: {sum(metas[2])}')
      elif mt == '4':
        print('remover meta')
        j = input('qual meta remover: ')
        if j in metas:
          metas.remove(j)
        print(f'meta {j} removida')
      elif mt == '0':
        print('voltar')
  elif r == '5':
    print('extrato do mês')
    print('receita',rec)
    print('despesas',desp)
  elif r == '0':
    print('sair')
  else:
    print('opção inválida')
print('fim do programa')
