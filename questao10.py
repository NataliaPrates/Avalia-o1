usuario = input("Nome de usuario: ")
senha = input("Senha: ")

while senha == usuario:
	senha = input("Digite uma senha diferente do nome de usuário: ")

print ("Usuário: %s | Senha: %s" %(usuario, senha))