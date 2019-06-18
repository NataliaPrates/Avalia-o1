salario = float(input('Digite o salário: '))

if salario <= 280:
    salario2 = ((salario/100)*20) + salario
    percentual = '20%'
    reajuste = (salario/100)*20
elif salario > 280 and salario <= 700:
    salario2 = salario + (salario/100)*15
    percentual = '15%'
    reajuste = (salario/100)*15
elif salario > 700 and salario <= 1500:
    salario2 = salario + (salario/100)*10
    percentual = '10%'
    reajuste = (salario/100)*10
else:
    salario2 = salario + (salario/100)*5
    percentual = '5%'
    reajuste = (salario/100)*5

print ('Salário antes do reajuste: ', salario)
print ('Percetual de aumento aplicado: ', percentual)
print ('Valor do aumento: ', reajuste)
print ('Novo salário: ', salario2)