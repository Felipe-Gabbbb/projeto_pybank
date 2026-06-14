import os
from datetime import datetime
import pickle
os.system('cls')
agora = datetime.now()
data_formatada = agora.strftime("%d/%m/%Y %H:%M")

print(data_formatada)
meses = 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'
rec = {
'salario': {'valor' : 3000, 'mes': meses[agora.month-1]},
 'freelance': {'valor': 500, 'mes': meses[agora.month-1]},
   'investimentos': {'valor': 200, 'mes': meses[agora.month-1]}
}
desp = { 
'cartões' :{ 
  'caixa' : {'nome': 'caixa', 'fatura': 1000,  'mes': meses[agora.month-1]},
  'bradesco' : {'nome' : 'bradesco', 'fatura': 500, 'mes': meses[agora.month-1]},
         },
'contas' :{
  'luz': {'nome':'luz','fatura':150, 'mes': meses[agora.month-1]},
  'agua': {'nome':'agua','fatura':100, 'mes': meses[agora.month-1]},
},
'outros' : {
  'shoppe':{'nome':'shoppe','fatura':236, 'mes': meses[agora.month-1]},
  'amazon':{'nome':'amazon','fatura':120, 'mes': meses[agora.month-1]},
}
}
metas = {
  'carro': {'nome' :'carro','total': 40000, 'valor' : 36500}, 
  'moto' : {'nome' :'moto', 'total':15000, 'valor': 8000},

}
try:
    arqRec = open('rec.pkl', 'rb')
    rec = pickle.load(arqRec)
    arqRec.close()
    arqDesp = open('desp.pkl', 'rb')
    desp = pickle.load(arqDesp)
    arqDesp.close()
    arqMetas = open('metas.pkl', 'rb')
    metas = pickle.load(arqMetas)
    arqMetas.close()
except:
    print('--- Nenhum arquivo de dados encontrado. Iniciando com dados vazios.')
    arqRec = open('rec.pkl', 'wb')
    arqDesp = open('desp.pkl', 'wb')
    arqMetas = open('metas.pkl', 'wb')
    arqRec.close()
    arqDesp.close()
    arqMetas.close()
    

