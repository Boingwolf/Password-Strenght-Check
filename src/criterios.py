import string
import re

PASSWORD_PREVISIVEL = [
    "password", 
    "123456", 
    "123456789", 
    "12345678", 
    "12345", 
    "111111", 
    "1234567", 
    "sunshine", 
    "qwerty", 
    "iloveyou",
    "princess", 
    "admin", 
    "welcome", 
    "666666", 
    "abc123", 
    "football", 
    "123123", 
    "monkey", 
    "654321", 
    "!@#$%^&*"
    ]

class Criterios:
    def __init__(self, password):
        self.password = password
    
    def tamanho(self):
        return len(self.password) >= 10
    
    def letra_maiuscula(self):
        return any(char.isupper() for char in self.password)
    
    def letra_minuscula(self):
        return any(char.islower() for char in self.password)
    
    def tem_numero(self):
        return any(char.isdigit() for char in self.password)
    
    def tem_simbolo(self):
        simbolos = string.punctuation
        return any(char in simbolos for char in self.password)
    
    def password_previsivel(self):
        pass_limpa = self.password.strip().lower()
        motivos = []
        if pass_limpa in PASSWORD_PREVISIVEL:
            motivos.append("A password está na lista de passwords comuns.")
        
        if any(sequencia in pass_limpa for sequencia in ["123", "abc", "qwerty"]):
            motivos.append("A password contém uma sequência previsível.")
        
        if re.search(r"\b\d{4}\b", pass_limpa):
            motivos.append("A password contém um ano, o que a torna mais previsível.")

        return len(motivos) > 0, motivos

