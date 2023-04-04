print('-' * 26)
print('------- Banco Braz -------')
print('-' * 26)
print('\n')
print('-' * 35)
valor = int(input('que valor você quer sacar? R$'))
cont50 = cont20 = cont10 = cont1 = 0

print('-' * 35)
while valor > 0:
    if valor < 10:
        valor -= 1
        cont1 += 1
        if valor < 1:
            print(f'total de {cont1} cédulas de R$1')
    elif valor < 20:
        valor -= 10
        cont10 += 1
        if valor < 10:
            print(f'total de {cont10} cédulas de R$10')
    elif valor < 50:
        valor -= 20
        cont20 += 1
        if valor < 20:
            print(f'total de {cont20} cédulas de R$20')
    elif valor >= 50:
        valor -= 50
        cont50 += 1
        if valor < 50:
            print(f'total de {cont50} cédulas de R$50')
    elif valor == 0:
        break
print('-' * 30)
print('volte sempre ao Banco Braz! tenha um bom dia!')
