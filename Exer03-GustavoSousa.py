# Peça ao usuário para inserir os nomes de três pessoas que deseja convidar para uma festa e armazená-las em uma lista
# Depois de inserir os três nomes, pergunte se deseja adicionar outro. Se o fizer, permita que adicione mais nomes até responder "não". 
# Quando ele responder "não", mostre quantas pessoas ele convidou para a festa, uma vez que o usuário tenha completado sua lista de nomes
# exiba a lista completa e peça que ele digite um dos nomes da lista. Exiba a posição desse nome na lista. 
# Pergunte ao usuário se ele ainda deseja que essa pessoa venha à festa. Se ele responder "não", exclua essa entrada da lista e exiba a lista novamente.

nomes = []
for i in range(3):
    nome = str(input("Digite o nome da pessoa que quer convidar : "))
    nomes.append(nome)
pergunta = str(input("Deseja continuar s/n : "))
if pergunta == "s":
    for i in range(100):
        nome = str(input("Digite o nome da pessoa que quer convidar : "))
        nomes.append(nome)
        pergunta2 = str(input("Deseja continuar s/n : "))
        if pergunta2 == "n":
            break
    else:
        print(nome)

print (nomes)        
pergunta3 = str(input("Deseja excluir alguem da lista : "))
nomes.remove(pergunta3)
print(nomes)