"""
Sentinel Data
---------------
Responsável pelo hashing e validação
das senhas dos usuários.
"""

from pwdlib import PasswordHash


# Cria o objeto responsável pelo hashing.
#
# O método recommended() seleciona uma
# configuração segura recomendada pela biblioteca.
password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    """
    Transforma uma senha em um hash seguro.

    A senha original nunca deve ser armazenada
    diretamente no banco de dados.
    """

    return password_hash.hash(password)


def verify_password(
    password: str,
    hashed_password: str,
) -> bool:
    """
    Verifica se a senha informada corresponde
    ao hash armazenado no banco.
    """

    return password_hash.verify(
        password,
        hashed_password,
    )