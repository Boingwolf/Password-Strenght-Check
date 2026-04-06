import criterios
import getpass

if __name__ == "__main__":
    password_input = getpass.getpass("Escreva a sua Password: ")
    
    password = criterios.Criterios(password_input)
    
    criterios_validos = [
        password.tamanho(),
        password.letra_maiuscula(),
        password.letra_minuscula(),
        password.tem_Numero(),
        password.tem_Simbolo(),
        password.password_previsivel()[0] == False
    ]
    count_Criterios = 0

    for criterio in criterios_validos:
        if criterio:
            count_Criterios += 1
    
    if count_Criterios == 5:
        print("A sua Password é Forte")
    elif count_Criterios >= 3:
        print("A sua Password é Média")
    else:
        print("A sua Password é Fraca")
        
    print(f"Você cumpriu {count_Criterios}/5 critérios.")
        
    melhorias = []

    if not criterios_validos[0]:
        melhorias.append("- Deve conter no mínimo 10 caracteres.")

    if not criterios_validos[1]:
        melhorias.append("- Deve conter pelo menos uma letra maiúscula.")

    if not criterios_validos[2]:
        melhorias.append("- Deve conter pelo menos uma letra minúscula.")

    if not criterios_validos[3]:
        melhorias.append("- Deve conter pelo menos um número.")

    if not criterios_validos[4]:
        melhorias.append("- Deve conter pelo menos um símbolo.")
        
    if not criterios_validos[5]:
        melhorias.append("- A password é previsível, evite usar palavras comuns ou sequências.")
        
        motivos = password.password_previsivel()[1]
        for motivo in motivos:
            melhorias.append(f"  - {motivo}")

    if melhorias:
        print("\nPode melhorar a sua password em:")
        for melhoria in melhorias:
            print(melhoria)
    else:
        print("A sua password cumpre todos os critérios definidos.")