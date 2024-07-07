import json


#Função para mostrar o menu principal
def mostrar_menu_principal():
    # Exibir o Menu Principal
    print("-=-=-=-=-=-=-=-=-=-=-" * 2)
    print(" Olá! Como vai? Este é o menu principal:")
    print("-=-=-=-=-=-=-=-=-=-=-" * 2)
    print("Estudantes\nProfessores\nDisciplinas\nTurmas\nMatrículas\nSair")

    return input("Escolha a opção desejada: ")


#Função para mostrar o menu de operações
def mostrar_menu_operacoes(opcao):
    print("-=-=-=-=-=-=-=-=-=-=-" * 2)
    print(f"Menu de operações para {opcao}: ")
    print("-=-=-=-=-=-=-=-=-=-=-" * 2)
    print("Incluir\nListar\nAtualizar\nExcluir\nVoltar ao Menu Principal")

    return input("Escolha entre as opções listadas o que deseja fazer (ou 0 para retornar ao menu principal): ")


# Listas
lista_estudantes = []
lista_professores = []
lista_disciplinas = []
lista_turmas = []
lista_matriculas = []



#Funções para trabalhar com as opções: estudantes e professores
def cadastrar_pessoa(lista, opcao):
    while True:
        codigo = int(input("Digite o código a ser cadastrado: "))
        nome = input(f"Digite o nome a ser cadastrado: ")
        cpf = input(f"Digite o CPF a ser cadastrado: ")

        pessoa = {"Código": codigo,
                  "Nome": nome,
                  "CPF": cpf
                  }

        lista.append(pessoa)

        print(f"{opcao} adicionado com sucesso!")
        deseja = input("Deseja continuar? [S/N]: ")
        if deseja.lower() in "n":
            print(f"\n{opcao} adicionados com sucesso:\n{lista}\n")
            if opcao in "Estudantes estudantes":
                #lista = ler_arquivo(arquivo_estudante)
                salvar_arq(lista, "estudante.json")
            elif opcao in "Professores professores":
                #lista = ler_arquivo(arquivo_professor)
                salvar_arq(lista, "professor.json")

            break


def listar_pessoas(lista, opcao):
    if opcao.lower() in ("estudantes", "professores"):
        if opcao.lower() == "estudantes":
            lista = ler_arquivo(arquivo_estudante)
        else:
            lista = ler_arquivo(arquivo_professor)

        if not lista:
            print(f"Não há {opcao.lower()} cadastrados.")
            return

        print(f"\n>>> {opcao} Cadastrados <<<")
        for pessoa in lista:

            if opcao.lower() == "estudantes":
                print("Código:", pessoa["Código"])
                print("Nome:", pessoa["Nome"])
                print("CPF:", pessoa["CPF"])
            elif opcao.lower() == "professores":
                print("Código:", pessoa["Código"])
                print("Nome:", pessoa["Nome"])
                print("CPF:", pessoa["CPF"])
            print("-----------------------------")
    else:
        print("opão invalida")
    return True


def editar_pessoa(lista, opcao):
    while True:
        if opcao.lower() in ("estudantes", "professores"):
            if opcao.lower() == "estudantes":
                codigo = int(input(f"Digite o código do {opcao.lower()} que deseja editar: "))
                lista = ler_arquivo(arquivo_estudante)
                for pessoa in lista:
                    if pessoa["Código"] == codigo:
                        nome = input(f"Digite o novo nome do {opcao.lower()}: ")
                        cpf = input(f"Digite o novo CPF do {opcao.lower()}: ")

                        pessoa["Nome"] = nome
                        pessoa["CPF"] = cpf

                        print(f"{opcao} editado com sucesso!")
                        salvar_arq(lista, "estudante.json")
                        return
        if opcao.lower() in ("estudantes", "professores"):
            if opcao.lower() == "professores":
                codigo = int(input(f"Digite o código do {opcao.lower()} que deseja editar: "))
                lista = ler_arquivo(arquivo_professor)
                for pessoa in lista:
                    if pessoa["Código"] == codigo:
                        nome = input(f"Digite o novo nome do {opcao.lower()}: ")
                        cpf = input(f"Digite o novo CPF do {opcao.lower()}: ")

                        pessoa["Nome"] = nome
                        pessoa["CPF"] = cpf

                        print(f"{opcao} editado com sucesso!")
                        salvar_arq(lista, "professor.json")
                        return
        print(f"{opcao} não encontrado!")


