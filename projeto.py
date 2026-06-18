import os
from datetime import datetime
import pickle
agora = datetime.now()
data_formatada = agora.strftime("%d/%m/%Y %H:%M")
meses = 'Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'
rec = {
'salario': {'valor' : 3000.0, 'mes': meses[agora.month-1]},
 'freelance': {'valor': 500.90, 'mes': meses[agora.month-1]},
   'investimentos': {'valor': 200.10, 'mes': meses[agora.month-1]}
}
desp = { 
'cartões' :{ 
  'caixa' : {'nome': 'caixa', 'fatura': 1000.0, 'status' : 'pendente', 'mes': meses[agora.month-1]},
  'bradesco' : {'nome' : 'bradesco', 'fatura': 500.0, 'status' : 'pendente', 'mes': meses[agora.month-1]},
         },
'contas' :{
  'luz': {'nome':'luz','fatura':150.86, 'status' : 'pendente', 'mes': meses[agora.month-1]},
  'agua': {'nome':'agua','fatura':100.95, 'status' : 'pendente', 'mes': meses[agora.month-1]},
},
'outros' : {
  'shoppe':{'nome':'shoppe','fatura':236.50, 'status' : 'pendente', 'mes': meses[agora.month-1]},
  'amazon':{'nome':'amazon','fatura':120.25, 'status' : 'pendente', 'mes': meses[agora.month-1]},
}
}
metas = {
  'carro': {'nome' :'carro','total': 40000.0, 'valor' : 36500.50, 'estado' : True}, 
  'moto' : {'nome' :'moto', 'total':15000.0, 'valor': 8000.66, 'estado' : True},

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
except (FileNotFoundError, EOFError):
    print('--- Nenhum arquivo de dados encontrado. Iniciando com dados vazios.')
    arqRec = open('rec.pkl', 'wb')
    arqDesp = open('desp.pkl', 'wb')
    arqMetas = open('metas.pkl', 'wb')
    arqRec.close()
    arqDesp.close()
    arqMetas.close()
r = ''
while r!= '0':  
  os.system('cls' if os.name=='nt' else 'clear')
  print(f'''
---------------
--- sigbank.3
--- Menu Principal
--- Data = {data_formatada}
--- 1 = Receitas
--- 2 = Despesas
--- 3 = Resumo financeiro
--- 4 = Metas
--- 5 = Extrato
--- 0 = Sair
---------------
  ''')
  r =input('opção: ')
  if r == '1':
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
            mt = input('--- Opção: ')
            continue
          valor = float(input('--- Digite o valor da receita:  '))
          if valor <= 0:
            print('--- Valor inválido. Voltando.')
            mt = input('--- Opção: ')
            continue
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
            a2 = float(input('--- Digite o novo valor da receita:  '))
            if a2 <= 0:
              print('--- Valor inválido. Voltando.')
              continue
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
          w = input('--- Pressione Enter para voltar: ')
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
                      continue
                    fatura = float(input('digite o valor total da fatura:  '))
                    if fatura <= 0:
                      print('--- Valor inválido. Voltando.')
                      continue
                    desp['contas'][c]= {
                      'nome': c, 
                      'fatura': fatura, 
                      'status': 'pendente', 
                      'mes': meses[agora.month-1]}
                    print('--- Conta definida')
                  elif m == '2':
                    print('--- Cadastrar cartão')           
                    c = input('--- Definir nome do cartão: ')
                    if c in desp['cartões']:
                      print('--- Cartão já existe. Voltando.')
                      continue
                    fatura = float(input('digite o valor total da fatura:  '))
                    if fatura <= 0:
                      print('--- Valor inválido. Voltando.')
                      continue
                    desp['cartões'][c]= {
                      'nome': c, 
                      'fatura': fatura, 
                      'status': 'pendente', 
                      'mes': meses[agora.month-1]}
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
                      print(f"--- Status: {dados['status']}")
                      print(f"--- Mês: {dados['mes']}")
                      print('-'*15)
                  a = input('--- Qual conta ou cartão atualizar: ')
                  if a in desp['contas']:
                    a2 = float(input('--- Digite o novo valor da fatura:  '))
                    if a2 <= 0:
                      print('--- Valor inválido. Voltando.')
                      continue
                    desp['contas'][a]['fatura'] = a2
                    print('--- Conta atualizada')
                  elif a in desp['cartões']:
                    a2 = float(input('--- Digite o novo valor da fatura:  '))
                    if a2 <= 0:
                      print('--- Valor inválido. Voltando.')
                      continue
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
                      print(f"--- Status: {dados['status']}")
                      print(f"--- Mês: {dados['mes']}")
                      print('-'*15)
                  gt = input('--- Pressione Enter para voltar: ')
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
                      continue
                    desp['contas'][p]['status'] = 'pago'
                    print(f'--- Conta {p} paga')
                  elif p in desp['cartões']:
                    if desp['cartões'][p]['status'] == 'pago':
                      print('--- Cartão já está pago. Voltando.')
                      continue
                    desp['cartões'][p]['status'] = 'pago'
                    print(f'--- Cartão {p} pago')
                  else:
                    print('--- Conta ou cartão não encontrado.')
                elif gt == '0':
                  print('--- Voltando')
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
                  continue
                fatura = float(input('--- Digite o valor total do gasto:  '))
                if fatura <= 0:
                  print('--- Valor inválido. Voltando.')
                  continue
                desp['outros'][c]= {
                  'nome': c, 
                  'fatura': fatura, 
                  'status': 'pendente', 
                  'mes': meses[agora.month-1]
                }
                print('--- Gasto definido')
              elif bt == '2':
                print('--- Ver gastos variados do mês')
                print('-'*15)
                for nome, dados in desp['outros'].items():
                  print(f"--- Nome: {nome}")
                  print(f"--- Fatura: {dados['fatura']}")
                  print(f"--- Status: {dados['status']}")
                  print(f"--- Mês: {dados['mes']}")
                  print('-'*15)
                bt = input('--- Pressione Enter para voltar: ')
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
                    continue
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
                else:
                  print('--- Gasto não encontrado.')
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
                        continue
                    desp['outros'][p]['status'] = 'pago'
                    print(f'--- Gasto {p} pago')
                else:
                  print('--- Gasto não encontrado.')
              elif bt == '0':
                print('--- Voltando')
  elif r == '3':
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
    print(f'--- Receitas: R$ {total_rec}')
    print(f'--- Contas pendentes: R$ {total_desp}')
    print(f'--- Valor disponível após quitar as pendências: R$ {total_rec - total_desp}')
    r = input('--- Pressione Enter para voltar: ')
  elif r == '4':
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
          mt = input('--- Opção: ')
          continue
        total = float(input('--- Digite o valor total da meta:  '))
        if total <= 0:
          print('--- Valor inválido. Voltando.')
          mt = input('--- Opção: ')
          continue
        metas[m]= {'nome': m, 'total': total, 'valor': 0, 'estado': True}
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
          else:
            metas[a]['valor'] += a2
            print('--- Valor adicionado a meta')
            print(f'--- Meta: {a}')
            print(f'--- Objetivo: {metas[a]["total"]}')
            print(f'--- Valor atual: {metas[a]["valor"]}')
        else:
          print('--- Meta não encontrada')
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
        y = input('--- Pressione Enter para voltar: ')
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
          else:
            print('--- Voltando.')
        else:
          print('--- Meta não encontrada.')
          print('--- Voltando.')
      elif mt == '0':
        print('--- Voltando')
  elif r == '5':
      print('--- Extrato do mês')
      print('--- Meses: Jan, Fev, Mar, Abr, Mai, Jun, Jul, Ago, Set, Out, Nov, Dez')
      jk = input('--- Qual mês deseja ver o extrato? ').capitalize()
      if jk not in meses:
          print('--- Mês inválido. Voltando ao menu principal.')
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