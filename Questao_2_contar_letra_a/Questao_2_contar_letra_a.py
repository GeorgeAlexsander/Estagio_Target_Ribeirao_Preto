def contar_letra_a(string):
    """
    Verifica a existência da letra 'a' (maiúscula ou minúscula) em uma string
    e conta quantas vezes ela ocorre.
    
    Parâmetros:
    string (str): A string em que a letra 'a' será contada.
    
    Retorna:
    None: Imprime a quantidade de vezes que a letra 'a' aparece na string.
    """
    # Converte a string para minúsculas para facilitar a contagem
    string = string.lower()
    
    # Conta a ocorrência da letra 'a'
    quantidade = string.count('a')
    
    # Verifica se a letra 'a' existe na string
    if quantidade > 0:
        print(f"A letra 'a' aparece {quantidade} vez(es) na string.")
    else:
        print("A letra 'a' não aparece na string.")

# Entrada da string
entrada = input("Digite uma string: ")
contar_letra_a(entrada)