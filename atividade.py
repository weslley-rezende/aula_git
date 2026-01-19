# menu atividade.py

def ler_int(msg):
    while True:
        try:
            return int(input(msg).strip())
        except ValueError:
            print("❌ Digite um número inteiro válido.")


def ler_float(msg):
    while True:
        txt = input(msg).strip().replace(",", ".")  # aceita vírgula ou ponto
        try:
            return float(txt)
        except ValueError:
            print("❌ Digite um número válido (ex.: 1.75 ou 1,75).")


def ler_str(msg):
    while True:
        s = input(msg).strip()
        if s:
            return s
        print("❌ Não pode ser vazio.")


def ler_bool(msg):
    while True:
        s = input(msg + " (s/n): ").strip().lower()
        if s in ("s", "sim", "y", "yes"):
            return True
        if s in ("n", "nao", "não", "no"):
            return False
        print("❌ Responda com s/n (sim/não).")


def exemplo_variavel_tipos():
    print("\n=== Variáveis e Tipos (interativo) ===")
    nome = ler_str("Digite seu nome: ")
    idade = ler_int("Digite sua idade (int): ")
    altura = ler_float("Digite sua altura (float): ")
    estudando_python = ler_bool("Você está estudando Python?")

    altura_inteira = int(altura)  # float -> int (trunca)

    print("\n--- Resultado ---")
    print("Nome (str):", nome)
    print("Idade (int):", idade)
    print("Altura (float):", altura)
    print("Estudando Python (bool):", estudando_python)
    print("Altura convertida para int (truncada):", altura_inteira)


def exemplo_operacoes_aritmeticas():
    print("\n=== Operações Aritméticas (interativo) ===")
    a = ler_float("Digite o valor de a: ")
    b = ler_float("Digite o valor de b: ")

    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao_real = None
    if b != 0:
        divisao_real = a / b

    # Para divisão inteira, resto e potência faz mais sentido usar inteiros
    ai = int(a)
    bi = int(b)

    print("\n--- Resultado ---")
    print(f"a = {a} | b = {b}")
    print("Soma (a + b) =", soma)
    print("Subtração (a - b) =", subtracao)
    print("Multiplicação (a * b) =", multiplicacao)
    if divisao_real is None:
        print("Divisão real (a / b) = indefinida (b = 0)")
    else:
        print("Divisão real (a / b) =", divisao_real)

    if bi == 0:
        print("Divisão inteira (a // b) = indefinida (b = 0)")
        print("Resto (a % b) = indefinido (b = 0)")
    else:
        print(f"Divisão inteira (int(a) // int(b)) = {ai // bi}  (usando int(a)={ai} e int(b)={bi})")
        print(f"Resto (int(a) % int(b)) = {ai % bi}  (usando int(a)={ai} e int(b)={bi})")

    print(f"Potência (int(a) ** int(b)) = {ai ** bi}  (usando int(a)={ai} e int(b)={bi})")


def exemplo_controle_condicional():
    print("\n=== Controle Condicional + Operadores Lógicos (interativo) ===")
    nota = ler_float("Digite a nota (0 a 10): ")
    frequencia = ler_int("Digite a frequência em % (0 a 100): ")

    aprovado = (nota >= 7) and (frequencia >= 75)
    reprovado_por_falta = not (frequencia >= 75)

    if nota >= 9:
        conceito = "A"
    elif nota >= 7:
        conceito = "B"
    elif nota >= 5:
        conceito = "C"
    else:
        conceito = "D"

    print("\n--- Resultado ---")
    print("Nota:", nota)
    print("Frequência (%):", frequencia)
    print("Conceito:", conceito)
    print("Aprovado (nota>=7 and freq>=75):", aprovado)
    print("Reprovado por falta (not freq>=75):", reprovado_por_falta)


def exemplo_estrutura_repeticao():
    print("\n=== Estruturas de Repetição (interativo) ===")

    # FOR: somar 1..N
    n = ler_int("Somar de 1 até N. Digite N: ")
    if n < 1:
        print("❌ N precisa ser >= 1")
    else:
        soma = 0
        for numero in range(1, n + 1):
            soma += numero
        print(f"Soma de 1 a {n} =", soma)

    # WHILE: listar os K primeiros pares
    k = ler_int("Quantos números pares você quer gerar? (K): ")
    if k < 1:
        print("❌ K precisa ser >= 1")
    else:
        pares = []
        atual = 0
        while len(pares) < k:
            atual += 1
            if atual % 2 == 0:
                pares.append(atual)
        print(f"{k} primeiros pares =", pares)


