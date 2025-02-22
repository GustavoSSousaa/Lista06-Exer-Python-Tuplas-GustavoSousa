# - Faça um programa que o usuario insira 10 produtos numa tupla.
# Exiba todos os produtos, solicite ao usuário para digitar um nome de produto e exiba a posição dele,
# em seguida peça para digitar numero entre 0 e 9 e exiba o produto da tupla.

produtos = ("Queijo", "arroz", "suco", "cafe", "presunto", "leite", "açucar", "cheedar", "batata", "margarina")

print(produtos)
nprodutos = str(input("Digite o produto : "))
if nprodutos in produtos:
    pprodutos = produtos.index(nprodutos)
    print ("o produto {} esta na posição {} " .format(nprodutos,pprodutos))
    