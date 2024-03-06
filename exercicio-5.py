def inverter_string(string):
    # Inicializa uma string vazia para armazenar a string invertida
    string_invertida = ""
    
    # Percorre a string de trás para frente e adiciona cada caractere à string invertida
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    
    return string_invertida

# Exemplo de uso:
# string_original = input("Digite uma string: ")  # Se quiser receber a string do usuário
string_original = "Olá, mundo!"  # Ou uma string pré-definida

string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)
