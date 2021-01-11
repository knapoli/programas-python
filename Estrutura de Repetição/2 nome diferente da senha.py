nome = input('Usuario: ')
senha = input('Senha: ')
while senha == nome:
    senha = input('Digite uma senha diferente de usuario: ')
print(nome, 'usuario')
print(senha, 'senha')