def excluir_pessoa(lista, opcao):
    while True:
        if opcao.lower() in ("estudantes", "professores"):
            if opcao.lower() == "estudantes":
                codigo = int(input(f"Digite o código do {opcao.lower()} que deseja excluir: "))
                lista = ler_arquivo(arquivo_estudante)
                for pessoa in lista:
                    if pessoa["Código"] == codigo:
                        lista.remove(pessoa)
                        print(f"{opcao} excluído com sucesso!")
                        salvar_arq(lista, "estudante.json")
                        return
        if opcao.lower() in ("estudantes", "professores"):
            if opcao.lower() == "professores":
                codigo = int(input(f"Digite o código do {opcao.lower()} que deseja excluir: "))
                lista = ler_arquivo(arquivo_professor)
                for pessoa in lista:
                    if pessoa["Código"] == codigo:
                        lista.remove(pessoa)
                        print(f"{opcao} excluído com sucesso!")
                        salvar_arq(lista, "professor.json")
                        return
        else:
            break

        if not lista:
            print(f"Não há {opcao.lower()} cadastrados.")
            return



#Funções para trabalhar com as opções: Disciplinas, turmas e matriculas
def cadastrar_dado(lista, nome_dado):
    while True:
        codigo = int(input(f"Digite o código da {nome_dado.lower()}: "))
        nome = input(f"Digite o nome da {nome_dado.lower()}: ")

        dado = {"Código": codigo,
                "Nome": nome
                }

        lista.append(dado)

        print(f"{nome_dado} adicionada com sucesso!")
        deseja = input("Deseja continuar? [S/N]: ")
        if deseja.lower() in "n":
            print(f"\n{nome_dado}s adicionadas com sucesso:\n{lista}\n")
            if opcao in "Disciplinas disciplinas":
                salvar_arq(lista, "disciplina.json")
            elif opcao in "Turmas turmas":
                salvar_arq(lista, "turma.json")
            elif opcao in "Matrículas matrículas":
                salvar_arq(lista, "matricula.json")
            break


def listar_dado(lista, nome_dado):
    if opcao.lower() in "disciplinas turmas matrículas":
        if opcao.lower() == "disciplinas":
            lista = ler_arquivo(arquivo_disciplina)
        elif opcao.lower() == "turmas":
            lista = ler_arquivo(arquivo_turma)
        elif opcao.lower() == "matrículas":
            lista = ler_arquivo(arquivo_matricula)

        if not lista:
            print(f"Não há {nome_dado.lower()} cadastradas.")
            return

        print(f"\n>>> {nome_dado.capitalize()} Cadastradas <<<")
        for dado in lista:
            if opcao.lower() == "disciplinas":
                print("Código:", dado["Código"])
                print("Nome:", dado["Nome"])
                print("-----------------------------")
            elif opcao.lower() == "turmas":
                print("Código:", dado["Código"])
                print("Nome:", dado["Nome"])
                print("-----------------------------")
            elif opcao.lower() == "matrículas":
                print("Código:", dado["Código"])
                print("Nome:", dado["Nome"])
                print("-----------------------------")
    else:
        print("opão invalida")
    return True



def editar_dado(lista, nome_dado):
    if opcao.lower() in "disciplinas turmas matrículas":
        if opcao.lower() == "disciplinas":
            codigo = int(input(f"Digite o código da {nome_dado.lower()} que deseja editar: "))
            lista = ler_arquivo(arquivo_disciplina)
            for dado in lista:
                if dado["Código"] == codigo:
                    nome = input(f"Digite o novo nome da {nome_dado.lower()}: ")

                    dado["Nome"] = nome

                    print(f"{nome_dado} editada com sucesso!")
                    salvar_arq(lista, arquivo_disciplina)
                    return
        elif opcao.lower() == "turmas":
            codigo = int(input(f"Digite o código da {nome_dado.lower()} que deseja editar: "))
            lista = ler_arquivo(arquivo_turma)
            for dado in lista:
                if dado["Código"] == codigo:
                    nome = input(f"Digite o novo nome da {nome_dado.lower()}: ")

                    dado["Nome"] = nome

                    print(f"{nome_dado} editada com sucesso!")
                    salvar_arq(lista, arquivo_turma)
                    return
        elif opcao.lower() == "matrículas":
            codigo = int(input(f"Digite o código da {nome_dado.lower()} que deseja editar: "))
            lista = ler_arquivo(arquivo_matricula)
            for dado in lista:
                if dado["Código"] == codigo:
                    nome = input(f"Digite o novo nome da {nome_dado.lower()}: ")

                    dado["Nome"] = nome

                    print(f"{nome_dado} editada com sucesso!")
                    salvar_arq(lista, arquivo_matricula)
                    return
    print(f"{nome_dado} não encontrado!")


