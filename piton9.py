import random  # Geração de números aleatórios
import time  # Medição de tempo

# Função para medir o tempo de execução
def medir_tempo(funcao, *args):
    inicio = time.time()  # Marca o início
    resultado = funcao(*args)  # Executa a função
    fim = time.time()  # Marca o fim
    return resultado, fim - inicio  # Retorna o resultado e o tempo total

# Função que gera dados aleatórios e salva em um arquivo
def gerar_dados_aleatorios(nome_arquivo, num_registros):
    chaves_geradas = set()
    with open(nome_arquivo, 'w') as f:
        while len(chaves_geradas) < num_registros:
            chave = random.randint(1, 10000)
            if chave not in chaves_geradas:
                dado1 = random.randint(1, 100)
                dado2 = ''.join(chr(random.randint(32, 126)) for _ in range(1000))
                f.write(f"{chave},{dado1},{dado2}\n")
                chaves_geradas.add(chave)

# Função de pesquisa sequencial
def pesquisa_sequencial(lista, chave):
    for cont, item in enumerate(lista):
        if item[0] == chave:
            return cont  # Retorna a posição
    return -1  # Retorna -1 se não encontrado

# Função para inserir em uma árvore binária
def inserir_binaria(arvore, valor):
    if arvore is None:
        return {"chave": valor, "esquerda": None, "direita": None}
    elif valor < arvore["chave"]:
        arvore["esquerda"] = inserir_binaria(arvore["esquerda"], valor)
    else:
        arvore["direita"] = inserir_binaria(arvore["direita"], valor)
    return arvore

# Função para buscar na árvore binária
def buscar_binaria(arvore, valor):
    if arvore is None:
        return None
    elif valor < arvore["chave"]:
        return buscar_binaria(arvore["esquerda"], valor)
    elif valor > arvore["chave"]:
        return buscar_binaria(arvore["direita"], valor)
    else:
        return arvore  # Retorna o nó encontrado

# Funções auxiliares para árvore AVL
def altura(arvore):
    if arvore is None:
        return 0
    return max(altura(arvore["esquerda"]), altura(arvore["direita"])) + 1

def fator_balanceamento(arvore):
    if arvore is None:
        return 0
    return altura(arvore["direita"]) - altura(arvore["esquerda"])

def rotacao_direita(y):
    x = y["esquerda"]
    y["esquerda"] = x["direita"]
    x["direita"] = y
    return x

def rotacao_esquerda(x):
    y = x["direita"]
    x["direita"] = y["esquerda"]
    y["esquerda"] = x
    return y

def inserir_avl(arvore, valor):
    if arvore is None:
        return {"chave": valor, "esquerda": None, "direita": None}
    elif valor < arvore["chave"]:
        arvore["esquerda"] = inserir_avl(arvore["esquerda"], valor)
    else:
        arvore["direita"] = inserir_avl(arvore["direita"], valor)

    fb = fator_balanceamento(arvore)

    if fb < -1 and valor < arvore["esquerda"]["chave"]:
        return rotacao_direita(arvore)
    if fb > 1 and valor > arvore["direita"]["chave"]:
        return rotacao_esquerda(arvore)
    if fb < -1 and valor > arvore["esquerda"]["chave"]:
        arvore["esquerda"] = rotacao_esquerda(arvore["esquerda"])
        return rotacao_direita(arvore)
    if fb > 1 and valor < arvore["direita"]["chave"]:
        arvore["direita"] = rotacao_direita(arvore["direita"])
        return rotacao_esquerda(arvore)

    return arvore

# Função para buscar na árvore AVL
def buscar_avl(arvore, valor):
    if arvore is None:
        return None
    elif valor < arvore["chave"]:
        return buscar_avl(arvore["esquerda"], valor)
    elif valor > arvore["chave"]:
        return buscar_avl(arvore["direita"], valor)
    else:
        return arvore  # Retorna o nó encontrado

