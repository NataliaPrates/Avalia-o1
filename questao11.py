
num = input("digite um numero de 1 a 10: ")
cont = 1
if num>=1 and num<=10:

 while cont<=10:
   tab = num * cont
   print ("%d × %d = %d" % num, cont, tab)
   cont = cont + 1
  
else:
  print "apenas valores de 1 a 10"