def excluir_dado(lista, nome_dado):
    if opcao.lower() in "disciplinas turmas matrículas":
        if opcao.lower() == "disciplinas":
            codigo = int(input(f"Digite o código da {nome_dado.lower()} que deseja excluir: "))
            lista = ler_arquivo(arquivo_disciplina)
            for dado in lista:
                if dado["Código"] == codigo:
                    lista.remove(dado)
                    print(f"{nome_dado} excluída com sucesso!")
                    salvar_arq(lista, arquivo_disciplina)
                    return
        elif opcao.lower() == "turmas":
            codigo = int(input(f"Digite o código da {nome_dado.lower()} que deseja excluir: "))
            lista = ler_arquivo(arquivo_turma)
            for dado in lista:
                if dado["Código"] == codigo:
                    lista.remove(dado)
                    print(f"{nome_dado} excluída com sucesso!")
                    salvar_arq(lista, arquivo_turma)
                    return
        elif opcao.lower() == "matrículas":
            codigo = int(input(f"Digite o código da {nome_dado.lower()} que deseja excluir: "))
            lista = ler_arquivo(arquivo_matricula)
            for dado in lista:
                if dado["Código"] == codigo:
                    lista.remove(dado)
                    print(f"{nome_dado} excluída com sucesso!")
                    salvar_arq(lista, arquivo_matricula)
                    return
    print(f"{nome_dado} não encontrado!")



#Funções de salvar os arquivos em Json
def salvar_arq(lista, nome_arquivo):
    with open(nome_arquivo, "w", encoding='utf-8') as arquivo_aberto:
        json.dump(lista, arquivo_aberto, ensure_ascii=False)


#Funções para ler os arquivos em Json
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding='utf-8') as arquivo_aberto:
            lista = json.load(arquivo_aberto)

        return lista
    except:
        return []


#Listas Json
arquivo_estudante = "estudante.json"
arquivo_professor = "professor.json"
arquivo_disciplina = "disciplina.json"
arquivo_turma = "turma.json"
arquivo_matricula = "matricula.json"


#Função para chamar o menu operacional
def acionar_menu_operacional(opcao):
    while True:
        escolha = mostrar_menu_operacoes(opcao)
        if escolha.lower() == "incluir":
            if opcao.lower() in ("estudantes", "professores"):
                cadastrar_pessoa(lista_estudantes if opcao.lower() == "estudantes" else lista_professores, opcao)
            elif opcao.lower() in ("disciplinas", "turmas", "matrículas"):
                cadastrar_dado(lista_disciplinas if opcao.lower() == "disciplinas" else
                               lista_turmas if opcao.lower() == "turmas" else lista_matriculas, opcao[:-1])
        elif escolha.lower() == "listar":
            if opcao.lower() in ("estudantes", "professores"):
                if not listar_pessoas(lista_estudantes if opcao.lower() == "estudantes" else lista_professores, opcao):
                    break

            elif opcao.lower() in ("disciplinas", "turmas", "matrículas"):
                listar_dado(lista_disciplinas if opcao.lower() == "disciplinas" else
                             lista_turmas if opcao.lower() == "turmas" else lista_matriculas, opcao[:-1])
        elif escolha.lower() == "atualizar":
            if opcao.lower() in ("estudantes", "professores"):
                editar_pessoa(lista_estudantes if opcao.lower() == "estudantes" else lista_professores, opcao)
            elif opcao.lower() in ("disciplinas", "turmas", "matrículas"):
                editar_dado(lista_disciplinas if opcao.lower() == "disciplinas" else
                            lista_turmas if opcao.lower() == "turmas" else lista_matriculas, opcao[:-1])
        elif escolha.lower() == "excluir":
            if opcao.lower() in ("estudantes", "professores"):
                excluir_pessoa(lista_estudantes if opcao.lower() == "estudantes" else lista_professores, opcao)
            elif opcao.lower() in ("disciplinas", "turmas", "matrículas"):
                excluir_dado(lista_disciplinas if opcao.lower() == "disciplinas" else
                             lista_turmas if opcao.lower() == "turmas" else lista_matriculas, opcao[:-1])
        elif escolha == "0":
            return False
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")


# Programa principal:
while True:
    opcao = mostrar_menu_principal()

    if opcao.lower() in ("estudantes", "professores", "disciplinas", "turmas", "matrículas"):
        print(f"Você escolheu a opção {opcao}")

        while True:
            if not acionar_menu_operacional(opcao):
                break

    elif opcao.lower() == "sair":
        print("Até a próxima!")
        break
    else:
        print("Opção inválida! Por favor, escolha uma opção válida.")
