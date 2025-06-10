from registrar_aluno import registrando
from calcular_media import calculo
from ver_alunos import visualizar
lista_alunos = []
def main():
   while True: 
    print(' 1 - inserir aluno\n 2 - calcular média\n 3 - ver todos os alunos\n 4 - SAIR')
    opcao = str(input('digite o que deseja :'))
    if opcao == '1':
      registrando(lista_alunos)
    elif opcao == '2':
      calculo(lista_alunos)
    elif opcao == '3':
      visualizar(lista_alunos)
    elif opcao == '4':
      print('até mais')
      break
    else:
      print('opção invalida!')
    
main()