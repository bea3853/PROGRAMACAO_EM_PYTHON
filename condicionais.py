dados = {
'nomes':[input('Nome:'), input('Nome: ')],
'idades':[int(input('Idade: ')), int(input('Idade: '))],
'quartos':['','S','D','L'],
'valores':[0,100.0,150.0,250.0]   

}


print('faça sua escolha')

quant = int(input('Dias'))
id = int(input('Escolha o ID do quarto'))

print(f'Quarto escolhido: {dados["quartos"][id]}')
valor = dados['valores'][id]

calculo = quant * valor

print(' Hospedagem R$', round(float(calculo),2))



