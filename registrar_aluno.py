def registrando(lista_alunos):
  while True: 
   try: 
    nome = str(input('qual seu nome :'))
    nota1 = float(input('qual sua primeira nota :'))
    nota2 = float(input('qual sua segunda nota :'))
    if (nota1 < 0 or nota1 > 10) or (nota2 < 0 or nota2 > 10):
     print('apenas notas de 1 - 10')
    alunos = {'nome' : nome ,
              'primeira nota' : nota1 ,
              'segunda nota' : nota2
              }
    lista_alunos.append(alunos)
    print('aluno e nota adicionados')
    break
   except ValueError:
     print('apenas números!')