def calcular_media(n1, n2):
    return (n1 + n2) / 2


def exemplo_funcao():
    print("\n=== Função com Parâmetros e Retorno (interativo) ===")
    n1 = ler_float("Digite a primeira nota: ")
    n2 = ler_float("Digite a segunda nota: ")
    media = calcular_media(n1, n2)

    print("\n--- Resultado ---")
    print("Nota 1 =", n1)
    print("Nota 2 =", n2)
    print("Média =", media)


def exemplo_lista_dict():
    print("\n=== Lista e Dicionário (interativo) ===")

    # LISTA: o usuário monta a lista
    qtd = ler_int("Quantos itens você quer colocar na lista de compras? ")
    compras = []
    for i in range(qtd):
        item = ler_str(f"Digite o item {i+1}: ")
        compras.append(item)

    print("\nLista criada:", compras)

    # Adicionar
    novo = ler_str("Digite um item para ADICIONAR (append): ")
    compras.append(novo)
    print("Lista após append:", compras)

    # Atualizar por índice
    if len(compras) > 0:
        idx = ler_int(f"Digite o índice para ATUALIZAR (0 até {len(compras)-1}): ")
        if 0 <= idx < len(compras):
            novo_valor = ler_str("Digite o novo valor: ")
            compras[idx] = novo_valor
            print("Lista após atualização:", compras)
        else:
            print("❌ Índice inválido. Pulando atualização.")

    # Remover por valor
    remover = ler_str("Digite um item para REMOVER (por valor): ")
    if remover in compras:
        compras.remove(remover)
        print("Lista após remoção:", compras)
    else:
        print("❌ Esse item não existe na lista. Nada removido.")

    # DICIONÁRIO: o usuário cria/edita
    print("\n--- Dicionário (aluno) ---")
    aluno = {}
    aluno["nome"] = ler_str("Nome do aluno: ")
    aluno["idade"] = ler_int("Idade do aluno: ")

    print("Dicionário inicial:", aluno)

    # Adicionar chave
    curso = ler_str("Digite um curso para ADICIONAR (chave 'curso'): ")
    aluno["curso"] = curso
    print("Após adicionar 'curso':", aluno)

    # Atualizar idade
    nova_idade = ler_int("Digite uma nova idade para ATUALIZAR: ")
    aluno["idade"] = nova_idade
    print("Após atualizar idade:", aluno)

    # Remover chave curso
    if "curso" in aluno:
        del aluno["curso"]
        print("Após remover 'curso':", aluno)


def executar_todos():
    exemplo_variavel_tipos()
    exemplo_operacoes_aritmeticas()
    exemplo_controle_condicional()
    exemplo_estrutura_repeticao()
    exemplo_funcao()
    exemplo_lista_dict()


def menu():
    while True:
        print("\n" + "=" * 45)
        print("MENU - ATIVIDADE (INTERATIVO)")
        print("=" * 45)
        print("1) Variáveis e Tipos")
        print("2) Operações Aritméticas")
        print("3) Controle Condicional + Operadores Lógicos")
        print("4) Estruturas de Repetição (for/while)")
        print("5) Função (parâmetros e retorno)")
        print("6) Lista e Dicionário")
        print("7) Executar TUDO")
        print("0) Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            exemplo_variavel_tipos()
        elif opcao == "2":
            exemplo_operacoes_aritmeticas()
        elif opcao == "3":
            exemplo_controle_condicional()
        elif opcao == "4":
            exemplo_estrutura_repeticao()
        elif opcao == "5":
            exemplo_funcao()
        elif opcao == "6":
            exemplo_lista_dict()
        elif opcao == "7":
            executar_todos()
        elif opcao == "0":
            print("Saindo... ✅")
            break
        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione ENTER para voltar ao menu...")


if __name__ == "__main__":
    menu()