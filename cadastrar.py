import time
import json

class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo 

    def exibir_informacoes(self):
        atributos = (
            '\n' + f"Nome: {'':<20}" + f"{str(self.nome):>15}",
            '\n' + f"Idade: {'':<20}" + f"{str(self.idade):>15}",
            '\n' + f"Sexo: {'':<20}" + f"{str(self.sexo):>15}"
        )

        for ch in atributos:
          time.sleep(0.1)
          print(ch, end='', flush=True)



class Usuario(Pessoa):
    def __init__(self, nome, idade, sexo, idUsuario, senhaId):
        super().__init__(nome, idade, sexo)
        self.idUsuario = idUsuario
        self.senhaId = senhaId
    
    def cadastrar(self):
        try:
            with open('usuarios.txt', 'a') as file:
                file.write(f"Nome: {self.nome}\n")
                file.write(f"Idade: {self.idade}\n")
                file.write(f"Sexo: {self.sexo}\n")
                file.write(f"ID de Usuário: {self.idUsuario}\n")
                file.write(f"Senha: {self.senhaId}\n")
                file.write("\n")
        except Exception as Valor_nao_correspondido:
            print(f"Erro ao cadastrar usuário: {Valor_nao_correspondido}")
        finally:
            print("Operação de cadastro concluída.")

    def verificarLogin(self):
        try:
            with open('usuarios.txt', 'r') as file:
                lines = file.readlines()

            idUsuario = f"ID de Usuário: {self.idUsuario}\n"
            senha = f"Senha: {self.senhaId}\n"

            if idUsuario in lines and senha in lines:
                print("Login bem-sucedido! Usuário autenticado.")
            else:
                print("Login falhou. ID de usuário ou senha incorretos.")
        except Exception as Valor_nao_correspondido:
            print(f"Erro ao verificar login: {Valor_nao_correspondido}")
        finally:
            print("Operação de verificação de login concluída.")


class Atleta(Usuario):
    def __init__(self, nome, idade, sexo, idUsuario, senhaId, ano, turno, curso, numeroCamisa):
        super().__init__(nome, idade, sexo, idUsuario, senhaId)
        self.ano = ano 
        self.turno = turno 
        self.curso = curso
        self.numeroCamisa = numeroCamisa

    def cadastrarAtleta(self):
          with open('atleta.txt', 'a') as file:
            file.write(f"Nome: {self.nome}\n")
            file.write(f"Idade: {self.idade}\n")
            file.write(f"Sexo: {self.sexo}\n")
            file.write(f"Ano: {self.ano}\n")
            file.write(f"Curso: {self.curso}\n")
            file.write(f"Turno: {self.turno}\n")
            file.write(f"Camisa: {self.numeroCamisa}\n")
            file.write("\n")


    def exibirAtletas(self):
        try:
            with open('atleta.txt', 'r') as file:
                atletas_info = file.read().split("\n\n")

            for atleta_info in atletas_info:
                if atleta_info.strip():
                    atributos = atleta_info.split("\n")
                    print("Informações do Atleta:")
                    for atributo in atributos:
                        print(atributo)
                    print()
        except FileNotFoundError as Valor_nao_correspondido:
            print(f"Arquivo de atletas não encontrado: {Valor_nao_correspondido}")
        except Exception as Valor_nao_correspondido:
            print(f"Erro ao exibir atletas: {Valor_nao_correspondido}")
        finally:
            print("Operação de exibição de atletas concluída.")
    
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Sexo: {self.sexo}, ID: {self.id_usuario}, Ano: {self.ano}, Turno: {self.turno}, Curso: {self.curso}, Número da Camisa: {self.n_camisa}"


class Professor(Usuario):
    def __init__(self,idUsuario, disciplina):
        super().__init__(idUsuario)
        self.disciplina = disciplina

    def cadastrarAtleta(self, nome, idade, sexo, idUsuario, senhaId, ano, turno, curso, numeroCamisa):
        novo_atleta = Atleta(nome, idade, sexo, idUsuario, senhaId, ano, turno, curso, numeroCamisa)
        novo_atleta.cadastrarAtleta()
    



class Lider(Usuario):
    def __init__(self, idUsuario, senhaId):
        super().__init__(idUsuario, senhaId)

    def cadastrarAtleta(self, nome, idade, sexo, idUsuario, senhaId, ano, turno, curso, numeroCamisa):
      novo_atleta = Atleta(nome, idade, sexo, idUsuario, senhaId, ano, turno, curso, numeroCamisa)
      novo_atleta.cadastrarAtleta()

  
class Equipe:
    def __init__(self, nomeEquipe):
        self.nomeEquipe = nomeEquipe
        self.atletas = []
        self.modalidades = []
        self.equipes = []

    arquivo = 'atleta.txt'

    def carregarAtletas(self, arquivo):
        try:
            with open(arquivo, 'r') as file:
                atletas_info = file.read().split("\n\n")

            for atleta_info in atletas_info:
                if atleta_info.strip():
                    atributos = atleta_info.split("\n")
                    atleta = {}
                    for atributo in atributos:
                        try:
                            key, value = atributo.split(": ")
                            atleta[key] = value
                        except ValueError as Valor_nao_correspondido:
                            print(f"Erro ao ler o arquivo: {Valor_nao_correspondido}")
                    self.atletas.append(atleta)
        except FileNotFoundError as Valor_nao_correspondido:
            print(f"Arquivo não encontrado: {Valor_nao_correspondido}")

    def carregarModalidades(self, arquivo):
        try:
            with open(arquivo, 'r') as file:
                modalidades_data = json.load(file)
                self.modalidades = modalidades_data
        except FileNotFoundError as Valor_nao_correspondido:
            print(f"Arquivo de modalidades não encontrado: {Valor_nao_correspondido}")
        except Exception as Valor_nao_correspondido:
            print(f"Erro ao carregar modalidades: {Valor_nao_correspondido}")
        finally:
            print("Operação de carregamento de modalidades concluída.")

    def carregarModalidades(self, arquivo):
      try:
        with open(arquivo, 'r') as file:
            modalidades_data = json.load(file)
            self.modalidades = modalidades_data
      except FileNotFoundError as Valor_nao_correspondido:
        print("Arquivo de modalidades não encontrado:{Valor_nao_correspondido}")

    def exibirModalidades(self):
        print("Modalidades:")
        for modalidade in self.modalidades:
            print(f"Nome: {modalidade['nome_modalidade']}")
            print(f"Descrição: {modalidade['descricao']}")
            print(f"Regras: {modalidade['regras']}\n")

    def escolherAtletasEFormarEquipe(self, atletas, tamanho_equipe):
        for i in range(0, len(atletas), tamanho_equipe):
            equipe = atletas[i:i + tamanho_equipe]
            self.equipes.append(equipe)

    def __str__(self):
        atletas_str = "\n".join(str(atleta) for atleta in self.atletas)
        return f"Nome da Equipe: {self.nome}\nAtletas:\n{atletas_str}"




class Modalidade:
    def __init__(self):
        self.modalidades = []

    def exibirModalidades(self, modalidades):
          with open(modalidades, "r") as file:
                self.modalidades = json.load(file)

          print("Modalidades:")
          for modalidade in self.modalidades:
              print(f"Nome: {modalidade['nome_modalidade']}")
              print(f"Descrição: {modalidade['descricao']}")
              print(f"Regras: {modalidade['regras']}\n")