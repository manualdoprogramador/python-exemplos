# CRIANDO NOSSA COLECAO DE idades

idades = [30,52,40,18,20,60]
print('colecao original', idades)

#ADICIONANDO E REMOVENDO ITENS
idades.append(25)
print('adicionado o numero 25', idades)

idades.remove(40)
print('removendo o 40', idades)

#SE TIVERMOS DOIS ITES IGUAIS ELE REMOVE O PRIMEIRO
idades.append(18)
idades.remove(18)
print('adicionado e removendo o 18', idades)

#ADICIONADO UM ITEM NA POSICAO DESEJADA
idades.insert(0, 20)
print('adicionou um item na posicao desejada', idades)

#ADICIONADO UMA LISTA NA OUTRA
idades2 = [54, 80]
idades.extend(idades2)
print('Adicionando a lista idades2 na lista idades', idades)

#CRIAR UM NOVA LISTA SOMANDO MAIS UM ANO DE idades PARA POSICAO
idades_mais_um = []
for idade in idades:
    idades_mais_um.append(idade+1)

print('1 - somando mais 1 ano para cada posicao da idade',idades_mais_um)

idades_mais_um2 = [(idade+1) for idade in idades]
print('2 - somando mais 1 ano para cada posicao da idade',idades_mais_um2)

#Ordenar a lista, temos duas formas de fazer isso
idades.sort() #apartir daqui toda as vez que usar a lista idade ela vai estar ordenada
print(idades)
print(sorted(idades)) #Esse ordena somente nessa linha

#SE QUISER SABER O TAMANHO DA LISTA OU SE ELA ESTA VAZIA
print('Tamanho da lista', len(idades))
print('Lista esta vazia?', len(idades) == 0)


