print('-' * 20)
print('CADASTRE UMA PESSOA')
print('-' * 20)
total18 = 0 #início da contagem
rapaz18 = 0 #início da contagem
mulher20 = 0 #início da contagem
while True:
    idade = int(input('Digite sua idade: '))

    sexo = ' ' #NÃO ESQUECER DISSO!!!!!!!
    while sexo not in 'MF': #while sexo not in 'MF' = enquanto sexo não for 'MF'
        sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]

    if idade >= 18:
        total18 += 1 #acréscimo de +1 na contagem
    if sexo == 'M':
        rapaz18 += 1 #acréscimo de +1 na contagem
    if sexo == 'F' and idade < 20:
        mulher20 += 1 #acréscimo de +1 na contagem

    c = ' ' #NÃO ESQUECER DISSO!!!!!!!
    while c not in 'SN': #while c not in 'SN' = enquanto c não for 'SN'
        c = input('Deseja continuar [S/N]: ').strip().upper()[0]

    if c == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {total18};')
print(f'Ao todo temos {rapaz18} rapaz(es) cadastrado(s);')
print(f'E temos {mulher20} mulher(es) com menos de 20 anos.')