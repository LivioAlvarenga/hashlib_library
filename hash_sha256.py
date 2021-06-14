import hashlib


def criar_senha_sha256(senha: str, token: str = 'AmueDFGuyVsce8524') -> str:
    """Transforma senha em uma hash sha256.

    Args:
        senha (str utf-8): Senha string utf-8 que será transformada em hash
        sha256.
        token (str, optional): Token que será agregado a sua senha. Defaults
        to 'AmueDFGuyVsce8524'.

    Returns:
        str: senha codificada em hash sha256 hexadecimal.
    """
    return hashlib.sha256(str.encode(token+senha)).hexdigest()


def validar_senha_sha256(senha: str, senha_sha256: str) -> bool:
    """Valida uma senha digitada com a senha armazenada no formato hash sha256.

    Args:
        senha (str utf-8): Senha string utf-8 que será comparada com a senha
        armazenada.
        senha_sha256 (str hash sha256 hexadecimal): Senha hash sha256
        armazenada para comparação.

    Returns:
        bol: True = senhas iguais, login autorizado. False = senhas
        divergentes.
    """
    if criar_senha_sha256(senha) == senha_sha256:
        return True
    return False


# .Testando o código.
if __name__ == '__main__':

    # .Criando senha
    print('\nCRIANDO SENHA')

    senha = criar_senha_sha256('Admin')
    bd_username_password = {'admin': senha}

    for usuário, senha in bd_username_password.items():
        print(f'\nUsuário: {usuário}\nSenha: {senha}\n')

    # .Validando senha
    print('\nVALIDANDO SENHA')

    senha_digitada = 'Admin'
    valida_senha = validar_senha_sha256(
        senha_digitada, bd_username_password['admin'])

    if valida_senha:
        print(f'\nA senha {senha_digitada} é valida!')
    else:
        print(f'\nA senha {senha_digitada} é inválida!')

    senha_digitada = 'João'
    valida_senha = validar_senha_sha256(
        senha_digitada, bd_username_password['admin'])

    if valida_senha:
        print(f'\nA senha {senha_digitada} é valida!')
    else:
        print(f'\nA senha {senha_digitada} é inválida!')
