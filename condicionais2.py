# O sistema deve permitir que o usuário "cadastre" 
# o nome e a idade de até 3 clientes.

print('CADASTRO')

dados_nomes = []
dados_idades = []

nome1 = input('Nome: ')
idade1 =int(input('Idade:')) 

nome2 = input('Nome: ')
idade2 =int(input('Idade:')) 

nome3 = input('Nome: ')
idade3 =int(input('Idade:')) 

dados_nomes.append(nome1)
dados_idades.append(idade1)

# escolha de quartos

QUARTOS  =  ['',"Simples", "Duplo" , "Luxo"]
valores =  [0,100.,150.,250]

print('quartos - ' , QUARTOS)
print('VALORES - ' , valores)

total =  []

escolha1 = int(input('Escolha o ID do quarto 1'))
escolha2 = int(input('Escolha o ID do quarto 2'))
escolha3 = int(input('Escolha o ID do quarto 3'))

dias1 = int(input('Escolha A QUANTIDADE DE DIAS: 1'))
dias2 = int(input('Escolha A QUANTIDADE DE DIAS: 2'))
dias3 = int(input('Escolha A QUANTIDADE DE DIAS: 3'))

if escolha1 == 1:
    print('VC ESCOLHEU O QUARTO :', QUARTOS[escolha1])
    cal =  dias1 * valores[escolha1]
    print('totaL',cal)
elif escolha1 == 2:
    print('VC ESCOLHEU O QUARTO :', QUARTOS[escolha1])
    cal =  dias1 * valores[escolha1]
    print('totaL',cal)        
elif escolha1 == 3:
    print('VC ESCOLHEU O QUARTO :', QUARTOS[escolha1])
    cal =  dias1 * valores[escolha1]
    print('totaL',cal)     


    
if escolha2 == 1:
    print('VC ESCOLHEU O QUARTO :', QUARTOS[escolha1])
    cal =  dias2 * valores[escolha1]
    print('totaL',cal)
elif escolha2 == 2:
    print('VC ESCOLHEU O QUARTO :', QUARTOS[escolha1])
    cal =  dias2 * valores[escolha1]
    print('totaL',cal)        
elif escolha2 == 3:
    print('VC ESCOLHEU O QUARTO :', QUARTOS[escolha1])
    cal =  dias2 * valores[escolha1]
    print('totaL',cal)     




if escolha3 == 1:
    print('VC ESCOLHEU O QUARTO :', QUARTOS[escolha3])
    cal =  dias3 * valores[escolha3]
    print('totaL',cal)
elif escolha3 == 2:
    print('VC ESCOLHEU O QUARTO :', QUARTOS[escolha3])
    cal =  dias3 * valores[escolha3]
    print('totaL',cal)        
elif escolha3 == 3:
    print('VC ESCOLHEU O QUARTO :', QUARTOS[escolha3])
    cal =  dias3 * valores[escolha3]
    print('totaL',cal) 