print('sig bank')
r = ''
while r!= '0':  
  mt = ''
  gt = ''
  bt = ''
  os.system('cls' if os.name=='nt' else 'clear')
  print(f'''
---------------
--- sigbank.0
--- Menu Principal
--- Data = {data_formatada}
--- 1 = Receitas
--- 2 = Despesas
--- 3 = Saldo
--- 4 = Metas
--- 5 = Extrato
--- 0 = Sair
---------------
  ''')
  r =input('opção: ')
  if r == '1':
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
    while mt != '0':
      if mt == '1':
        print('--- Adicionar receita')
        print('-'*15)
        c = input('--- Definir nome da receita: ')
        valor = int(input('digite o valor da receita:  '))
        rec[c]= {'valor': valor, 'mes': meses[agora.month-1]}
        print('--- Receita definida')
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
          a2 = int(input('--- Digite o novo valor da receita:  '))
          rec[a]['valor'] = a2
          print('--- Receita atualizada')
        else:
          print('--- Receita não encontrada')
      elif mt == '3':
        print('--- Ver receitas')
        print('-'*15)
        for nome, dados in rec.items():
          print(f"--- Nome: {nome}")
          print(f"--- Valor: {dados['valor']}")
          print(f"--- Mês: {dados['mes']}")
          print('-'*15)
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
          else:
            print('--- Voltando.')
        else:
          print('--- Receita não encontrada.')
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
            while gt!= '0':
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
                gt = input('--- Opção')
                if gt =='1':
                  print('-'*15)
                  m = input('--- Cadastrar conta ou cartão? (1- Conta/2- Cartão')
                  if m == 1:
                    print('--- Cadastrar conta')           
                    c = input('--- Definir nome da conta: ')
                    fatura = int(input('digite o valor total da fatura:  '))
                    desp['contas']= {c, fatura, meses[agora.month-1]}
                    print('--- Conta definida')
                  elif m == 2:
                    
                    print('--- Cadastrar cartão')           
                    c = input('--- Definir nome do cartão: ')
                    fatura = int(input('digite o valor total da fatura:  '))
                    desp['cartões']= {c, fatura, meses[agora.month-1]}
                    print('--- Cartão definido')
                  else:
                    print('digite uma opção válida')
                elif gt == '2':
                  print('--- Atualizar conta ou cartão')
                  print('-'*15)
                  for categoria, itens in desp.items():
                    print(f"--- Categoria: {categoria}")
                    print('-'*15)
                    for nome, dados in itens.items():
                      print(f"--- Nome: {nome}")
                      print(f"--- Fatura: {dados['fatura']}")
                      print(f"--- Mês: {dados['mes']}")
                      print('-'*15)
                  a = input('--- Qual conta ou cartão atualizar: ')
                  if a in desp['contas']:
                    a2 = int(input('--- Digite o novo valor da fatura:  '))
                    desp['contas'][a]['fatura'] = a2
                    print('--- Conta atualizada')
                  elif a in desp['cartões']:
                    a2 = int(input('--- Digite o novo valor da fatura:  '))
                    desp['cartões'][a]['fatura'] = a2
                    print('--- Cartão atualizado')
                  else:
                    print('--- Conta ou cartão não encontrado')
                elif gt == '3':
                  print('--- Ver contas e cartões')
                  print('-'*15)
                  for categoria, itens in desp.items():
                    print(f"--- Categoria: {categoria}")
                    print('-'*15)
                    for nome, dados in itens.items():
                      print(f"--- Nome: {nome}")
                      print(f"--- Fatura: {dados['fatura']}")
                      print(f"--- Mês: {dados['mes']}")
                      print('-'*15)
                elif gt == '4':
                  print('--- Deletar conta ou cartão')
                  print('-'*15)
                  for categoria, itens in desp.items():
                    print(f"--- Categoria: {categoria}")
                    for nome, dados in itens.items():
                      print(f"--- Nome: {nome}")
                      print(f"--- Fatura: {dados['fatura']}")
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
                  elif d in desp['cartões']:
                    print(desp['cartões'][d])
                    d1 = input('--- Tem certeza? (S/N) ')
                    if (d1 == 's') or (d1 == 'S'):
                      del desp['cartões'][d]
                      print(f'--- Cartão {d} deletado')
                    else:
                      print('--- Voltando.')
                  else:
                    print('--- Conta ou cartão não encontrado.')
                elif gt == '0':
                  print('--- Voltando')
        elif mt == '2':
            while bt != '0':
              print('''
---------------
--- Gastos Variados
--- 1 = Cadastrar Gasto
--- 2 = Ver Gastos do mês
--- 3 = Atualizar gasto
--- 4 = Deletar gasto
--- 0 = Voltar
---------------
        ''')
              bt = input('--- Opção: ')
              if bt == '1':
                print('--- Cadastrar gasto variado')
                print('-'*15)
                c = input('--- Definir nome do gasto: ')
                fatura = int(input('digite o valor total do gasto:  '))
                desp['outros'][c]= {'nome': c, 'fatura': fatura, 'mes': meses[agora.month-1]}
                print('--- Gasto definido')
              elif bt == '2':
                print('--- Ver gastos variados do mês')
                print('-'*15)
                for nome, dados in desp['outros'].items():
                  print(f"--- Nome: {nome}")
                  print(f"--- Fatura: {dados['fatura']}")
                  print(f"--- Mês: {dados['mes']}")
                  print('-'*15)
              elif bt == '3':
                print('--- Atualizar gasto variado')
                print('-'*15)
                for nome, dados in desp['outros'].items():
                  print(f"--- Nome: {nome}")
                  print(f"--- Fatura: {dados['fatura']}")
                  print(f"--- Mês: {dados['mes']}")
                  print('-'*15)
                a = input('--- Qual gasto atualizar: ')
                if a in desp['outros']:
                  a2 = int(input('--- Digite o novo valor do gasto:  '))
                  desp['outros'][a]['fatura'] = a2
                  print('--- Gasto atualizado')
                else:
                  print('--- Gasto não encontrado')
              elif bt == '4':
                print('--- Deletar gasto variado')
                print('-'*15)
                for nome, dados in desp['outros'].items():
                  print(f"--- Nome: {nome}")
                  print(f"--- Fatura: {dados['fatura']}")
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
                else:
                  print('--- Gasto não encontrado.')
  elif r == '3':
    print('--- Saldo do mês')
    total_rec = sum(dados['valor'] for dados in rec.values())
    total_desp = sum(dados['fatura'] for dados in desp['outros'].values())
    print(f'--- Receita: {total_rec}')
    print(f'--- Despesas: {total_desp}')
    print(f'--- Saldo: {total_rec - total_desp}')
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
        total = int(input('digite o valor total da meta:  '))
        metas[m]= {'nome': m, 'total': total, 'valor': 0}
        print('meta definida')
      elif mt == '2':
        print('--- Adicionar valor a meta')
        print('-'*15)
        for nome, dados in metas.items():
          print(f"--- Nome: {nome}")
          print(f"--- Total: {dados['total']}")
          print(f"--- Valor atual: {dados['valor']}")
          print('-'*15)
        a = input('qual meta adicionar o valor: ')
        if a in metas:
          a2= int(input('digite o valor a ser adicionado:  '))
          metas[a]['valor'] +=a2
          print('valor adicionado')
          print(f'meta = {metas[a]}')
          if (metas[a]['valor']) >= (metas[a]['total']):
            print('meta atingida')
            a3 = input('--- Deseja sacar o dinheiro? (S/N)')
            if a3 == 's' or a3 == 'S':
              rec.append(metas[a]['valor'])
              del metas[a]
        else:
          print('meta não encontrada')
      elif mt == '3':
        print('ver metas')
        print('-'*15)
        for nome, dados in metas.items():
          print(f"--- Nome: {nome}")
          print(f"--- Total: {dados['total']}")
          print(f"--- Valor atual: {dados['valor']}")
          print('-'*15)
      elif mt == '4':
        print('--- Remover meta')
        j = input('--- Qual meta remover: ')
        if j in metas:
          print(metas[j])
          j1 = input('--- Tem ceteza? ')
          if (j1 == 's') or (j1 == 'S'):
            del metas[j]
            print(f'--- Meta {j} removida')
          else:
            print('--- Voltando.')
        else:
          print('--- Cliente não encontrado.')
          print('--- Voltando.')
      elif mt == '0':
        print('--- Voltando')
  elif r == '5':
      print('--- Extrato do mês')
      print('--- Meses: Jan, Fev, Mar, Abr, Mai, Jun, Jul, Ago, Set, Out, Nov, Dez')
      jk = input('--- Qual mês deseja ver o extrato? ').capitalize()
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
            print()
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
              for nome, dados in itens.items():
                  if dados['mes'] == jk:
                    print(f"--- Categoria: {categoria}")
                    print(f"--- Nome: {nome}")
                    print(f"--- Fatura: {dados['fatura']}")
                    print(f"--- Mês: {dados['mes']}")
                    print('-'*15)
            print('--- Voltando')
            lok = input('--- Pressione Enter para voltar: ')
      else:
        print('--- Voltando')
        lok = input('--- Pressione Enter para voltar: ')
  elif r == '0':
    print('--- Saindo do programa')
  else:
    print('--- Opção inválida')
arqRec = open('rec.pkl', 'wb')
pickle.dump(rec, arqRec)
arqRec.close()
arqDesp = open('desp.pkl', 'wb')
pickle.dump(desp, arqDesp)
arqDesp.close()
arqMetas = open('metas.pkl', 'wb')
pickle.dump(metas, arqMetas)
arqMetas.close()
print('--- Dados salvos com sucesso')
print('--- Fim do programa')