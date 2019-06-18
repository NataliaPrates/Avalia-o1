T= int(input('Informe o tamanho em metros quadrados: '))

#1 litro pinta 3m quadrados, entao uma lata de de 18 litros pinta 54m quadrados

if T % 54 == 0:
	latas = T / 54
else: 
	latas = int(T / 54)+1

preco = latas * 80
print ('Precisará de %d latas' %latas)
print ('O preço será R$ %.2f' %preco)