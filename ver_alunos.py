def visualizar(lista_alunos):
  if not lista_alunos:
    print('não há nota média por enquanto')
  else:
    for alunos in lista_alunos:
      print(f'{alunos["nome"]} | {alunos["primeira nota"]} | {alunos["segunda nota"]}')
          