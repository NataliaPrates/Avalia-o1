s=int(input('Digite: 1- para masculino/ 2- para feminino:'))
h=float(input('Digite sua Altura:'))
p=float(input('Digite seu peso:'))

pIdeal=(72.7*h)-58 if s==1 else (62.1*h)-44.7

if p < pIdeal:
    print('Voce esta abaixo do peso ideal!!!')
elif p == pIdeal:
    print('Voce esta com o peso ideal!!!')
else:
    print('Voce esta a cima do peso ideal!!!')
print('Peso:%.2f / Peso ideal:%.2f'%(p,pIdeal))

    