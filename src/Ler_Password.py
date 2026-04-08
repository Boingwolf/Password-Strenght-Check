import getpass


def ler_password(prompt="Escreva a sua Password: "):
    """Usa apenas getpass para ler a password."""
    try:
        return getpass.getpass(prompt, echo_char="*")
    except TypeError:
        return getpass.getpass(prompt)

