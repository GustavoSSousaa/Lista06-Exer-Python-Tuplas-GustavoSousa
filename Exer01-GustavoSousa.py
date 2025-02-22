# Crie uma tupla contendo os nomes de cinco países e exiba toda a tupla. 
# Peça ao usuário para inserir um dos países
# que foram mostrados a ele e, em seguida, exibir o número de índice (ou seja, posição na lista) desse item na tupla.

paises = ("Brasil", "Canadá", "Japão", "Alemanha", "Austrália")

print("Lista de países disponíveis:")
for i, pais in enumerate(paises, start=0):
    print(f"{i}. {pais}")

pais_escolhido = input("Digite o nome de um dos países mostrados: ")


if pais_escolhido in paises:
    posicao = paises.index(pais_escolhido) 
    print(f"O país '{pais_escolhido}' está na posição {posicao} da lista.")
else:
    print ("Esse pais não esta na lista")