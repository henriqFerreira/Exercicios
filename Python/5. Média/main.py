# Faça um programa que leia as duas notas de um aluno em uma matéria e mostre
# na tela a sua média na disciplina.
# 
# Ex:
# Nota 1: 4.5
# Nota 2: 8.5
# A média entre 4.5 e 8.5 é igual a 6.5
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
media = (nota1 + nota2)/2
print("A média entre " + str(nota1) + " e " + str(nota2) + " é igual a " + str(media))