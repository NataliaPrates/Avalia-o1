quanto= float(input('Quanto ganha por hora? '))
horas= int(input('Horas trabalhadas por mês: '))

salario= quanto * horas
ir = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05

print ('+ Salário Bruto : R$ %.2f' %salario)
print ('- IR: R$ %.2f' %ir )
print ('- INSS: R$ %.2f' %inss )
print ('- Sindicato: R$ %.2f' %sindicato )
print ('= Salário Liquido : R$ %.2f' %(salario - ir - inss - sindicato))