# Função para carregar registros de um arquivo em uma lista
def carregar_dados(nome_arquivo):
    registros = []  # Lista para armazenar os registros
    with open(nome_arquivo, 'r') as f:
        for linha in f:
            partes = linha.strip().split(',')
            if len(partes) == 3:
                chave, dado1, dado2 = partes
                registros.append((int(chave), int(dado1), dado2))
    return registros

# Função principal para executar os experimentos
def executar_experimentos():
    tamanhos = [100, 500, 1000, 5000, 10000]  # Tamanhos dos arquivos

    for tamanho in tamanhos:
        nome_arquivo = f'dados_{tamanho}.txt'
        gerar_dados_aleatorios(nome_arquivo, tamanho)  # Gera o arquivo
        registros = carregar_dados(nome_arquivo)  # Carrega os registros

        chaves_busca = random.sample([r[0] for r in registros], 15)

        # Busca Sequencial
        print(f"\n--- Busca Sequencial ({tamanho} registros) ---")
        tempos_seq = [medir_tempo(pesquisa_sequencial, registros, chave)[1] for chave in chaves_busca]
        print(f"Tempo médio de busca sequencial: {sum(tempos_seq)/len(tempos_seq):.6f} segundos")

        # Árvore Binária
        arvore_binaria = None
        for registro in registros:
            arvore_binaria = inserir_binaria(arvore_binaria, registro[0])

        print(f"\n--- Árvore Binária ({tamanho} registros) ---")
        tempos_bin = [medir_tempo(buscar_binaria, arvore_binaria, chave)[1] for chave in chaves_busca]
        print(f"Tempo médio de busca em árvore binária: {sum(tempos_bin)/len(tempos_bin):.6f} segundos")

        # Árvore AVL
        arvore_avl = None
        for registro in registros:
            arvore_avl = inserir_avl(arvore_avl, registro[0])

        print(f"\n--- Árvore AVL ({tamanho} registros) ---")
        tempos_avl = [medir_tempo(buscar_avl, arvore_avl, chave)[1] for chave in chaves_busca]
        print(f"Tempo médio de busca em árvore AVL: {sum(tempos_avl)/len(tempos_avl):.6f} segundos")

if __name__ == "__main__":
   def executar_experimentos():
    tamanhos = [100, 500, 1000, 5000, 10000]  # Tamanhos dos arquivos

    for tamanho in tamanhos:
        nome_arquivo = f'dados_{tamanho}.txt'
        gerar_dados_aleatorios(nome_arquivo, tamanho)  # Gera o arquivo
        registros = carregar_dados(nome_arquivo)  # Carrega os registros

        # Garante que o número de chaves a serem buscadas não exceda o número de registros
        num_chaves_busca = min(15, len(registros))  # Obtém o menor valor entre 15 e o número de registros
        chaves_busca = random.sample([r[0] for r in registros], num_chaves_busca)

        # Busca Sequencial
        print(f"\n--- Busca Sequencial ({tamanho} registros) ---")
        tempos_seq = [medir_tempo(pesquisa_sequencial, registros, chave)[1] for chave in chaves_busca]
        print(f"Tempo médio de busca sequencial: {sum(tempos_seq)/len(tempos_seq):.6f} segundos")

        # Árvore Binária
        arvore_binaria = None
        for registro in registros:
            arvore_binaria = inserir_binaria(arvore_binaria, registro[0])

        print(f"\n--- Árvore Binária ({tamanho} registros) ---")
        tempos_bin = [medir_tempo(buscar_binaria, arvore_binaria, chave)[1] for chave in chaves_busca]
        print(f"Tempo médio de busca em árvore binária: {sum(tempos_bin)/len(tempos_bin):.6f} segundos")

        # Árvore AVL
        arvore_avl = None
        for registro in registros:
            arvore_avl = inserir_avl(arvore_avl, registro[0])

        print(f"\n--- Árvore AVL ({tamanho} registros) ---")
        tempos_avl = [medir_tempo(buscar_avl, arvore_avl, chave)[1] for chave in chaves_busca]
        print(f"Tempo médio de busca em árvore AVL: {sum(tempos_avl)/len(tempos_avl):.6f} segundos")
