#Turma: 2° INFORMÁTICA - VESPERTINO
#Alunos: BEATRIZ, MARIA EDUARDA, GUSTAVO EMANUEL, YURI RAMALHO

#iniciar_sistema
from inicio import *
from cadastrar import *
import os
import time
import itertools
import random

def bloco_de_excessao(norma):
  while True:
    try:
        norma
        break
    except:
      print('Algum valor digitado não corresponde...')

opcao = 0

while opcao != 2:
  exibir_tela_inicial()
  while True:
    try:
      opcao = int(input("Selecione uma opção: "))
      break
    except:
       print('Valores não correspondem, digite novamente...')
  if opcao == 1:
    time.sleep(2)
    os.system('cls')
    iniciar_jogo()
    time.sleep(2)
    os.system('cls')
    break

  elif opcao == 2:
    print("Saindo...")
    exit()
  else:
    print("Opção inválida. Por favor, selecione novamente.")
#iniciar_sistema
print('Iniciando com um cadastro básico...\n')
while True:
  try:
    nome_usuario = input("Digite o nome: ")
    idade_usuario = int(input("Digite a idade: "))
    sexo_usuario = input("Digite o sexo: ")
    id_usuario = int(input("Digite o ID de usuário: "))
    senha_usuario = int(input("Digite a senha: "))
    print('')
    atleta_usuario = Usuario(nome_usuario, idade_usuario, sexo_usuario, id_usuario, senha_usuario)
    Usuario.cadastrar(atleta_usuario)
    Usuario.verificarLogin(atleta_usuario)
    break
  except ValueError:
    print('Valores não correspondem, digite novamente...')

while True:
  try:
    t_Usuario = int(input("Qual é o seu tipo de usuário:\n[1] Atleta\n[2] Professor(a)\n[3] Líder\n"))
    break
  except:
      print('Valores não correspondem, digite novamente...')

if t_Usuario == 1:
    perg1 = int(input("Deseja continuar:\n[1] Sim\n[2] Não\n"))
    if perg1 == 1:
        while True:
          try:
            ano = int(input("Digite o ano da turma: "))
            curso = input("Digite o curso da turma: ")
            turno = input("Digite o turno da turma: ")
            n_camisa = input('Digite o número da sua camisa: ')
            atleta = Atleta(nome_usuario, idade_usuario, sexo_usuario, id_usuario, senha_usuario, ano, turno, curso, n_camisa)
            atleta.cadastrarAtleta()
            print('')
            atleta.exibirAtletas()
            break
          except:
            print("Algum valor não corresponde com as normas do programa...")
elif t_Usuario == 2:
    
    perg1 = int(input("Deseja continuar:\n[1] Sim\n[2] Não\n"))
    if perg1 == 1:
        n_atletas = int(input('Deseja cadastrar quantos atletas: '))
        if n_atletas > 1:
            nome_equipe = input('Nome da equipe que está sendo cadastrada: ')
            tamanho_equipe = n_atletas
            atletas = []
            for i in range(n_atletas):
              print(f'Cadastro do {i+1}° atleta:\n')
              nome_atleta = input("Digite o nome: ")
              idade_atleta = int(input("Digite a idade: "))
              sexo_atleta = input("Digite o sexo: ")
              id_atleta = int(input("Digite o ID de usuário: "))
              senha_atleta = int(input("Digite a senha: "))
              ano = int(input("Digite o ano da turma: "))
              curso_atleta = input("Digite o curso da turma: ")
              turno_atleta = input("Digite o turno da turma: ")
              n_camisa_atleta = int(input('Digite o número da sua camisa: '))
              atleta = Atleta(nome_atleta, idade_atleta, sexo_atleta, id_atleta, senha_atleta, ano, turno_atleta, curso_atleta, n_camisa_atleta)
              atletas.append(atleta)
              atleta.cadastrarAtleta()
            equipe = Equipe(f"{nome_equipe}")
            equipe.atletas.extend(atletas)
            equipe.escolherAtletasEFormarEquipe(equipe.atletas, tamanho_equipe)
            print("Equipes formadas:")
            for i, equipe in enumerate(equipe.equipes, start=1):
                print(f"Equipe {i}: {equipe}")
        else:
              print('Cadastro único:')
              nome_atleta = input("Digite o nome: ")
              idade_atleta = int(input("Digite a idade: "))
              sexo_atleta = input("Digite o sexo: ")
              id_atleta = int(input("Digite o ID de usuário: "))
              senha_atleta = int(input("Digite a senha: "))
              ano = int(input("Digite o ano da turma: "))
              curso_atleta = input("Digite o curso da turma: ")
              turno_atleta = input("Digite o turno da turma: ")
              n_camisa_atleta = int(input('Digite o número da sua camisa: '))
              atleta = Atleta(nome_atleta, idade_atleta, sexo_atleta, id_atleta, senha_atleta, ano, turno_atleta, curso_atleta, n_camisa_atleta)
              atleta.cadastrarAtleta()
              print('')
              atleta.exibirAtletas()

elif t_Usuario == 3:
    perg1 = int(input("Deseja continuar:\n[1] Sim\n[2] Não\n"))
    if perg1 == 1:
        n_atletas = int(input('Deseja cadastrar quantos atletas: '))
        if n_atletas > 1:
            nome_equipe = input('Nome da equipe que está sendo cadastrada: ')
            tamanho_equipe = n_atletas
            atletas = []
            for i in range(n_atletas):
              print(f'Cadastro do {i+1}° atleta:\n')
              nome_atleta = input("Digite o nome: ")
              idade_atleta = int(input("Digite a idade: "))
              sexo_atleta = input("Digite o sexo: ")
              id_atleta = int(input("Digite o ID de usuário: "))
              senha_atleta = int(input("Digite a senha: "))
              ano = int(input("Digite o ano da turma: "))
              curso_atleta = input("Digite o curso da turma: ")
              turno_atleta = input("Digite o turno da turma: ")
              n_camisa_atleta = int(input('Digite o número da sua camisa: '))
              atleta = Atleta(nome_atleta, idade_atleta, sexo_atleta, id_atleta, senha_atleta, ano, turno_atleta, curso_atleta, n_camisa_atleta)
              atletas.append(atleta)
              atleta.cadastrarAtleta()
            equipe = Equipe(f"{nome_equipe}")
            equipe.atletas.extend(atletas)
            equipe.escolherAtletasEFormarEquipe(equipe.atletas, tamanho_equipe)
            print("Equipes formadas:")
            for i, equipe in enumerate(equipe.equipes, start=1):
                print(f"Equipe {i}: {equipe}")
        else:
              print('Cadastro único:')
              nome_atleta = input("Digite o nome: ")
              idade_atleta = int(input("Digite a idade: "))
              sexo_atleta = input("Digite o sexo: ")
              id_atleta = int(input("Digite o ID de usuário: "))
              senha_atleta = input("Digite a senha: ")
              ano = int(input("Digite o ano da turma: "))
              curso_atleta = input("Digite o curso da turma: ")
              turno_atleta = input("Digite o turno da turma: ")
              n_camisa_atleta = int(input('Digite o número da sua camisa: '))
              atleta = Atleta(nome_atleta, idade_atleta, sexo_atleta, id_atleta, senha_atleta, ano, turno_atleta, curso_atleta, n_camisa_atleta)
              atleta.cadastrarAtleta()
              print('')
              atleta.exibirAtletas()
    
                

else:
    print("Opção inválida.")