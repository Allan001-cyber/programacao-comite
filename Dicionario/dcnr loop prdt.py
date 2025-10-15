stq={
    'Mochila': 100,
    'Caderno': 50,
    'Lapis': 200
}

print('   Estoque Atualizado')
for m,v in stq.items():
    print(f'\nProduto: {m} \nQuantidade: {v} \n')

stq.update({'Mochila': 27,'Caderno': 15,'Lapis': 100})
print(f'Vendas efetuadas com sucesso!\n')

print('   Estoque Atualizado')
for m,v in stq.items():
    print(f'\nProduto: {m} \nQuantidade: {v} \n')

stq['Caneta']= 80
stq['Estojo']= 50

print('   Estoque Atualizado')
for m,v in stq.items():
    print(f'\nProduto: {m} \nQuantidade: {v} \n')

del stq['Caderno']

print('   Estoque Atualizado')
for m,v in stq.items():
    print(f'\nProduto: {m} \nQuantidade: {v}')

stq.clear()

print('   Estoque Atualizado')
for m,v in stq.items():
    print(f'\nProduto: {m} \nQuantidade: {v}')