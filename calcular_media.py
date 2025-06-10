import math
def calculo(lista_alunos):
 if not lista_alunos:
    print('não há alunos para calcular')
 nome_verificar = str(input('digite seu nome :'))
 for alunos in lista_alunos:
   if nome_verificar == alunos['nome']:
     total_media = (alunos["primeira nota"] + alunos["segunda nota"]) / 2
     if total_media > 10 :
      media_arredondada = math.floor(total_media)
      print(f' a média do aluno : {alunos["nome"]} | {media_arredondada}')
     else:    
       print(f' a média do aluno : {alunos["nome"]} | {total_media}')
   else:
     print('nome invalido!')

