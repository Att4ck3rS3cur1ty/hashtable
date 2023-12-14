# parte 1:

'''

tabela_hash = [None] * 11

# garante que ficará no range da tabela => [0,len(hash_table)-1]. 
def funcao_hash(chave):
    return chave % len(tabela_hash)

# para inserir o par de chave/valor, pegamos a chave hash e armazenamos o valor ao slot
def inserir(chave, valor):
    chave_hash = funcao_hash(chave)
    tabela_hash[chave_hash] = valor

# mostrar tabela vazia
print(tabela_hash)

# inserir 6 na posição 5 e mostrar o valor
inserir(5,6)
print(tabela_hash)

# inserir 8 na posição 5 e mostrar o valor
inserir(5,8)
print(tabela_hash)
'''

# parte 2:

tabela_hash = [None] * 11

# garante que ficará no range da tabela => [0,len(hash_table)-1]. 
def funcao_hash(chave):
    return chave % len(tabela_hash)

# para inserir o par de chave/valor, pegamos a chave hash e armazenamos o valor ao slot
def inserir(chave, valor):
    chave_hash = funcao_hash(chave)

    # resolver problema de colisão! Se o slot atual estiver ocupado, pular para procurar espaço no próximo.
    while(tabela_hash[chave_hash]):
        chave_hash = (chave_hash + 1) % len(tabela_hash)
    
    tabela_hash[chave_hash] = valor

# mostrar tabela vazia
print(tabela_hash)

# inserir 6 na posição 5 e mostrar o valor
inserir(5,6)
print(tabela_hash)

# inserir 8 na posição 5 e mostrar o valor
inserir(5,8)
print(tabela_hash)
