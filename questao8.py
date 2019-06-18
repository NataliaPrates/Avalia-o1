
perguntas = ["Telefonou para a vítima? S ou N: " ,
             "Esteve no local do crime? S ou N: " ,
             "Mora perto da vítima? S ou N: " ,
             "Devia para a vítima? S ou N: " ,
             "Já trabalhou com a vítima? S ou N: "]

resposta = 0

for qual in perguntas:
  resposta += (input(qual) == "S")
  
if resposta == 5:
  print("Assassino")
elif resposta >=3:
  print("Cúmplice")
elif resposta ==2:
  print("Suspeito")
else:
  print("Inocente")
