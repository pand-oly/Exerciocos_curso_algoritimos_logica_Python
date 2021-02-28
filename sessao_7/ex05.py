nome = input('Nome de usuario: ')
senha = input('Senha: ')

while senha == nome:
    print('Senha não pode ser igual nome de usuario')
    nome = input('Nome de usuario: ')
    senha = input('Senha: ')
