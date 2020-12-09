import os
import sys
import random
import json
import pickle
from datetime import timedelta, date

class Emprestimo:
  def __init__ (self, idMembro, livro, dataEmprestimo, dataDevolucao):
    self.id = idMembro
    self.livro = livro
    self.dataEmprestimo = dataEmprestimo
    self.dataDevolucao = dataDevolucao

  def getID(self):
    return self.id

  def getISBN(self):
    return self.ISBN

  def getDataEmprestimo(self):
    return self.dataEmprestimo

  def getDataDevolucao(self):
    return self.dataDevolucao

  def getRecibo(self):
    print('-=' * 16)
    print('RECIBO')
    print('ID: ', self.id)
    print('Data de Empréstimo: ', self.dataEmprestimo.strftime('%d/%m/%Y'))
    print('Data de Devolução: ', (self.dataDevolucao).strftime('%d/%m/%Y'))
    print(f'Livro -- Título: {self.livro.getTitulo()}, gênero: {self.livro.getGenero()}, ISBN: {self.livro.getISBN()} e Autor: {self.livro.getAutor()}')
    print('Obs: Haverá uma multa de R$ 2 para cada dia de atraso na devolução!')

class Conta:
  def __init__ (self, nome, idConta, senha):
    self.nome = nome
    self.idConta = idConta
    self.senha = senha

  def setNome(self, nome):
    self.nome = nome

  def setSenha(self, senha):
    self.senha = senha

  def getNome(self):
    return self.nome

  def getId(self):
    return self.idConta

class Livro:
  def __init__ (self, quantidade ,titulo, genero, isbn, autor):
    self.quantidade = quantidade
    self.titulo = titulo
    self.genero = genero
    self.isbn = isbn
    self.autor = autor

  def setQuantidade(self, quantidade):
    self.quantidade += quantidade

  def setTitulo(self, titulo):
    self.titulo = titulo

  def setGenero(self, genero):
    self.genero = genero

  def setISBN(self, isbn):
    self.isbn = isbn

  def setAutor(self, autor):
    self.autor = autor

  def getQuantidade(self):
    return self.quantidade

  def getTitulo(self):
    return self.titulo

  def getGenero(self):
    return self.genero

  def getISBN(self):
    return self.isbn

  def getAutor(self):
    return self.autor

class Membro(Conta):
  def __init__ (self, nome, idade, endereco, cpf, idConta, senha):
    super().__init__(nome, idConta, senha)
    self.idade = idade
    self.endereco = endereco
    self.cpf = cpf

  def setIdade(self, idade):
    self.idade = idade

  def setEndereco(self, endereco):
    self.endereco = endereco

  def setCpf(self, cpf):
    self.cpf = cpf

  def getIdade(self):
    return self.idade

  def getEndereco(self):
    return self.endereco

  def getCpf(self):
    return self.cpf

class Bibliotecario(Conta):
  def __init__ (self, nome, turno, cpf, idConta, senha):
    super().__init__(nome, idConta, senha)
    self.turno = turno
    self.cpf = cpf

  def setCpf(self, cpf):
    self.cpf = cpf

  def setTurno(self, turno):
    self.turno = turno

  def getCpf(self):
    return self.cpf

  def getTurno(self):
    return self.turno

class Administrador(Conta):
  def __init__(self, idConta, senha, nome, telefone):
    super().__init__(nome, idConta, senha)
    self.telefone = telefone

  def setId(self, idConta):
    self.idConta = idConta

  def setTelefone(self, telefone):
    self.telefone = telefone

  def getTelefone(self):
    return self.telefone

class Biblioteca():
  def __init__ (self, nome, endereco, telefone):
    self.nome = nome
    self.endereco = endereco
    self.telefone = telefone
  
  def setNome(self, nome):
    self.nome = nome

  def setEndereco(self, endereco):
    self.endereco = endereco

  def setTelefone(self, telefone):
    self.telefone = telefone
  
  def getNome(self):
    return self.nome

  def getEndereco(self):
    return self.endereco

  def getTelefone(self):
    return self.telefone

if (os.stat('path/arquivosExternos/idAdministrador.json').st_size == 0) != True:
  with open('path/arquivosExternos/idAdministrador.json', 'r') as file:
    idAdministrador = json.load(file)
else:
  idAdministrador = 'admin'

if (os.stat('path/arquivosExternos/senhaAdministrador.json').st_size == 0) != True:
  with open('path/arquivosExternos/senhaAdministrador.json', 'r') as file:
    senhaAdministrador = json.load(file)
else:
  senhaAdministrador = '123'

if (os.stat('path/arquivosExternos/listaIdBibliotecarios.json').st_size == 0) != True:
  with open('path/arquivosExternos/listaIdBibliotecarios.json', 'r') as file:
    listaIdBibliotecario = json.load(file)
else:
  listaIdBibliotecario = []

if (os.stat('path/arquivosExternos/listaSenhaBibliotecarios.json').st_size == 0) != True:
  with open('path/arquivosExternos/listaSenhaBibliotecarios.json', 'r') as file:
    listaSenhaBibliotecario = json.load(file)
else:
  listaSenhaBibliotecario = []

try:
  with open('path/arquivosExternos/listaBibliotecarios.pickle', 'rb') as i:
    listaBibliotecarios = pickle.load(i)
except EOFError:
    listaBibliotecarios = []

if (os.stat('path/arquivosExternos/listaCpfBibliotecarios.json').st_size == 0) != True:
  with open('path/arquivosExternos/listaCpfBibliotecarios.json', 'r') as file:
    listaCpfBibliotecarios = json.load(file)
else:
  listaCpfBibliotecarios = []

try:
  with open('path/arquivosExternos/listaMembros.pickle', 'rb') as i:
    listaMembros = pickle.load(i)
except EOFError:
    listaMembros = []

if (os.stat('path/arquivosExternos/listaIdMembros.json').st_size == 0) != True:
  with open('path/arquivosExternos/listaIdMembros.json', 'r') as file:
    listaIdMembro = json.load(file)
else:
  listaIdMembro = []

if (os.stat('path/arquivosExternos/listaSenhaMembros.json').st_size == 0) != True:
  with open('path/arquivosExternos/listaSenhaMembros.json', 'r') as file:
    listaSenhaMembro = json.load(file)
else:
  listaSenhaMembro = []

try:
  with open('path/arquivosExternos/listaLivros.pickle', 'rb') as i:
      listaLivros = pickle.load(i)
except EOFError:
      listaLivros = []

if (os.stat('path/arquivosExternos/listaTitulos.json').st_size == 0) != True:
  with open('path/arquivosExternos/listaTitulos.json', 'r') as file:
    listaTitulos = json.load(file)
else:
  listaTitulos = []

if (os.stat('path/arquivosExternos/listaISBN.json').st_size == 0) != True:
  with open('path/arquivosExternos/listaISBN.json', 'r') as file:
    listaISBN = json.load(file)
else:
  listaISBN = []

try:
  with open('path/arquivosExternos/listaLivrosEmprestados.pickle', 'rb') as i:
    listaLivrosEmprestados = pickle.load(i)
except EOFError:
    listaLivrosEmprestados = []

try:
  with open('path/arquivosExternos/administrador.pickle', 'rb') as i:
    administrador = pickle.load(i)
except EOFError:
    administrador = Administrador('admin', '123', 'Nome Admin', '01 01010101')

try:
  with open('path/arquivosExternos/biblioteca.pickle', 'rb') as i:
    biblioteca = pickle.load(i)
except EOFError:
    biblioteca = Biblioteca('Biblioteca Central', 'Rua da Biblioteca', '10 10101010')

def atualizaIdAdmin():
  with open('path/arquivosExternos/IdAdministrador.json', 'w') as file:
    json.dump(idAdministrador, file, indent = 2)

def atualizaSenhaAdmin():
  with open('path/arquivosExternos/SenhaAdministrador.json', 'w') as file:
    json.dump(senhaAdministrador, file, indent = 2)

def atualizaAdmin():
  with open('path/arquivosExternos/administrador.pickle', 'wb') as output:
    pickle.dump(administrador, output, pickle.HIGHEST_PROTOCOL)

def atualizaBiblioteca():
  with open('path/arquivosExternos/biblioteca.pickle', 'wb') as output:
    pickle.dump(biblioteca, output, pickle.HIGHEST_PROTOCOL)

def atualizaListaIdBibliotecarios():
  with open('path/arquivosExternos/listaIdBibliotecarios.json', 'w') as file:
    json.dump(listaIdBibliotecario, file, indent = 2)

def atualizaListaSenhaBibliotecarios():
  with open('path/arquivosExternos/listaSenhaBibliotecarios.json', 'w') as file:
    json.dump(listaSenhaBibliotecario, file, indent = 2)

def atualizaListaBibliotecarios():
  with open('path/arquivosExternos/listaBibliotecarios.pickle', 'wb') as output:
    pickle.dump(listaBibliotecarios, output, pickle.HIGHEST_PROTOCOL)

def atualizaListaCpfBibliotecarios():
  with open('path/arquivosExternos/listaCpfBibliotecarios.json', 'w') as file:
    json.dump(listaCpfBibliotecarios, file, indent = 2)

def atualizaListaMembros():
  with open('path/arquivosExternos/listaMembros.pickle', 'wb') as output:
    pickle.dump(listaMembros, output, pickle.HIGHEST_PROTOCOL)

def atualizaListaIdMembros():
  with open('path/arquivosExternos/listaIdMembros.json', 'w') as file:
    json.dump(listaIdMembro, file, indent = 2)

def atualizaListaSenhaMembros():
  with open('path/arquivosExternos/listaSenhaMembros.json', 'w') as file:
    json.dump(listaSenhaMembro, file, indent = 2)

def atualizaListaLivros():
  with open('path/arquivosExternos/listaLivros.pickle', 'wb') as output:
    pickle.dump(listaLivros, output, pickle.HIGHEST_PROTOCOL)

def atualizaListaTitulos():
  with open('path/arquivosExternos/listaTitulos.json', 'w') as file:
    json.dump(listaTitulos, file, indent = 2)

def atualizaListaISBN():
  with open('path/arquivosExternos/listaISBN.json', 'w') as file:
    json.dump(listaISBN, file, indent = 2)

def atualizaListaLivrosEmprestados():
  with open('path/arquivosExternos/listaLivrosEmprestados.pickle', 'wb') as output:
    pickle.dump(listaLivrosEmprestados, output, pickle.HIGHEST_PROTOCOL)

def validacaoLogin(tipo, idInput, senha):
  valido = False

  if tipo == 1: # bibliotecário

    if idInput not in listaIdBibliotecario:
      valido = False
    else:
      indice = listaIdBibliotecario.index(idInput)

      if (listaIdBibliotecario[indice] == idInput) and (listaSenhaBibliotecario[indice] == senha):
        valido = True

  elif tipo == 2: # membro

    if idInput not in listaIdMembro:
      valido = False
    else:
      indice = listaIdMembro.index(idInput)

      if (listaIdMembro[indice] == idInput) and (listaSenhaMembro[indice] == senha):
        valido = True

  elif tipo == 3: # administrador
    if senha == senhaAdministrador and idInput == idAdministrador:
      valido = True

  return valido

def login(opcao):
  header()

  valido = False

  while valido == False:

    header()

    idInput = input('\n[0 - Menu] Digite o seu id: ')

    if idInput == '0':
      menuPrincipal()

    senhaInput = input('[0 - Menu] Digite a sua senha: ')

    if senhaInput == '0':
      menuPrincipal()

    if opcao == 1: # bibliotecário
      valido = validacaoLogin(opcao, idInput, senhaInput)
    elif opcao == 2: # membro
      valido = validacaoLogin(opcao, idInput, senhaInput)
    else: # administrador
      valido = validacaoLogin(opcao, idInput, senhaInput)

  return idInput

def header():
  os.system('cls' if os.name == 'nt' else 'clear')
  
  print('-=' * 60)
  print('\t\t\t\t\t\tGERENCIADOR DE BIBLIOTECA')
  print('-=' * 60)

def menuBibliotecario(idConta):
  opcao = 0

  while opcao < 1 or opcao > 11:

      header()

      print('\n1 - Adicionar livro')
      print('2 - Remover livro')
      print('3 - Editar livro')
      print('4 - Verificar membros')
      print('5 - Registrar novo membro')
      print('6 - Editar Membro')
      print('7 - Remover membro')
      print('8 - Pesquisar livros')
      print('9 - Verificar livros emprestados')
      print('10 - Alterar senha')
      print('11 - Retornar ao menu')

      opcao = int(input('\nDigite uma opção: '))
        
  if opcao == 1:
    
    header()

    print('\n**Menu - Adicionar Livro**\n')

    titulo = input('[0 - Menu] Digite o título do livro: ').upper()

    if titulo == '0':
      menuBibliotecario(idConta)

    genero = input('[0 - Menu] Digite o gênero do livro: ').upper()

    if genero == '0':
      menuBibliotecario(idConta)

    isbn = input('[0 - Menu] Digite o ISBN do livro: ')

    if isbn == '0':
      menuBibliotecario(idConta)

    autor = input('[0 - Menu] Digite o nome do autor: ').upper()

    if autor == '0':
      menuBibliotecario(idConta)

    quantidadeInvalida = True

    while quantidadeInvalida == True:

      quantidade = int(input('[0 - Menu] Digite a quantidade de livros: '))

      if quantidade == 0:
        menuBibliotecario(idConta)

      if quantidade > 0:
        quantidadeInvalida = False

    livroEncontrado = False

    for livro in listaLivros:
      if isbn == livro.getISBN():
        indice = listaLivros.index(livro)
        livroEncontrado = True
    
    if livroEncontrado == True:

      header()

      print('\n**Menu - Adicionar Livro**\n')

      print('-=' * 16)
      print('Título: ', listaLivros[indice].getTitulo())
      print('Gênero: ', listaLivros[indice].getGenero())
      print('ISBN: ', listaLivros[indice].getISBN())
      print('Autor: ', listaLivros[indice].getAutor())
      print('Quantidade: ', listaLivros[indice].getQuantidade())
      print('-=' * 16)

      opcao = ''

      while opcao != '1' and opcao != '2':

        opcao = input('\n[1 - Sim | 2 - Não] O livro já existe na biblioteca, deseja adicionar mais unidades ? ')

      if opcao == '1':
  
        header()

        print('\n**Menu - Adicionar Livro**\n')

        print('-=' * 16)
        print('Título: ', listaLivros[indice].getTitulo())
        print('Gênero: ', listaLivros[indice].getGenero())
        print('ISBN: ', listaLivros[indice].getISBN())
        print('Autor: ', listaLivros[indice].getAutor())
        print('Quantidade: ', listaLivros[indice].getQuantidade())
        print('-=' * 16)

        quantidade = -1

        while quantidade < 0:

          quantidade = int(input('\n[0 - Menu] Digite quantas unidades deseja adicionar: '))

          if quantidade == 0:
            menuBibliotecario(idConta)

          listaLivros[indice].setQuantidade(quantidade)
          print('-=' * 16)
          print('Título: ', listaLivros[indice].getTitulo())
          print('Gênero: ', listaLivros[indice].getGenero())
          print('ISBN: ', listaLivros[indice].getISBN())
          print('Autor: ', listaLivros[indice].getAutor())
          print('Quantidade: ', listaLivros[indice].getQuantidade())
          print('-=' * 16)

        atualizaListaLivros()

        header()

        print('\n**Menu - Adicionar Livro**\n')

        print('Quantidade adicionada!')

        print('-=' * 16)
        print('Título: ', listaLivros[indice].getTitulo())
        print('Gênero: ', listaLivros[indice].getGenero())
        print('ISBN: ', listaLivros[indice].getISBN())
        print('Autor: ', listaLivros[indice].getAutor())
        print('Quantidade: ', listaLivros[indice].getQuantidade())
        print('-=' * 16)

        opcao = ''

        while opcao != '1':

          opcao = input('\nDigite 1 para retornar ao menu: ')

        menuBibliotecario(idConta)

      else:
        menuBibliotecario(idConta)

    else:
      umLivro = Livro(quantidade, titulo, genero, isbn, autor)

      listaTitulos.append(titulo)

      atualizaListaTitulos()

      listaISBN.append(isbn)

      atualizaListaISBN()

      listaLivros.append(umLivro)

      atualizaListaLivros()

      indiceLivro = len(listaTitulos) - 1

    header()

    print('\n**Menu - Adicionar Livro**\n')

    print('Livro Adicionado!')

    print('-=' * 16)
    print('Título: ', listaLivros[indiceLivro].getTitulo())
    print('Gênero: ', listaLivros[indiceLivro].getGenero())
    print('ISBN: ', listaLivros[indiceLivro].getISBN())
    print('Autor: ', listaLivros[indiceLivro].getAutor())
    print('Quantidade: ', listaLivros[indiceLivro].getQuantidade())
    print('-=' * 16)

    opcao = ''

    while opcao != '1':
      opcao = input('\nDigite 1 para retornar ao menu: ')   

    menuBibliotecario(idConta)

  elif opcao == 2:

    opcao = 0
    
    while opcao < 1 or opcao > 3:

      header()
      print('\n**Menu - Remover livro**\n')

      print('1 - Remover livro utilizando título')
      print('2 - Remover livro utilizando ISBN')
      print('3 - Retornar ao menu')

      opcao = int(input('\nDigite uma opção: '))

    if opcao == 1:

      livroEncontrado = False

      counter = 0

      while livroEncontrado == False:
  
        header()
        print('\n**Menu - Remover livro**\n')

        if counter >= 1:
          print('Nenhum livro encontrado, tente novamente!\n')

        tituloRemocao = input('[0 - Menu] Digite o título: ').upper()

        if tituloRemocao == '0':
          menuBibliotecario(idConta)

        counter += 1

        for livro in listaLivros:
          if tituloRemocao == livro.getTitulo():
            indiceLivro = listaLivros.index(livro)
            livroEncontrado = True
    
      header()
      print('\n**Menu - Remover livro**\n')

      print('-=' * 16)
      print('Título: ', listaLivros[indiceLivro].getTitulo())
      print('Gênero: ', listaLivros[indiceLivro].getGenero())
      print('ISBN: ', listaLivros[indiceLivro].getISBN())
      print('Autor: ', listaLivros[indiceLivro].getAutor())
      print('Quantidade: ', listaLivros[indiceLivro].getQuantidade())
      print('-=' * 16)

      if listaLivros[indiceLivro].getQuantidade() > 1:
        opcao = 0
        
        while opcao < 1 or opcao > 3:
    
          header()
          print('\n**Menu - Remover livro**\n')

          print('-=' * 16)
          print('Título: ', listaLivros[indiceLivro].getTitulo())
          print('Gênero: ', listaLivros[indiceLivro].getGenero())
          print('ISBN: ', listaLivros[indiceLivro].getISBN())
          print('Autor: ', listaLivros[indiceLivro].getAutor())
          print('Quantidade: ', listaLivros[indiceLivro].getQuantidade())
          print('-=' * 16)

          opcao = int(input('\n[1 - Todas | 2 - Apenas uma | 3 - Menu] Há mais de uma unidade desse livro, deseja remover todas ou apenas uma ? '))

        if opcao == 1:

          opcao = 0

          while opcao < 1 or opcao > 2:
      
            header()
            print('\n**Menu - Remover livro**\n')

            print('-=' * 16)
            print('Título: ', listaLivros[indiceLivro].getTitulo())
            print('Gênero: ', listaLivros[indiceLivro].getGenero())
            print('ISBN: ', listaLivros[indiceLivro].getISBN())
            print('Autor: ', listaLivros[indiceLivro].getAutor())
            print('Quantidade: ', listaLivros[indiceLivro].getQuantidade())
            print('-=' * 16)

            opcao = int(input('\n[1 - Sim | 2 - Não - Menu] Tem certeza de que deseja remover todas as unidades do livro ? '))

          if opcao == 1:
            del listaLivros[indiceLivro]
            del listaTitulos[indiceLivro]
            del listaISBN[indiceLivro]

            atualizaListaLivros()

            atualizaListaTitulos()

            atualizaListaISBN()

            menuBibliotecario(idConta)
  
          else:
            menuBibliotecario(idConta)

        elif opcao == 2:
    
          header()

          print('\n**Menu - Remover livro**\n')

          print('ANTES')
          print('-=' * 16)
          print('Título: ', listaLivros[indiceLivro].getTitulo())
          print('Gênero: ', listaLivros[indiceLivro].getGenero())
          print('ISBN: ', listaLivros[indiceLivro].getISBN())
          print('Autor: ', listaLivros[indiceLivro].getAutor())
          print('Quantidade: ', listaLivros[indiceLivro].getQuantidade())
          print('-=' * 16)

          listaLivros[indiceLivro].setQuantidade(-1)

          atualizaListaLivros()

          print('DEPOIS')
          print('-=' * 16)
          print('Título: ', listaLivros[indiceLivro].getTitulo())
          print('Gênero: ', listaLivros[indiceLivro].getGenero())
          print('ISBN: ', listaLivros[indiceLivro].getISBN())
          print('Autor: ', listaLivros[indiceLivro].getAutor())
          print('Quantidade: ', listaLivros[indiceLivro].getQuantidade())
          print('-=' * 16)

          opcao = 0

          while opcao != 1:
            opcao = int(input('\nDigite 1 para retornar ao menu: '))

          menuBibliotecario(idConta)

        else:
          menuBibliotecario(idConta)

      else:
        opcao = 0

        while opcao < 1 or opcao > 2:
    
          header()
          print('\n**Menu - Remover livro**\n')
          
          print('-=' * 16)
          print('Título: ', livro.getTitulo())
          print('Gênero: ', livro.getGenero())
          print('ISBN: ', livro.getISBN())
          print('Autor: ', livro.getAutor())
          print('Quantidade: ', livro.getQuantidade())
          print('-=' * 16)

          opcao = int(input('\n[1 - Sim | 2 - Não - Menu] Tem certeza de que deseja remover o livro ? '))

        if opcao == 1:
          del listaLivros[indiceLivro]
          del listaTitulos[indiceLivro]
          del listaISBN[indiceLivro]

          atualizaListaLivros()

          atualizaListaTitulos()

          atualizaListaISBN()

          menuBibliotecario(idConta)

        else:
          menuBibliotecario(idConta)

    elif opcao == 2:

      livroEncontrado = False

      while livroEncontrado == False:
  
        header()
        print('\n**Menu - Remover livro**\n')        

        isbnRemocao = input('[0 - Menu] Digite o ISBN: ')

        if isbnRemocao == '0':
          menuBibliotecario(idConta)

        for livro in listaLivros:
          if isbnRemocao == livro.getISBN():
            indiceLivro = listaLivros.index(livro)
            livroEncontrado = True

      header()
      print('\n**Menu - Remover livro**\n')

      print('-=' * 16)
      print('Título: ', listaLivros[indiceLivro].getTitulo())
      print('Gênero: ', listaLivros[indiceLivro].getGenero())
      print('ISBN: ', listaLivros[indiceLivro].getISBN())
      print('Autor: ', listaLivros[indiceLivro].getAutor())
      print('Quantidade: ', listaLivros[indiceLivro].getQuantidade())
      print('-=' * 16)

      if listaLivros[indiceLivro].getQuantidade() > 1:
        opcao = 0
        
        while opcao < 1 or opcao > 3:
    
          header()
          print('\n**Menu - Remover livro**\n')

          print('-=' * 16)
          print('Título: ', listaLivros[indiceLivro].getTitulo())
          print('Gênero: ', listaLivros[indiceLivro].getGenero())
          print('ISBN: ', listaLivros[indiceLivro].getISBN())
          print('Autor: ', listaLivros[indiceLivro].getAutor())
          print('Quantidade: ', listaLivros[indiceLivro].getQuantidade())
          print('-=' * 16)

          opcao = int(input('\n[1 - Todas | 2 - Apenas uma | 3 - Menu] Há mais de uma unidade desse livro, deseja remover todas ou apenas uma ? '))

        if opcao == 1:

          opcao = 0

          while opcao < 1 or opcao > 2:
      
            header()
            print('\n**Menu - Remover livro**\n')

            print('-=' * 16)
            print('Título: ', listaLivros[indiceLivro].getTitulo())
            print('Gênero: ', listaLivros[indiceLivro].getGenero())
            print('ISBN: ', listaLivros[indiceLivro].getISBN())
            print('Autor: ', listaLivros[indiceLivro].getAutor())
            print('Quantidade: ', listaLivros[indiceLivro].getQuantidade())
            print('-=' * 16)

            opcao = int(input('\n[1 - Sim | 2 - Não] Tem certeza de que deseja remover todas as unidades do livro ? '))

          if opcao == 1:

            del listaLivros[indiceLivro]
            del listaTitulos[indiceLivro]
            del listaISBN[indiceLivro]

            atualizaListaLivros()

            atualizaListaTitulos()

            atualizaListaISBN()

            menuBibliotecario(idConta)
  
          else:
            menuBibliotecario(idConta)

        elif opcao == 2:
    
          header()
          print('\n**Menu - Remover livro**\n')

          print('ANTES')
          print('-=' * 16)
          print('Título: ', listaLivros[indiceLivro].getTitulo())
          print('Gênero: ', listaLivros[indiceLivro].getGenero())
          print('ISBN: ', listaLivros[indiceLivro].getISBN())
          print('Autor: ', listaLivros[indiceLivro].getAutor())
          print('Quantidade: ', listaLivros[indiceLivro].getQuantidade())
          print('-=' * 16)

          listaLivros[indiceLivro].setQuantidade(-1)

          atualizaListaLivros()

          print('DEPOIS')
          print('-=' * 16)
          print('Título: ', listaLivros[indiceLivro].getTitulo())
          print('Gênero: ', listaLivros[indiceLivro].getGenero())
          print('ISBN: ', listaLivros[indiceLivro].getISBN())
          print('Autor: ', listaLivros[indiceLivro].getAutor())
          print('Quantidade: ', listaLivros[indiceLivro].getQuantidade())
          print('-=' * 16)

          opcao = ''

          while opcao != '1':
            opcao = input('\nDigite 1 para retornar ao menu: ')

          menuBibliotecario(idConta)

        else:
          menuBibliotecario(idConta)

      else:
        opcao = 0

        while opcao < 1 or opcao > 2:
    
          header()
          print('\n**Menu - Remover livro**\n')

          print('-=' * 16)
          print('Título: ', listaLivros[indiceLivro].getTitulo())
          print('Gênero: ', listaLivros[indiceLivro].getGenero())
          print('ISBN: ', listaLivros[indiceLivro].getISBN())
          print('Autor: ', listaLivros[indiceLivro].getAutor())
          print('Quantidade: ', listaLivros[indiceLivro].getQuantidade())
          print('-=' * 16)

          opcao = int(input('\n[1 - Sim | 2 - Não] Tem certeza de que deseja remover o livro ? '))

        if opcao == 1:
          
          del listaLivros[indiceLivro]
          del listaTitulos[indiceLivro]
          del listaISBN[indiceLivro]

          atualizaListaLivros()

          atualizaListaTitulos()

          atualizaListaISBN()

          menuBibliotecario(idConta)

        else:
          menuBibliotecario(idConta)

    else:
      menuBibliotecario(idConta)

  elif opcao == 3:
    opcao = 0

    while opcao < 1 or opcao > 3:

      header()
      print('\n**Menu - Edição livro**\n')  

      print('1 - Editar livro utilizando atual título')
      print('2 - Editar livro utilizando atual ISBN')
      print('3 - Retornar ao menu')

      opcao = int(input('\nDigite uma opção: '))

    if opcao == 1:
      livroEncontrado = False

      counter = 0

      while livroEncontrado == False:

        header()
        print('\n**Menu - Edição livro**\n')

        if counter >= 1:
          print('Nenhum livro encontrado, tente novamente!\n')

        titulo = input('[0 - Menu] Digite o título: ').upper()

        if titulo == '0':
          menuBibliotecario(idConta)

        counter += 1

        for livro in listaLivros:
          if livro.getTitulo() == titulo:
            indiceLivro = listaLivros.index(livro)
            livroEncontrado = True

      opcao = 0

      while opcao < 1 or opcao > 6:

        header()
        print('\n**Menu - Edição livro**\n')

        print('-=' * 16)
        print('Título: ', listaLivros[indiceLivro].getTitulo())
        print('Gênero: ', listaLivros[indiceLivro].getGenero())
        print('ISBN: ', listaLivros[indiceLivro].getISBN())
        print('Autor: ', listaLivros[indiceLivro].getAutor())
        print('-=' * 16)

        print('\n1 - Editar título')
        print('2 - Editar gênero')
        print('3 - Editar ISBN')
        print('4 - Editar Autor')
        print('5 - Editar todas as informações')
        print('6 - Retornar ao menu')

        opcao = int(input('\nDigite uma opção: '))

      if opcao == 1:

        header()
        print('\n**Menu - Edição livro**\n')

        novoTitulo = input('[0 - Menu] Digite o novo título: ').upper()
        
        if novoTitulo == '0':
          menuBibliotecario(idConta)

        header()
        print('\n**Menu - Edição livro**\n')

        print('Antes:')
        print('-=' * 16)
        print('Título: ', listaLivros[indiceLivro].getTitulo())
        print('Gênero: ', listaLivros[indiceLivro].getGenero())
        print('ISBN: ', listaLivros[indiceLivro].getISBN())
        print('Autor: ', listaLivros[indiceLivro].getAutor())
        print('-=' * 16)

        listaLivros[indiceLivro].setTitulo(novoTitulo)
        listaTitulos[indiceLivro] = novoTitulo

        atualizaListaLivros()

        atualizaListaTitulos()

        print('Depois:')
        print('-=' * 16)
        print('Título: ', listaLivros[indiceLivro].getTitulo())
        print('Gênero: ', listaLivros[indiceLivro].getGenero())
        print('ISBN: ', listaLivros[indiceLivro].getISBN())
        print('Autor: ', listaLivros[indiceLivro].getAutor())
        print('-=' * 16)

        opcaoRetorno = ''

        while opcaoRetorno != '1':
          opcaoRetorno = input('\nDigite 1 para voltar ao menu: ')

        menuBibliotecario(idConta)

      elif opcao == 2:

        header()
        print('\n**Menu - Edição livro**\n')

        novoGenero = input('Digite o novo gênero: ').upper()
        
        if novoGenero == '0':
          menuBibliotecario(idConta)

        header()
        print('\n**Menu - Edição livro**\n')

        print('Antes:')
        print('-=' * 16)
        print('Título: ', listaLivros[indiceLivro].getTitulo())
        print('Gênero: ', listaLivros[indiceLivro].getGenero())
        print('ISBN: ', listaLivros[indiceLivro].getISBN())
        print('Autor: ', listaLivros[indiceLivro].getAutor())
        print('-=' * 16)

        listaLivros[indiceLivro].setGenero(novoGenero)

        atualizaListaLivros()

        print('Depois:')
        print('-=' * 16)
        print('Título: ', listaLivros[indiceLivro].getTitulo())
        print('Gênero: ', listaLivros[indiceLivro].getGenero())
        print('ISBN: ', listaLivros[indiceLivro].getISBN())
        print('Autor: ', listaLivros[indiceLivro].getAutor())
        print('-=' * 16)

        opcaoRetorno = ''

        while opcaoRetorno != '1':
          opcaoRetorno = input('\nDigite 1 para voltar ao menu: ')

        menuBibliotecario(idConta)              

      elif opcao == 3:

        header()
        print('\n**Menu - Edição livro**\n')   

        novoISBN = input('[0 - Menu] Digite o novo ISBN: ')

        if novoISBN == '0':
          menuBibliotecario(idConta)

        isbnExistente = False

        for isbn in listaISBN:
          if novoISBN == isbn:
            isbnExistente = True

        while isbnExistente == True:

          header()
          print('\n**Menu - Edição livro**\n')

          print('[ISBN já registrado, tente novamente!]\n')
          novoISBN = input('[0 - Menu] Digite o novo ISBN: ')
          
          if novoISBN == '0':
            menuBibliotecario(idConta)

          if novoISBN not in listaISBN:
            isbnExistente = False

        header()
        print('\n**Menu - Edição livro**\n')

        print('Antes:')
        print('-=' * 16)
        print('Título: ', listaLivros[indiceLivro].getTitulo())
        print('Gênero: ', listaLivros[indiceLivro].getGenero())
        print('ISBN: ', listaLivros[indiceLivro].getISBN())
        print('Autor: ', listaLivros[indiceLivro].getAutor())
        print('-=' * 16)

        listaLivros[indiceLivro].setISBN(novoISBN)
        listaISBN[indiceLivro] = novoISBN

        atualizaListaLivros()

        atualizaListaISBN()

        print('Depois:')
        print('-=' * 16)
        print('Título: ', listaLivros[indiceLivro].getTitulo())
        print('Gênero: ', listaLivros[indiceLivro].getGenero())
        print('ISBN: ', listaLivros[indiceLivro].getISBN())
        print('Autor: ', listaLivros[indiceLivro].getAutor())
        print('-=' * 16)

        opcaoRetorno = ''

        while opcaoRetorno != '1':
          opcaoRetorno = input('\nDigite 1 para voltar ao menu: ')

        menuBibliotecario(idConta)

      elif opcao == 4:

        header()
        print('\n**Menu - Edição livro**\n') 

        novoAutor = input('[0 - Menu] Digite o novo autor: ').upper()

        if novoAutor == '0':
          menuBibliotecario(idConta)    

        header()
        print('\n**Menu - Edição livro**\n')

        print('Antes:')
        print('-=' * 16)
        print('Título: ', listaLivros[indiceLivro].getTitulo())
        print('Gênero: ', listaLivros[indiceLivro].getGenero())
        print('ISBN: ', listaLivros[indiceLivro].getISBN())
        print('Autor: ', listaLivros[indiceLivro].getAutor())
        print('-=' * 16)

        listaLivros[indiceLivro].setAutor(novoAutor)

        atualizaListaLivros()

        print('Depois:')
        print('-=' * 16)
        print('Título: ', listaLivros[indiceLivro].getTitulo())
        print('Gênero: ', listaLivros[indiceLivro].getGenero())
        print('ISBN: ', listaLivros[indiceLivro].getISBN())
        print('Autor: ', listaLivros[indiceLivro].getAutor())
        print('-=' * 16)

        opcaoRetorno = ''

        while opcaoRetorno != '1':
          opcaoRetorno = input('\nDigite 1 para voltar ao menu: ')

        menuBibliotecario(idConta)
      
      elif opcao == 5:

        header()
        print('\n**Menu - Edição livro**\n')

        novoTitulo = input('[0 - Menu] Digite o novo título: ').upper()

        if novoTitulo == '0':
          menuBibliotecario(idConta)

        novoGenero = input('[0 - Menu] Digite o novo gênero: ').upper()

        if novoGenero == '0':
          menuBibliotecario(idConta)

        novoISBN = input('[0 - Menu] Digite o novo ISBN: ')

        if novoISBN == '0':
          menuBibliotecario(idConta)

        isbnExistente = False

        for isbn in listaISBN:
          if novoISBN == isbn:
            isbnExistente = True

        while isbnExistente == True:
          print('[ISBN já registrado, tente novamente!')
          novoISBN = input('[0 - Menu] Digite o novo ISBN: ')
          
          if novoISBN == '0':
            menuBibliotecario(idConta)

          if novoISBN not in listaISBN:
            isbnExistente = False

        novoAutor = input('[0 - Menu] Digite o novo autor: ').upper()

        if novoAutor == '0':
          menuBibliotecario(idConta)

        header()
        print('\n**Menu - Edição livro**\n')

        print('Antes:')
        print('-=' * 16)
        print('Título: ', listaLivros[indiceLivro].getTitulo())
        print('Gênero: ', listaLivros[indiceLivro].getGenero())
        print('ISBN: ', listaLivros[indiceLivro].getISBN())
        listaISBN[indiceLivro] = novoISBN
        print('Autor: ', listaLivros[indiceLivro].getAutor())
        print('-=' * 16)

        listaLivros[indiceLivro].setTitulo(novoTitulo)
        listaTitulos[indiceLivro] = novoTitulo
        listaLivros[indiceLivro].setGenero(novoGenero)
        listaLivros[indiceLivro].setISBN(novoISBN)
        listaISBN[indiceLivro] = novoISBN
        listaLivros[indiceLivro].setAutor(novoAutor)

        atualizaListaLivros()

        atualizaListaTitulos()

        atualizaListaISBN()

        print('Depois:')
        print('-=' * 16)
        print('Título: ', listaLivros[indiceLivro].getTitulo())
        print('Gênero: ', listaLivros[indiceLivro].getGenero())
        print('ISBN: ', listaLivros[indiceLivro].getISBN())
        print('Autor: ', listaLivros[indiceLivro].getAutor())
        print('-=' * 16)

        opcaoRetorno = ''

        while opcaoRetorno != '1':
          opcaoRetorno = input('\nDigite 1 para voltar ao menu: ')

        menuBibliotecario(idConta)

      else:
        menuBibliotecario(idConta)

    elif opcao == 2:

      livroEncontrado = False

      counter = 0

      while livroEncontrado == False:
        header()
        print('\n**Menu - Edição livro**\n')            
  
        if counter >= 1:
          print('Nenhum livro encontrado, tente novamente!\n')

        isbn = input('[0 - Menu] Digite o ISBN: ')

        if isbn == '0':
          menuBibliotecario(idConta)

        counter += 1

        for livro in listaLivros:
          if livro.getISBN() == isbn:
            indiceLivro = listaLivros.index(livro)
            livroEncontrado = True

      opcao = 0

      while opcao < 1 or opcao > 6:

        header()
        print('\n**Menu - Edição livro**\n')   

        print('-=' * 16)
        print('Título: ', listaLivros[indiceLivro].getTitulo())
        print('Gênero: ', listaLivros[indiceLivro].getGenero())
        print('ISBN: ', listaLivros[indiceLivro].getISBN())
        print('Autor: ', listaLivros[indiceLivro].getAutor())
        print('-=' * 16)

        print('\n1 - Editar título')
        print('2 - Editar gênero')
        print('3 - Editar ISBN')
        print('4 - Editar Autor')
        print('5 - Editar todas as informações')
        print('6 - Retornar ao menu')

        opcao = int(input('\nDigite uma opção: '))

      if opcao == 1:
  
        header()
        print('\n**Menu - Edição livro**\n')

        novoTitulo = input('[0 - Menu] Digite o novo título: ').upper()

        if novoTitulo == '0':
          menuBibliotecario(idConta)

        header()
        print('\n**Menu - Edição livro**\n')   

        print('Antes:')
        print('-=' * 16)
        print('Título: ', listaLivros[indiceLivro].getTitulo())
        print('Gênero: ', listaLivros[indiceLivro].getGenero())
        print('ISBN: ', listaLivros[indiceLivro].getISBN())
        print('Autor: ', listaLivros[indiceLivro].getAutor())
        print('-=' * 16)

        listaLivros[indiceLivro].setTitulo(novoTitulo)
        listaTitulos[indiceLivro] = novoTitulo

        atualizaListaLivros()

        atualizaListaTitulos()

        print('Depois:')
        print('-=' * 16)
        print('Título: ', listaLivros[indiceLivro].getTitulo())
        print('Gênero: ', listaLivros[indiceLivro].getGenero())
        print('ISBN: ', listaLivros[indiceLivro].getISBN())
        print('Autor: ', listaLivros[indiceLivro].getAutor())
        print('-=' * 16)

        opcaoRetorno = ''

        while opcaoRetorno != '1':
          opcaoRetorno = input('\nDigite 1 para voltar ao menu: ')

        menuBibliotecario(idConta)

      elif opcao == 2:
  
        header()
        print('\n**Menu - Edição livro**\n')

        novoGenero = input('[0 - Menu] Digite o novo gênero: ').upper()

        if novoGenero == '0':
          menuBibliotecario(idConta)
  
        header()
        print('\n**Menu - Edição livro**\n')   

        print('Antes:')
        print('-=' * 16)
        print('Título: ', listaLivros[indiceLivro].getTitulo())
        print('Gênero: ', listaLivros[indiceLivro].getGenero())
        print('ISBN: ', listaLivros[indiceLivro].getISBN())
        print('Autor: ', listaLivros[indiceLivro].getAutor())
        print('-=' * 16)

        listaLivros[indiceLivro].setGenero(novoGenero)

        atualizaListaLivros()

        print('Depois:')
        print('-=' * 16)
        print('Título: ', listaLivros[indiceLivro].getTitulo())
        print('Gênero: ', listaLivros[indiceLivro].getGenero())
        print('ISBN: ', listaLivros[indiceLivro].getISBN())
        print('Autor: ', listaLivros[indiceLivro].getAutor())
        print('-=' * 16)

        opcaoRetorno = ''

        while opcaoRetorno != '1':
          opcaoRetorno = input('\nDigite 1 para voltar ao menu: ')

        menuBibliotecario(idConta)

      elif opcao == 3:
  
        header()
        print('\n**Menu - Edição livro**\n')

        novoISBN = input('[0 - Menu] Digite o novo ISBN: ')

        if novoISBN == '0':
          menuBibliotecario(idConta)

        isbnExistente = False

        for isbn in listaISBN:
          if novoISBN == isbn:
            isbnExistente = True

        while isbnExistente == True:
          header()
          print('\n**Menu - Edição livro**\n')
          print('[ISBN já registrado, tente novamente!]\n')
          novoISBN = input('[0 - Menu] Digite o novo ISBN: ')
          
          if novoISBN == '0':
            menuBibliotecario(idConta)

          if novoISBN not in listaISBN:
            isbnExistente = False

        header()
        print('\n**Menu - Edição livro**\n')   

        print('Antes:')
        print('-=' * 16)
        print('Título: ', listaLivros[indiceLivro].getTitulo())
        print('Gênero: ', listaLivros[indiceLivro].getGenero())
        print('ISBN: ', listaLivros[indiceLivro].getISBN())
        print('Autor: ', listaLivros[indiceLivro].getAutor())
        print('-=' * 16)

        listaLivros[indiceLivro].setISBN(novoISBN)
        listaISBN[indiceLivro] = novoISBN

        atualizaListaLivros()

        atualizaListaISBN()

        print('Depois:')
        print('-=' * 16)
        print('Título: ', listaLivros[indiceLivro].getTitulo())
        print('Gênero: ', listaLivros[indiceLivro].getGenero())
        print('ISBN: ', listaLivros[indiceLivro].getISBN())
        print('Autor: ', listaLivros[indiceLivro].getAutor())
        print('-=' * 16)

        opcaoRetorno = ''

        while opcaoRetorno != '1':
          opcaoRetorno = input('\nDigite 1 para voltar ao menu: ')

        menuBibliotecario(idConta)

      elif opcao == 4:
  
        header()
        print('\n**Menu - Edição livro**\n')

        novoAutor = input('[0 - Menu] Digite o novo autor: ').upper()

        if novoAutor == '0':
          menuBibliotecario(idConta)

        header()
        print('\n**Menu - Edição livro**\n')   

        print('Antes:')
        print('-=' * 16)
        print('Título: ', listaLivros[indiceLivro].getTitulo())
        print('Gênero: ', listaLivros[indiceLivro].getGenero())
        print('ISBN: ', listaLivros[indiceLivro].getISBN())
        print('Autor: ', listaLivros[indiceLivro].getAutor())
        print('-=' * 16)

        listaLivros[indiceLivro].setAutor(novoAutor)
        
        atualizaListaLivros()

        print('Depois:')
        print('-=' * 16)
        print('Título: ', listaLivros[indiceLivro].getTitulo())
        print('Gênero: ', listaLivros[indiceLivro].getGenero())
        print('ISBN: ', listaLivros[indiceLivro].getISBN())
        print('Autor: ', listaLivros[indiceLivro].getAutor())
        print('-=' * 16)

        opcaoRetorno = ''

        while opcaoRetorno != '1':
          opcaoRetorno = input('\nDigite 1 para voltar ao menu: ')

        menuBibliotecario(idConta)
      
      elif opcao == 5:

        header()
        print('\n**Menu - Edição livro**\n')   

        novoTitulo = input('[0 - Menu] Digite o novo título: ').upper()

        if novoTitulo == '0':
          menuBibliotecario(idConta)

        novoGenero = input('[0 - Menu] Digite o novo gênero: ').upper()

        if novoGenero == '0':
          menuBibliotecario(idConta)

        novoISBN = input('[0 - Menu] Digite o novo ISBN: ')

        if novoISBN == '0':
          menuBibliotecario(idConta)

        isbnExistente = False

        for isbn in listaISBN:
          if novoISBN == isbn:
            isbnExistente = True

        while isbnExistente == True:
          print('[ISBN já registrado, tente novamente!')
          novoISBN = input('[0 - Menu] Digite o novo ISBN: ')
          
          if novoISBN == '0':
            menuBibliotecario(idConta)

          if novoISBN not in listaISBN:
            isbnExistente = False

        novoAutor = input('[0 - Menu] Digite o novo autor: ').upper()

        if novoAutor == '0':
          menuBibliotecario(idConta)

        header()
        print('\n**Menu - Edição livro**\n')   

        print('Antes:')
        print('-=' * 16)
        print('Título: ', listaLivros[indiceLivro].getTitulo())
        print('Gênero: ', listaLivros[indiceLivro].getGenero())
        print('ISBN: ', listaLivros[indiceLivro].getISBN())
        print('Autor: ', listaLivros[indiceLivro].getAutor())
        print('-=' * 16)

        listaLivros[indiceLivro].setTitulo(novoTitulo)
        listaTitulos[indiceLivro] = novoTitulo
        listaLivros[indiceLivro].setGenero(novoGenero)
        listaLivros[indiceLivro].setISBN(novoISBN)
        listaISBN[indiceLivro] = novoISBN
        listaLivros[indiceLivro].setAutor(novoAutor)

        atualizaListaLivros()

        atualizaListaTitulos()

        atualizaListaISBN()

        print('Depois:')
        print('-=' * 16)
        print('Título: ', listaLivros[indiceLivro].getTitulo())
        print('Gênero: ', listaLivros[indiceLivro].getGenero())
        print('ISBN: ', listaLivros[indiceLivro].getISBN())
        print('Autor: ', listaLivros[indiceLivro].getAutor())
        print('-=' * 16)

        opcaoRetorno = ''

        while opcaoRetorno != '1':
          opcaoRetorno = input('\nDigite 1 para voltar ao menu: ')

        menuBibliotecario(idConta)

      else:
        menuBibliotecario(idConta)

    else:
      menuBibliotecario(idConta)

  elif opcao == 4:

    opcao = 0

    while opcao < 1 or opcao > 4:

      header()
      print('\n**Menu - Verificar membros**\n')

      print('1 - Procurar por ID')
      print('2 - Procurar por CPF')
      print('3 - Ver todos')
      print('4 - Retornar ao menu')

      opcao = int(input('\nDigite uma opção: '))

    if opcao == 1:

      membroEncontrado = False

      while membroEncontrado == False:

        header()
        print('\n**Menu - Verificar membros**\n')

        idPesquisa = input('[0 - Menu] Digite o ID: ')

        if idPesquisa == '0':
          menuBibliotecario(idConta)

        header()
        print('\n**Menu - Verificar membros**\n')

        for membro in listaMembros:
          if membro.getId() == idPesquisa:
            membroEncontrado = True
            print('-=' * 16)
            print('Nome: ', membro.getNome())
            print('Idade: ', membro.getIdade())
            print('Endereço: ', membro.getEndereco())
            print('CPF: ', membro.getCpf())
            print('ID: ', membro.getId())
            print('-=' * 16)

      opcao = ''

      while opcao != '1':
        opcao = input('\nDigite 1 para retornar: ')    

      menuBibliotecario(idConta)

    elif opcao == 2:

      membroEncontrado = False

      while membroEncontrado == False:

        header()
        print('\n**Menu - Verificar membros**\n')

        cpfPesquisa = input('[0 - Menu] Digite o CPF: ')

        if cpfPesquisa == '0':
          menuBibliotecario(idConta)

        header()
        print('\n**Menu - Verificar membros**\n')

        for membro in listaMembros:
          if membro.getCpf() == cpfPesquisa:
            membroEncontrado = True
            print('-=' * 16)
            print('Nome: ', membro.getNome())
            print('Idade: ', membro.getIdade())
            print('Endereço: ', membro.getEndereco())
            print('CPF: ', membro.getCpf())
            print('ID: ', membro.getId())
            print('-=' * 16)

      opcao = ''

      while opcao != '1':
        opcao = input('\nDigite 1 para retornar: ') 

      menuBibliotecario(idConta)

    elif opcao == 3:

      header()
      print('\n**Menu - Verificar membros**\n')

      counter = 0

      for membro in listaMembros:

        counter += 1

        print('-=' * 16)
        print('Nome: ', membro.getNome())
        print('Idade: ', membro.getIdade())
        print('Endereço: ', membro.getEndereco())
        print('CPF: ', membro.getCpf())
        print('ID: ', membro.getId())
        print('-=' * 16)

      if counter == 0:
        print('Nenhum membro encontrado!')

      opcao = ''

      while opcao != '1':
        opcao = input('\nDigite 1 para retornar: ') 

      menuBibliotecario(idConta)

    else:
      menuBibliotecario(idConta)

  elif opcao == 5:
    
    header()
    print('\n**Menu para registro de novo membro**\n')

    nome = input('[0 - Menu] Digite o nome: ').upper()

    if nome == '0':
      menuBibliotecario(idConta)

    idade = input('[0 - Menu] Digite a idade: ')

    if idade == '0':
      menuBibliotecario(idConta)

    enderecoMembro = input('[0 - Menu] Digite o endereço do membro: ').upper()

    if enderecoMembro == '0':
      menuBibliotecario(idConta)

    cpfMembro = input('[0 - Menu] Digite o cpf do membro: ')

    if cpfMembro == '0':
      menuBibliotecario(idConta)

    cpfExistente = False

    for membro in listaMembros:
      if cpfMembro == membro.getCpf():
        cpfExistente = True
    
    while cpfExistente == True:
      print('[CPF já registrado, tente novamente!]')
      cpfMembro = input('[0 - Menu] Digite o cpf do membro: ')

      if cpfMembro == '0':
        menuBibliotecario(idConta)

      counter = -1

      for membro in listaMembros:
        counter += 1
        if cpfMembro == membro.getCpf():
          counter += 100
          cpfExistente = True

      if counter == len(listaMembros) - 1:
        cpfExistente = False

    idMembro = random.randint(1000, 10000)

    while idMembro in listaIdMembro == True:
      idMembro = str(random.randint(1000, 10000))
    
    idMembro = str(idMembro)

    senhaMembro = input('[0 - Menu] Digite a senha: ')

    if senhaMembro == '0':
      menuBibliotecario(idConta)

    novoMembro = Membro(nome, idade, enderecoMembro, cpfMembro, idMembro, senhaMembro)

    listaMembros.append(novoMembro)
    listaIdMembro.append(idMembro)
    listaSenhaMembro.append(senhaMembro)

    atualizaListaMembros()

    atualizaListaIdMembros()

    atualizaListaSenhaMembros()

    header()

    for membro in listaMembros:
      if membro.getId() == idMembro:
        print('\nMembro cadastrado!\n')
        print('-=' * 16)
        print('Nome: ', membro.getNome())
        print('Idade: ', membro.getIdade())
        print('Endereço: ', membro.getEndereco())
        print('CPF: ', membro.getCpf())
        print('ID: ', membro.getId())    
        print('-=' * 16)

    opcao = ''

    while opcao != '1':
      opcao = input('\nDigite 1 para voltar ao menu: ')

    menuBibliotecario(idConta)

  elif opcao == 6:
    
    opcaoMembro = 0

    while opcaoMembro < 1 or opcaoMembro > 3:

      header()
      print('\n**Menu - Editar membro**\n')

      print('1 - Pesquisar membro utilizando id')
      print('2 - Pesquisar membro utilizando cpf')
      print('3 - Retornar ao menu')

      opcaoMembro = int(input('\nDigite uma opção: '))   

    if opcaoMembro == 1:
      
      membroEncontrado = False

      while membroEncontrado == False:
  
        header()
        print('\n**Menu - Editar membro**\n')

        idPesquisa = input('[0 - Menu] Digite o id: ')

        if idPesquisa == '0':
          menuBibliotecario(idConta)

        for membro in listaMembros:
          if membro.getId() == idPesquisa:
            indiceMembro = listaMembros.index(membro)
            membroEncontrado = True

      opcao = 0

      while opcao < 1 or opcao > 5:

        header()
        print('\n**Menu - Editar membro**\n')

        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)

        print('\n1 - Editar nome')
        print('2 - Editar idade')
        print('3 - Editar endereço')
        print('4 - Editar CPF')
        print('5 - Editar todas as informações')

        opcao = int(input('\nDigite uma opção: '))

      if opcao == 1:

        header()
        print('\n**Menu - Editar membro**\n')

        novoNome = input('[0 - Menu] Digite o novo nome: ').upper()

        if novoNome == '0':
          menuBibliotecario(idConta)

        header()
        print('\n**Menu - Editar membro**\n')

        print('-=' * 16)
        print('Antes:')
        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)

        listaMembros[indiceMembro].setNome(novoNome)

        atualizaListaMembros()

        print('Depois:')
        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)

        opcao = ''

        while opcao != '1':
          opcao = input('\nDigite 1 para voltar ao menu: ')

        menuBibliotecario(idConta)

      elif opcao == 2:

        header()
        print('\n**Menu - Editar membro**\n')

        novaIdade = input('[0 - Menu] Digite a nova idade: ')

        if novaIdade == '0':
          menuBibliotecario(idConta)

        header()
        print('\n**Menu - Editar membro**\n')

        print('-=' * 16)
        print('Antes:')
        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)

        listaMembros[indiceMembro].setIdade(novaIdade)

        atualizaListaMembros()

        print('Depois:')
        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)

        opcao = 0

        while opcao != '1':
          opcao = input('\nDigite 1 para voltar ao menu: ')

        menuBibliotecario(idConta)

      elif opcao == 3:

        header()
        print('\n**Menu - Editar membro**\n')

        novoEndereco = input('[0 - Menu] Digite o novo endereço: ').upper()

        if novoEndereco == '0':
          menuBibliotecario(idConta)

        header()
        print('\n**Menu - Editar membro**\n')

        print('-=' * 16)
        print('Antes:')
        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)

        listaMembros[indiceMembro].setEndereco(novoEndereco)

        atualizaListaMembros()

        print('Depois:')
        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)

        opcao = ''

        while opcao != '1':
          opcao = input('\nDigite 1 para voltar ao menu: ')

        menuBibliotecario(idConta)

      elif opcao == 4:

        header()
        print('\n**Menu - Editar membro**\n')

        novoCPF = input('[0 - Menu] Digite o novo cpf: ')

        if novoCPF == '0':
          menuBibliotecario(idConta)

        cpfExistente = False

        for membro in listaMembros:
          if novoCPF == membro.getCpf():
            cpfExistente = True
        
        while cpfExistente == True:
          print('[CPF já registrado, tente novamente!]')
          novoCPF = input('[0 - Menu] Digite o cpf do membro: ')

          if novoCPF == '0':
            menuBibliotecario(idConta)

          counter = -1

          for membro in listaMembros:
            counter += 1
            if novoCPF == membro.getCpf():
              counter += 100
              cpfExistente = True

          if counter == len(listaMembros) - 1:
            cpfExistente = False

        header()
        print('\n**Menu - Editar membro**\n')

        print('-=' * 16)
        print('Antes:')
        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)

        listaMembros[indiceMembro].setCpf(novoCPF)

        atualizaListaMembros()

        print('Depois:')
        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)

        opcao = ''

        while opcao != '1':
          opcao = input('\nDigite 1 para voltar ao menu: ')

        menuBibliotecario(idConta)
      
      elif opcao == 5:

        header()
        print('\n**Menu - Editar membro**\n')

        novoNome = input('[0 - Menu] Digite o novo nome: ').upper()

        if novoNome == '0':
          menuBibliotecario(idConta)

        novaIdade = input('[0 - Menu] Digite a nova idade: ')

        if novaIdade == '0':
          menuBibliotecario(idConta)

        novoEndereco = input('[0 - Menu] Digite o novo endereço: ').upper()

        if novoEndereco == '0':
          menuBibliotecario(idConta)

        novoCPF = input('[0 - Menu] Digite o novo cpf: ')

        if novoCPF == '0':
          menuBibliotecario(idConta)

        cpfExistente = False

        for membro in listaMembros:
          if novoCPF == membro.getCpf():
            cpfExistente = True
        
        while cpfExistente == True:
          print('[CPF já registrado, tente novamente!]')
          novoCPF = input('[0 - Menu] Digite o cpf do membro: ')

          if novoCPF == '0':
            menuBibliotecario(idConta)

          counter = -1

          for membro in listaMembros:
            counter += 1
            if novoCPF == membro.getCpf():
              counter += 100
              cpfExistente = True

          if counter == len(listaMembros) - 1:
            cpfExistente = False

        header()
        print('\n**Menu - Editar membro**\n')
        print('-=' * 16)
        print('Antes:')
        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)

        listaMembros[indiceMembro].setNome(novoNome)
        listaMembros[indiceMembro].setIdade(novaIdade)
        listaMembros[indiceMembro].setEndereco(novoEndereco)
        listaMembros[indiceMembro].setCpf(novoCPF)

        atualizaListaMembros()

        print('Depois:')
        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)

        opcao = ''

        while opcao != '1':
          opcao = input('\nDigite 1 para voltar ao menu: ')

        menuBibliotecario(idConta)

    elif opcaoMembro == 2:

      membroEncontrado = False

      while membroEncontrado == False:

        header()
        print('\n**Menu - Editar membro**\n')

        cpfPesquisa = input('[0 - Menu] Digite o CPF: ')

        if cpfPesquisa == '0':
          menuBibliotecario(idConta)

        for membro in listaMembros:
          if membro.getCpf() == cpfPesquisa:
            indiceMembro = listaMembros.index(membro)
            membroEncontrado = True

      opcao = 0

      while opcao < 1 or opcao > 5:

        header()
        print('\n**Menu - Editar membro**\n')

        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)

        print('\n1 - Editar nome')
        print('2 - Editar idade')
        print('3 - Editar endereço')
        print('4 - Editar CPF')
        print('5 - Editar todas as informações')

        opcao = int(input('\nDigite uma opção: '))

      if opcao == 1:

        header()
        print('\n**Menu - Editar membro**\n')

        novoNome = input('[0 - Menu] Digite o novo nome: ').upper()
        
        if novoNome == '0':
          menuBibliotecario(idConta)

        header()
        print('\n**Menu - Editar membro**\n')

        print('-=' * 16)
        print('Antes:')
        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)

        listaMembros[indiceMembro].setNome(novoNome)

        atualizaListaMembros()

        print('Depois:')
        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)

        opcao = ''

        while opcao != '1':
          opcao = input('\nDigite 1 para voltar ao menu: ')

        menuBibliotecario(idConta)

      elif opcao == 2:

        header()
        print('\n**Menu - Editar membro**\n')

        novaIdade = input('[0 - Menu] Digite a nova idade: ')

        if novaIdade == '0':
          menuBibliotecario(idConta)

        header()
        print('\n**Menu - Editar membro**\n')

        print('-=' * 16)
        print('Antes:')
        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)

        listaMembros[indiceMembro].setIdade(novaIdade)

        atualizaListaMembros()

        print('Depois:')
        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)

        opcao = ''

        while opcao != '1':
          opcao = input('\nDigite 1 para voltar ao menu: ')

        menuBibliotecario(idConta)

      elif opcao == 3:

        header()
        print('\n**Menu - Editar membro**\n')

        novoEndereco = input('Digite o novo endereço: ').upper()

        if novoEndereco == '0':
          menuBibliotecario(idConta)

        header()
        print('\n**Menu - Editar membro**\n')

        print('-=' * 16)
        print('Antes:')
        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)

        listaMembros[indiceMembro].setEndereco(novoEndereco)

        atualizaListaMembros()

        print('Depois:')
        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)

        opcao = ''

        while opcao != '1':
          opcao = input('\nDigite 1 para voltar ao menu: ')

        menuBibliotecario(idConta)

      elif opcao == 4:

        header()
        print('\n**Menu - Editar membro**\n')

        novoCPF = input('[0 - Menu] Digite o novo cpf: ')

        if novoCPF == '0':
          menuBibliotecario(idConta)

        cpfExistente = False

        for membro in listaMembros:
          if novoCPF == membro.getCpf():
            cpfExistente = True
        
        while cpfExistente == True:
          print('[CPF já registrado, tente novamente!]')
          novoCPF = input('[0 - Menu] Digite o cpf do membro: ')

          if novoCPF == '0':
            menuBibliotecario(idConta)

          counter = -1

          for membro in listaMembros:
            counter += 1
            if novoCPF == membro.getCpf():
              counter += 100
              cpfExistente = True

          if counter == len(listaMembros) - 1:
            cpfExistente = False

        header()
        print('\n**Menu - Editar membro**\n')

        print('-=' * 16)
        print('Antes:')
        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)

        listaMembros[indiceMembro].setCpf(novoCPF)

        atualizaListaMembros()

        print('Depois:')
        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)
    
        opcao = ''

        while opcao != '1':
          opcao = input('\nDigite 1 para voltar ao menu: ')

        menuBibliotecario(idConta)

      elif opcao == 5:

        header()
        print('\n**Menu - Editar membro**\n')

        novoNome = input('[0 - Menu] Digite o novo nome: ').upper()

        if novoNome == '0':
          menuBibliotecario(idConta)

        novaIdade = input('[0 - Menu] Digite a nova idade: ')

        if novaIdade == '0':
          menuBibliotecario(idConta)    

        novoEndereco = input('[0 - Menu] Digite o novo endereço: ').upper()

        if novoEndereco == '0':
          menuBibliotecario(idConta)

        novoCPF = input('[0 - Menu] Digite o novo cpf: ')

        if novoCPF == '0':
          menuBibliotecario(idConta)

        cpfExistente = False

        for membro in listaMembros:
          if novoCPF == membro.getCpf():
            cpfExistente = True
        
        while cpfExistente == True:
          print('[CPF já registrado, tente novamente!]')
          novoCPF = input('[0 - Menu] Digite o cpf do membro: ')

          if novoCPF == '0':
            menuBibliotecario(idConta)

          counter = -1

          for membro in listaMembros:
            counter += 1
            if novoCPF == membro.getCpf():
              counter += 100
              cpfExistente = True

          if counter == len(listaMembros) - 1:
            cpfExistente = False

        header()
        print('\n**Menu - Editar membro**\n')

        print('-=' * 16)
        print('Antes:')
        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)

        listaMembros[indiceMembro].setNome(novoNome)
        listaMembros[indiceMembro].setIdade(novaIdade)
        listaMembros[indiceMembro].setEndereco(novoEndereco)
        listaMembros[indiceMembro].setCpf(novoCPF)

        atualizaListaMembros()

        print('Depois:')
        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)

        opcao = ''

        while opcao != '1':
          opcao = input('\nDigite 1 para voltar ao menu: ')

        menuBibliotecario(idConta)

    else:
      menuBibliotecario(idConta)

  elif opcao == 7:
    
    opcao = 0

    while opcao < 1 or opcao > 3:

      header()
      print('\n**Menu - Remover membro**\n')

      print('1 - Remover membro utilizando ID')
      print('2 - Remover membro utilizando CPF')
      print('3 - Retornar ao menu')

      opcao = int(input('\nDigite uma opção: '))         

    if opcao == 1:

      membroEncontrado = False

      while membroEncontrado == False:
        
        header()
        print('\n**Menu - Remover membro**\n')

        idMembroRemocao = input('[0 - Menu] Digite o id: ')
        
        if idMembroRemocao == '0':
          menuBibliotecario(idConta)

        if idMembroRemocao in listaIdMembro:
          membroEncontrado = True
          indiceMembro = listaIdMembro.index(idMembroRemocao)

      opcao = 0

      while opcao < 1 or opcao > 2:
    
        header()
        print('\n**Menu - Remover membro**\n')

        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)

        opcao = int(input('\n[1 - Sim | 2 - Não] Tem certeza de que deseja remover o membro ? '))

      if opcao == 1:
        del listaIdMembro[indiceMembro]
        del listaSenhaMembro[indiceMembro]
        del listaMembros[indiceMembro]

        atualizaListaMembros()

        atualizaListaSenhaMembros()

        atualizaListaIdMembros()

        menuBibliotecario(idConta)

      else:
        menuBibliotecario(idConta)

    elif opcao == 2:

      membroEncontrado = False

      while membroEncontrado == False:

        header()
        print('\n**Menu - Remover membro**\n')

        cpfMembroRemocao = input('[0 - Menu] Digite o cpf: ')

        if cpfMembroRemocao == '0':
          menuBibliotecario(idConta)

        for membro in listaMembros:
          if cpfMembroRemocao == membro.getCpf():
            indiceMembro = listaMembros.index(membro)
            membroEncontrado = True

      opcao = 0

      while opcao < 1 or opcao > 2:
  
        header()
        print('\n**Menu - Remover membro**\n')

        print('-=' * 16)
        print('Nome: ', listaMembros[indiceMembro].getNome())
        print('Idade: ', listaMembros[indiceMembro].getIdade())
        print('Endereço: ', listaMembros[indiceMembro].getEndereco())
        print('CPF: ', listaMembros[indiceMembro].getCpf())
        print('ID: ', listaMembros[indiceMembro].getId())
        print('-=' * 16)

        opcao = int(input('\n[1- Sim | 2 - Não] Tem certeza de que deseja remover o membro ? '))

      if opcao == 1:

        del listaIdMembro[indiceMembro]
        del listaSenhaMembro[indiceMembro]
        del listaMembros[indiceMembro]

        atualizaListaMembros()

        atualizaListaSenhaMembros()

        atualizaListaIdMembros()

        menuBibliotecario(idConta)
      
      else:
        menuBibliotecario(idConta)

    else:      
      menuBibliotecario(idConta)

  elif opcao == 8:
    
    opcaoProcurarLivro = 0

    while opcaoProcurarLivro < 1 or opcaoProcurarLivro > 6:

      header()
      print('\n**Menu - Pesquisa livros**\n')

      print('1 - Procurar por título')
      print('2 - Procurar por ISBN')
      print('3 - Procurar por autor')
      print('4 - Procurar por gênero')
      print('5 - Ver todos os livros')
      print('6 - Retornar ao menu')

      opcaoProcurarLivro = int(input('\nDigite uma opção: ')) 

    if opcaoProcurarLivro == 1:

      livroEncontrado = False

      while livroEncontrado == False:
  
        header()
        print('\n**Menu - Pesquisa livros**\n')

        tituloLivro = input('[0 - Menu] Digite o título: ').upper()

        if tituloLivro == '0':
          menuBibliotecario(idConta)

        header()
        print('\n**Menu - Pesquisa livros**\n')

        for livro in listaLivros:
          if tituloLivro == livro.getTitulo():
            print('-=' * 16)
            print('Título: ', livro.getTitulo())
            print('Gênero: ', livro.getGenero())
            print('ISBN: ', livro.getISBN())
            print('Autor: ', livro.getAutor())
            print('-=' * 16)
            livroEncontrado = True

      opcao = ''

      while opcao != '1':
        opcao = input('\nDigite 1 para retornar: ')      

      menuBibliotecario(idConta)

    elif opcaoProcurarLivro == 2:

      livroEncontrado = False

      while livroEncontrado == False:
  
        header()
        print('\n**Menu - Pesquisa livros**\n')

        isbnLivro = input('[0 - Menu] Digite o ISBN: ')

        if isbnLivro == '0':
          menuBibliotecario(idConta)

        header()
        print('\n**Menu - Pesquisa livros**\n')

        for livro in listaLivros:
          if isbnLivro == livro.getISBN():
            print('-=' * 16)
            print('Título: ', livro.getTitulo())
            print('Gênero: ', livro.getGenero())
            print('ISBN: ', livro.getISBN())
            print('Autor: ', livro.getAutor())
            print('-=' * 16)
            livroEncontrado = True

      opcao = ''

      while opcao != '1':
        opcao = input('\nDigite 1 para retornar: ')

      menuBibliotecario(idConta)

    elif opcaoProcurarLivro == 3:

      autorEncontrado = False

      counter = 0

      while autorEncontrado == False:

        header()
        print('\n**Menu - Pesquisa livros**\n')

        if counter >= 1:
          print('Nenhum resultado encontrado, tente novamente!\n')

        autorLivro = input('[0 - Menu] Digite o autor: ').upper()
        
        counter += 1

        if autorLivro == '0':
          menuBibliotecario(idConta)

        header()
        print('\n**Menu - Pesquisa livros**\n')

        for livro in listaLivros:
          if autorLivro == livro.getAutor():
            autorEncontrado = True

      for livro in listaLivros:
        if autorLivro == livro.getAutor():
          print('-=' * 16)
          print('Título: ', livro.getTitulo())
          print('Gênero: ', livro.getGenero())
          print('ISBN: ', livro.getISBN())
          print('Autor: ', livro.getAutor())
          print('-=' * 16)

      opcao = ''

      while opcao != '1':
        opcao = input('\nDigite 1 para retornar ao menu: ')

      menuBibliotecario(idConta)

    elif opcaoProcurarLivro == 4:

      generoEncontrado = False

      counter = 0

      while generoEncontrado == False:
  
        header()
        print('\n**Menu - Pesquisa livros**\n')

        if counter >= 1:
          print('Nenhum resultado encontrado, tente novamente!\n')

        generoLivro = input('[0 - Menu] Digite o gênero: ').upper()

        counter += 1

        if generoLivro == '0':
          menuBibliotecario(idConta)

        header()
        print('\n**Menu - Pesquisa livros**\n')

        for livro in listaLivros:
          if generoLivro == livro.getGenero():
            generoEncontrado = True

      for livro in listaLivros:
        if generoLivro == livro.getGenero():
          print('-=' * 16)
          print('Título: ', livro.getTitulo())
          print('Gênero: ', livro.getGenero())
          print('ISBN: ', livro.getISBN())
          print('Autor: ', livro.getAutor())
          print('-=' * 16)

      opcao = ''

      while opcao != '1':
        opcao = input('\nDigite 1 para retornar: ')    

      menuBibliotecario(idConta)

    elif opcaoProcurarLivro == 5:

      header()
      print('\n**Menu - Pesquisa livros**\n')

      counter = 0

      for livro in listaLivros:
        counter += 1
        print('-=' * 16)
        print('Título: ', livro.getTitulo())
        print('Gênero: ', livro.getGenero())
        print('ISBN: ', livro.getISBN())
        print('Autor: ', livro.getAutor())
        print('-=' * 16)

      if counter == 0:
        print('Nenhum livro encontrado!')

      opcao = ''

      while opcao != '1':
        opcao = input('\nDigite 1 para retornar ao menu: ') 

      menuBibliotecario(idConta)

    else:
      menuBibliotecario(idConta)

  elif opcao == 9:
    
    header()
    print('\n**Menu - Verificar livros emprestados**\n')

    for livro in listaLivrosEmprestados:
      livro.getRecibo()
      print('-=' * 16)

    opcao = ''

    while opcao != '1':
      opcao = input('\nDigite 1 para retornar ao menu: ')
      
    menuBibliotecario(idConta)

  elif opcao == 10:
    
    senhaAtual = '-1'

    global listaSenhaBibliotecario
    global listaIdBibliotecario

    indiceSenha = listaIdBibliotecario.index(idConta)

    while senhaAtual != listaSenhaBibliotecario[indiceSenha]:

      header()
      print('\n**Menu - Alterar senha**\n')

      senhaAtual = input('[0 - Menu] Digite a senha atual: ')

      if senhaAtual == '0':
        menuBibliotecario(idConta)

    header()
    print('\n**Menu - Alterar senha**\n')

    novaSenha = input('[0 - Menu] Digite a nova senha: ')

    if novaSenha == '0':
      menuBibliotecario(idConta)

    novaSenhaConfirmacao = input('[0 - Menu] Digite a nova senha novamente: ')

    if novaSenhaConfirmacao == '0':
      menuBibliotecario(idConta)

    while novaSenha != novaSenhaConfirmacao:

      header()
      print('\n**Menu - Alterar senha**\n')
      print('As senhas digitadas são diferentes, tente novamente!')
      novaSenha = input('\n[0 - Menu] Digite a nova senha: ')

      if novaSenha == '0':
        menuBibliotecario(idConta)

      novaSenhaConfirmacao = input('[0 - Menu] Digite a nova senha novamente: ')

      if novaSenhaConfirmacao == '0':
        menuBibliotecario(idConta)

    listaSenhaBibliotecario[indiceSenha] = novaSenhaConfirmacao

    atualizaListaSenhaBibliotecarios()

    menuPrincipal()

  else:
    
    menuPrincipal()

def menuMembro(idConta):

  opcao = 0

  while opcao < 1 or opcao > 4:

    header()

    print('\n1 - Procurar por livros')
    print('2 - Verificar/retornar livros em posse')
    print('3 - Alterar senha')
    print('4 - Retornar ao menu')

    opcao = int(input('\nDigite uma opção: '))
  
  if opcao == 1:

    opcaoProcurarLivro = 0

    while opcaoProcurarLivro < 1 or opcaoProcurarLivro > 6:

      header()
      print('\n**Menu - Pesquisa livros**\n')

      print('1 - Procurar por título')
      print('2 - Procurar por ISBN')
      print('3 - Procurar por autor')
      print('4 - Procurar por gênero')
      print('5 - Ver todos os livros')
      print('6 - Retornar ao menu')

      opcaoProcurarLivro = int(input('\nDigite uma opção: ')) 

    if opcaoProcurarLivro == 1:

      livroEncontrado = False

      counter = 0

      while livroEncontrado == False:
  
        header()
        print('\n**Menu - Pesquisa livros**\n')

        if counter >= 1:
          print('Nenhum resultado encontrado, tente novamente!\n')

        tituloLivro = input('[0 - Menu] Digite o título: ').upper()

        counter += 1

        if tituloLivro == '0':
          menuMembro(idConta)

        header()
        print('\n**Menu - Pesquisa livros**\n')

        for livro in listaLivros:
          if tituloLivro == livro.getTitulo():
            print('-=' * 16)
            print('Título: ', livro.getTitulo())
            print('Gênero: ', livro.getGenero())
            print('ISBN: ', livro.getISBN())
            print('Autor: ', livro.getAutor())
            print('-=' * 16)
            
            indiceLivro = listaLivros.index(livro)
            livroEncontrado = True

      opcao = 0
      while (opcao < 1 or opcao > 2) and livroEncontrado == True:
  
        header()
        print('\n**Menu - Pesquisa livros**\n')

        print('-=' * 16)
        print('Título: ', listaLivros[indiceLivro].getTitulo())
        print('Gênero: ', listaLivros[indiceLivro].getGenero())
        print('ISBN: ', listaLivros[indiceLivro].getISBN())
        print('Autor: ', listaLivros[indiceLivro].getAutor())
        print('-=' * 16)

        opcao = int(input('\n[1 - Pegar livro | 2 - Menu] Digite uma opção: '))

      if opcao == 1 and listaLivros[indiceLivro].getQuantidade() >= 1:

        dataEmprestimo  = date.today()
        dataDevolucao = date.today() + timedelta(days=7)

        livroEmprestado = Emprestimo(idConta, listaLivros[indiceLivro], dataEmprestimo, dataDevolucao)

        listaLivrosEmprestados.append(livroEmprestado)

        listaLivros[indiceLivro].setQuantidade(-1)

        atualizaListaLivrosEmprestados()

        atualizaListaLivros()

        header()
        print('\n**Menu - Pesquisa livros**\n')

        listaLivrosEmprestados[len(listaLivrosEmprestados) - 1].getRecibo()
        print('-=' * 16)

        opcao = '0'
        while opcao != '1':
          opcao = input('\nDigite 1 para retornar ao menu: ')

        menuMembro(idConta)

      elif opcao == 1 and listaLivros[indiceLivro].getQuantidade() < 1:

        opcao = '0'

        while opcao != '1':

          header()
          print('\n**Menu - Pesquisa livros**\n')

          print('Todas as unidades deste livro estão emprestadas atualmente!')

          opcao = input('\nDigite 1 para retornar ao menu: ')

        menuMembro(idConta)       

      else:

        menuMembro(idConta)       

    elif opcaoProcurarLivro == 2:

      livroEncontrado = False

      counter = 0

      while livroEncontrado == False:

        header()
        print('\n**Menu - Pesquisa livros**\n')

        if counter >= 1:
          print('Nenhum resultado encontrado, tente novamente!\n')

        isbnLivro = input('[0 - Menu] Digite o ISBN: ')

        counter += 1

        if isbnLivro == '0':
          menuMembro(idConta)

        header()
        print('\n**Menu - Pesquisa livros**\n')

        for livro in listaLivros:
          if isbnLivro == livro.getISBN():
            print('-=' * 16)
            print('Título: ', livro.getTitulo())
            print('Gênero: ', livro.getGenero())
            print('ISBN: ', livro.getISBN())
            print('Autor: ', livro.getAutor())
            print('-=' * 16)

            indiceLivro = listaLivros.index(livro)
            livroEncontrado = True

      if listaLivros[indiceLivro].getQuantidade() >= 0:

        opcao = 0
        while opcao < 1 or opcao > 2:
    
          header()
          print('\n**Menu - Pesquisa livros**\n')

          print('-=' * 16)
          print('Título: ', listaLivros[indiceLivro].getTitulo())
          print('Gênero: ', listaLivros[indiceLivro].getGenero())
          print('ISBN: ', listaLivros[indiceLivro].getISBN())
          print('Autor: ', listaLivros[indiceLivro].getAutor())
          print('-=' * 16)

          opcao = int(input('\n[1 - Pegar livro | 2 - Menu] Digite uma opção: '))

        if opcao == 1 and listaLivros[indiceLivro].getQuantidade() >= 1:

          dataEmprestimo  = date.today()
          dataDevolucao = date.today() + timedelta(days=7)

          livroEmprestado = Emprestimo(idConta, listaLivros[indiceLivro], dataEmprestimo, dataDevolucao)

          listaLivrosEmprestados.append(livroEmprestado)

          listaLivros[indiceLivro].setQuantidade(-1)

          atualizaListaLivrosEmprestados()

          atualizaListaLivros()

          header()
          print('\n**Menu - Pesquisa livros**\n')

          listaLivrosEmprestados[len(listaLivrosEmprestados) - 1].getRecibo()

          print('-=' * 16)

          opcao = '0'

          while opcao != '1':
            opcao = input('\nDigite 1 para retornar ao menu: ')

          menuMembro(idConta)
      
        elif opcao == 1 and listaLivros[indiceLivro].getQuantidade() < 1:

          opcao = '0'

          while opcao != '1':

            header()
            print('\n**Menu - Pesquisa livros**\n')

            print('Todas as unidades deste livro estão emprestadas atualmente!')
          
            opcao = input('\nDigite 1 para retornar ao menu: ')

          menuMembro(idConta) 

        else:
    
          menuMembro(idConta)       

    elif opcaoProcurarLivro == 3:
      
      autorEncontrado = False

      counter = 0

      while autorEncontrado == False:

        header()
        print('\n**Menu - Pesquisa livros**\n')

        if counter >= 1:
          print('Nenhum resultado encontrado, tente novamente!\n')

        autorLivro = input('[0 - Menu] Digite o autor: ').upper()
        
        counter += 1

        if autorLivro == '0':
          menuMembro(idConta)

        header()
        print('\n**Menu - Pesquisa livros**\n')

        for livro in listaLivros:
          if autorLivro == livro.getAutor():
            autorEncontrado = True

      opcao = 0

      while opcao < 1 or opcao > 2:

        header()
        print('\n**Menu - Pesquisa livros**\n')

        for livro in listaLivros:
          if autorLivro == livro.getAutor():
            print('-=' * 16)
            print('Título: ', livro.getTitulo())
            print('Gênero: ', livro.getGenero())
            print('ISBN: ', livro.getISBN())
            print('Autor: ', livro.getAutor())
            print('-=' * 16)

        opcao = int(input('\n[1 - Pegar livro | 2 - Menu] Digite uma opção: '))
      
      if opcao == 1:
        isbnEncontrado = False

        header()
        print('\n**Menu - Pesquisa livros**\n')

        while isbnEncontrado == False:

          header()
          print('\n**Menu - Pesquisa livros**\n')

          for livro in listaLivros:
            if autorLivro == livro.getAutor():
              print('-=' * 16)
              print('Título: ', livro.getTitulo())
              print('Gênero: ', livro.getGenero())
              print('ISBN: ', livro.getISBN())
              print('Autor: ', livro.getAutor())
              print('-=' * 16)

          isbn = input('\n[0 - Menu] Digite o ISBN do livro que deseja pegar emprestado: ')
          
          if isbn == '0':
            menuMembro(idConta)
          
          for livro in listaLivros:
            if isbn == livro.getISBN() and autorLivro == livro.getAutor():
              isbnEncontrado = True
              indiceLivro = listaLivros.index(livro)
              if livro.getQuantidade() >= 1:

                dataEmprestimo  = date.today()
                dataDevolucao = date.today() + timedelta(days=7)

                livroEmprestado = Emprestimo(idConta, listaLivros[indiceLivro], dataEmprestimo, dataDevolucao)

                listaLivrosEmprestados.append(livroEmprestado)

                livro.setQuantidade(-1)

                atualizaListaLivrosEmprestados()

                atualizaListaLivros()

                header()
                print('\n**Menu - Pesquisa livros**\n')

                listaLivrosEmprestados[len(listaLivrosEmprestados) - 1].getRecibo()

                print('-=' * 16)

                opcao = '0'
                while opcao != '1':
                  opcao = input('\nDigite 1 para retornar ao menu: ')

                menuMembro(idConta)

              else:

                opcao = '0'

                while opcao != '1':

                  header()
                  print('\n**Menu - Pesquisa livros**\n')

                  print('Todas as unidades deste livro estão emprestadas atualmente!')

                  opcao = input('\nDigite 1 para retornar ao menu: ')

                menuMembro(idConta)
      else:
        menuMembro(idConta)

    elif opcaoProcurarLivro == 4:

      generoEncontrado = False

      counter = 0

      while generoEncontrado == False:

        header()
        print('\n**Menu - Pesquisa livros**\n')
        
        if counter >= 1:
          print('Nenhum resultado encontrado, tente novamente!\n')

        generoLivro = input('[0 - Menu] Digite o gênero: ').upper()
        
        counter += 1

        if generoLivro == '0':
          menuMembro(idConta)

        header()
        print('\n**Menu - Pesquisa livros**\n')

        for livro in listaLivros:
          if generoLivro == livro.getGenero():
            generoEncontrado = True

      opcao = 0

      while opcao < 1 or opcao > 2:

        header()
        print('\n**Menu - Pesquisa livros**\n')

        for livro in listaLivros:
          if generoLivro == livro.getGenero():
            print('-=' * 16)
            print('Título: ', livro.getTitulo())
            print('Gênero: ', livro.getGenero())
            print('ISBN: ', livro.getISBN())
            print('Autor: ', livro.getAutor())
            print('-=' * 16)

        opcao = int(input('\n[1 - Pegar livro | 2 - Menu] Digite uma opção: '))
      
      if opcao == 1:
        isbnEncontrado = False

        header()
        print('\n**Menu - Pesquisa livros**\n')

        while isbnEncontrado == False:

          header()
          print('\n**Menu - Pesquisa livros**\n')

          for livro in listaLivros:
            if generoLivro == livro.getGenero():
              print('-=' * 16)
              print('Título: ', livro.getTitulo())
              print('Gênero: ', livro.getGenero())
              print('ISBN: ', livro.getISBN())
              print('Autor: ', livro.getAutor())
              print('-=' * 16)

          isbn = input('\n[0 - Menu] Digite o ISBN do livro que deseja pegar emprestado: ')
          
          if isbn == '0':
            menuMembro(idConta)
          
          for livro in listaLivros:
            if isbn == livro.getISBN():
              indiceLivro = listaLivros.index(livro)
              isbnEncontrado = True
              if livro.getQuantidade() >= 1:

                dataEmprestimo  = date.today()
                dataDevolucao = date.today() + timedelta(days=7)

                livroEmprestado = Emprestimo(idConta, listaLivros[indiceLivro], isbn, dataEmprestimo, dataDevolucao)

                listaLivrosEmprestados.append(livroEmprestado)

                livro.setQuantidade(-1)

                atualizaListaLivrosEmprestados()

                atualizaListaLivros()

                header()
                print('\n**Menu - Pesquisa livros**\n')

                listaLivrosEmprestados[len(listaLivrosEmprestados) - 1].getRecibo()

                print('-=' * 16)

                opcao = ''

                while opcao != '1':
                  opcao = input('\nDigite 1 para retornar ao menu: ')

                menuMembro(idConta)
                
              else:

                opcao = '0'

                while opcao != '1':

                  header()
                  print('\n**Menu - Pesquisa livros**\n')

                  print('Todas as unidades deste livro estão emprestadas atualmente!')

                  opcao = input('\nDigite 1 para retornar ao menu: ')

                menuMembro(idConta)

      else:
        menuMembro(idConta)

    elif opcaoProcurarLivro == 5:
            
      header()
      print('\n**Menu - Pesquisa livros**\n')

      counter = 0

      for livro in listaLivros:
        counter += 1
        print('-=' * 16)
        print('Título: ', livro.getTitulo())
        print('Gênero: ', livro.getGenero())
        print('ISBN: ', livro.getISBN())
        print('Autor: ', livro.getAutor())
        print('-=' * 16)

      if counter == 0:
        print('Nenhum livro encontrado!')

      opcao = ''

      while counter == 0 and opcao != '1':
        opcao = input('\nDigite 1 para retornar ao menu: ')

        if opcao == '1':
          menuMembro(idConta)

      opcao = 0

      while opcao < 1 or opcao > 2:
        header()
        print('\n**Menu - Pesquisa livros**\n')

        for livro in listaLivros:
          print('-=' * 16)
          print('Título: ', livro.getTitulo())
          print('Gênero: ', livro.getGenero())
          print('ISBN: ', livro.getISBN())
          print('Autor: ', livro.getAutor())
          print('-=' * 16)

        opcao = int(input('\n[1 - Pegar livro | 2 - Menu] Digite uma opção: '))

      if opcao == 1:
        isbnEncontrado = False

        while isbnEncontrado == False:
    
          header()
          print('\n**Menu - Pesquisa livros**\n')

          for livro in listaLivros:
            print('-=' * 16)
            print('Título: ', livro.getTitulo())
            print('Gênero: ', livro.getGenero())
            print('ISBN: ', livro.getISBN())
            print('Autor: ', livro.getAutor())
            print('-=' * 16)

          isbn = input('\n[0 - Menu] Digite o ISBN do livro que deseja pegar emprestado: ')
          
          if isbn == '0':
            menuMembro(idConta)

          header()
          print('\n**Menu - Pesquisa livros**\n')

          for livro in listaLivros:
            if isbn == livro.getISBN():
              indiceLivro = listaLivros.index(livro)
              isbnEncontrado = True
              if livro.getQuantidade() >= 1:

                dataEmprestimo  = date.today()
                dataDevolucao = date.today() + timedelta(days=7)

                livroEmprestado = Emprestimo(idConta, listaLivros[indiceLivro], dataEmprestimo, dataDevolucao)

                listaLivrosEmprestados.append(livroEmprestado)

                livro.setQuantidade(-1)

                atualizaListaLivrosEmprestados()

                atualizaListaLivros()

                header()
                print('\n**Menu - Pesquisa livros**\n')

                listaLivrosEmprestados[len(listaLivrosEmprestados) - 1].getRecibo()

                print('-=' * 16)

                opcao = '0'
                while opcao != '1':
                  opcao = input('\nDigite 1 para retornar ao menu: ')

                menuMembro(idConta)
                
              else:

                opcao = '0'

                while opcao != '1':
                  header()
                  print('\n**Menu - Pesquisa livros**\n')

                  print('Todas as unidades deste livro estão emprestadas atualmente!')
                  
                  opcao = input('\nDigite 1 para retornar ao menu: ')

                menuMembro(idConta)

      else:
        menuMembro(idConta)

    else:

      menuMembro(idConta)

  elif opcao == 2:
    
    header()
    print('\n**Menu - Verificação/retorno de livros**\n')

    dataAtual = date.today()

    livroEncontrado = False

    for livro in listaLivrosEmprestados:
      if livro.getID() == idConta:
        livroEncontrado = True

        livro.getRecibo()

        diferenca = abs(dataAtual - livro.getDataEmprestimo()).days

        if diferenca < 7:
          print(f'Dias: ({diferenca}/7)')
          print('-=' * 16)
        elif diferenca == 7:
          print(f'Dias: ({diferenca}/7)')
          print('\nVocê deve devolver o livro hoje para não pagar multa!')
          print('-=' * 16)
        elif diferenca > 7:
          multa = (diferenca - 7) * 2
          print(f'Dias: ({diferenca}/7)')
          print(f'\nNo momento, você deverá pagar uma multa de R$ {multa} ao devolver o livro (R$ 2 por dia de atraso).')
          print('-=' * 16)

    if livroEncontrado == True:

      opcao = ''

      while opcao != '1' and opcao != '2':
        opcao = input('\n[1 - Menu | 2 - Devolver livro] Deseja retornar ao menu ou devolver um livro ? ')
      
      if opcao == '1':
        menuMembro(idConta)

      if opcao == '2':
        isbnEncontrado = False

        while isbnEncontrado == False:
          isbn = input('[0 - Menu] Digite o ISBN do livro que deseja devolver: ')

          if isbn == '0':
            menuMembro(idConta)

          for livro in listaLivrosEmprestados:
            if idConta == livro.getID() and isbn == livro.livro.getISBN():
              isbnEncontrado = True
              indiceLivro = listaLivrosEmprestados.index(livro)

        if diferenca <= 7:

          header()
          print('\n**Menu - Verificação/retorno de livros**\n')

          del listaLivrosEmprestados[indiceLivro]
          
          for livro in listaLivros:
            if isbn == livro.getISBN():
              livro.setQuantidade(1)

          atualizaListaLivrosEmprestados()

          atualizaListaLivros()

          print('Livro devolvido!')

          opcao = ''

          while opcao != '1':
            opcao = input('\nDigite 1 para retornar ao menu: ')

          if opcao == '1':
            menuMembro(idConta)
        
        elif diferenca > 7:

          opcao = ''

          while opcao != '1':
            header()
            print('\n**Menu - Verificação/retorno de livros**\n')

            print(f'Você deverá pagar uma multa de R$ {multa}.')

            del listaLivrosEmprestados[indiceLivro]
            
            for livro in listaLivros:
              if isbn == livro.getISBN():
                livro.setQuantidade(1)
            
            atualizaListaLivrosEmprestados()

            atualizaListaLivros()

            print('Livro devolvido!\n')

            opcao = input('Digite 1 para retornar ao menu: ')

          if opcao == '1':
            menuMembro(idConta)

    if livroEncontrado == False:

      header()
      print('\n**Menu - Verificação/retorno de livros**\n')

      print('Não há livros em sua posse!')

      opcao = '0'

      while opcao != '1':
        opcao = input('\nDigite 1 para retornar ao menu: ')

      if opcao == '1':
        menuMembro(idConta)


    menuMembro(idConta)

  elif opcao == 3:
    
    global listaSenhaMembro
    global listaIdMembro

    indiceSenha = listaIdMembro.index(idConta)

    senhaAtual = '-1'

    while senhaAtual != listaSenhaMembro[indiceSenha]:

      header()
      print('\n**Menu - Alterar senha**\n')

      senhaAtual = input('[0 - Menu] Digite a senha atual: ')

      if senhaAtual == '0':
        menuMembro(idConta)

    header()
    print('\n**Menu - Alterar senha**\n')

    novaSenha = input('[0 - Menu] Digite a nova senha: ')

    if novaSenha == '0':
      menuMembro(idConta)

    novaSenhaConfirmacao = input('[0 - Menu] Digite a nova senha novamente: ')

    if novaSenhaConfirmacao == '0':
      menuMembro(idConta)

    while novaSenha != novaSenhaConfirmacao:

      header()
      print('\n**Menu - Alterar senha**\n')

      print('As senhas digitadas são diferentes, tente novamente!')

      novaSenha = input('\n[0 - Menu] Digite a nova senha: ')

      if novaSenha == '0':
        menuMembro(idConta)

      novaSenhaConfirmacao = input('[0 - Menu] Digite a nova senha novamente: ')

      if novaSenhaConfirmacao == '0':
        menuMembro(idConta)

    listaSenhaMembro[indiceSenha] = novaSenhaConfirmacao

    atualizaListaSenhaMembros()

    menuPrincipal()

  else:

    menuPrincipal()

def menuAdministrador():

  opcao = 0

  while opcao < 1 or opcao > 7:
    
    header()
    print('\n1 - Verificar bibliotecários')
    print('2 - Adicionar bibliotecário')
    print('3 - Editar bibliotecário')
    print('4 - Remover bibliotecário')
    print('5 - Alterar senha')
    print('6 - Alterar informações do administrador')
    print('7 - Retornar ao menu')
    opcao = int(input('\nDigite uma opção: '))

  if opcao == 1:

    opcao = 0

    while opcao < 1 or opcao > 4:

      header()
      print('\n**Menu - Verificar bibliotecários**\n')

      print('1 - Procurar por ID')
      print('2 - Procurar por CPF')
      print('3 - Ver todos')
      print('4 - Retornar ao menu')

      opcao = int(input('\nDigite uma opção: '))

    if opcao == 1:

      bibliotecarioEncontrado = False

      while bibliotecarioEncontrado == False:
        header()
        print('\n**Menu - Verificar bibliotecários**\n')

        idPesquisa = input('[0 - Menu] Digite o ID: ')

        if idPesquisa == '0':
          menuAdministrador()

        header()
        print('\n**Menu - Verificar bibliotecários**\n')

        for bibliotecario in listaBibliotecarios:
          if bibliotecario.getId() == idPesquisa:
            bibliotecarioEncontrado = True
            print('-=' * 16)
            print('Nome: ', bibliotecario.getNome())
            print('Turno: ', bibliotecario.getTurno())
            print('CPF: ', bibliotecario.getCpf())
            print('ID: ', bibliotecario.getId())
            print('-=' * 16)

      opcao = ''

      while opcao != '1':
        opcao = input('\nDigite 1 para retornar: ')    

      menuAdministrador()
    
    elif opcao == 2:

      bibliotecarioEncontrado = False

      while bibliotecarioEncontrado == False:
        header()
        print('\n**Menu - Verificar bibliotecários**\n')

        cpfPesquisa = input('[0 - Menu] Digite o CPF: ')

        if cpfPesquisa == '0':
          menuAdministrador()

        header()
        print('\n**Menu - Verificar bibliotecários**\n')

        for bibliotecario in listaBibliotecarios:
          if bibliotecario.getCpf() == cpfPesquisa:
            bibliotecarioEncontrado = True
            print('-=' * 16)
            print('Nome: ', bibliotecario.getNome())
            print('Turno: ', bibliotecario.getTurno())
            print('CPF: ', bibliotecario.getCpf())
            print('ID: ', bibliotecario.getId())
            print('-=' * 16)

      opcao = ''

      while opcao != '1':
        opcao = input('\nDigite 1 para retornar: ') 

      menuAdministrador()

    elif opcao == 3:

      header()
      print('\n**Menu - Verificar bibliotecários**\n')

      counter = 0

      for bibliotecario in listaBibliotecarios:
        counter += 1
        print('-=' * 16)
        print('Nome: ', bibliotecario.getNome())
        print('Turno: ', bibliotecario.getTurno())
        print('CPF: ', bibliotecario.getCpf())
        print('ID: ', bibliotecario.getId())
        print('-=' * 16)

      if counter == 0:
        print('Nenhum bibliotecário encontrado!')

      opcao = ''

      while opcao != '1':
        opcao = input('\nDigite 1 para retornar: ') 

      menuAdministrador()

    else:
      menuAdministrador()

  elif opcao == 2:
    
    header()
    print('\n**Menu - Adicionar bibliotecário**\n')

    nome = input('[0 - Menu] Digite o nome: ').upper()
    
    if nome == '0':
      menuAdministrador()

    turno = input('[0 - Menu] Digite o turno do bibliotecário [M/T/N]: ').upper()

    if turno == '0':
      menuAdministrador()

    while turno != 'M' and turno != 'T' and turno != 'N':
      turno = input('[0 - Menu] Digite o turno do bibliotecário [M/T/N]: ').upper()

    cpfBibliotecario = input('[0 - Menu] Digite o CPF: ')

    if cpfBibliotecario == '0':
      menuAdministrador()

    cpfExistente = cpfBibliotecario not in listaCpfBibliotecarios

    while cpfExistente != True:
      print('[CPF já registrado, tente novamente!]')
      cpfBibliotecario = input('[0 - Menu] Digite o CPF: ')

      if cpfBibliotecario == '0':
        menuAdministrador()

      cpfExistente = cpfBibliotecario not in listaCpfBibliotecarios

    listaCpfBibliotecarios.append(cpfBibliotecario)

    idBibliotecario = random.randint(1000, 10000)

    while idBibliotecario in listaIdBibliotecario == True:
      idBibliotecario = str(random.randint(1000, 10000))
    
    idBibliotecario = str(idBibliotecario)

    senhaBibliotecario = input('Digite a senha: ')

    novoBibliotecario = Bibliotecario(nome, turno, cpfBibliotecario, idBibliotecario, senhaBibliotecario)

    listaBibliotecarios.append(novoBibliotecario)
    listaIdBibliotecario.append(idBibliotecario)
    listaSenhaBibliotecario.append(senhaBibliotecario)

    atualizaListaCpfBibliotecarios()

    atualizaListaBibliotecarios()

    atualizaListaIdBibliotecarios()

    atualizaListaSenhaBibliotecarios()

    header()
    print('\nBibliotecário cadastrado!\n')

    for bibliotecario in listaBibliotecarios:
      if bibliotecario.getId() == idBibliotecario:
        print('-=' * 16)
        print('Nome: ', bibliotecario.getNome())
        print('Turno: ', bibliotecario.getTurno())
        print('CPF: ', bibliotecario.getCpf())
        print('ID: ', bibliotecario.getId())
        print('-=' * 16)

    opcao = ''

    while opcao != '1':

      opcao = input('\nDigite 1 para voltar ao menu: ')

    menuAdministrador()

  elif opcao == 3:
    
    opcao = 0

    while opcao < 1 or opcao > 3:

      header()
      print('\n**Menu - Editar bibliotecário**\n')

      print('1 - Pesquisar bibliotecário utilizando id')
      print('2 - Pesquisar bibliotecário utilizando cpf')
      print('3 - Retornar ao menu')

      opcao = int(input('\nDigite uma opção: '))

    if opcao == 1:

      bibliotecarioEncontrado = False

      while bibliotecarioEncontrado == False:

        header()
        print('\n**Menu - Editar bibliotecário**\n')

        idPesquisa = input('[0 - Menu] Digite o id: ')

        if idPesquisa == '0':
          menuAdministrador()

        for bibliotecario in listaBibliotecarios:
          if idPesquisa == bibliotecario.getId():
            bibliotecarioEncontrado = True
            indiceBibliotecario = listaBibliotecarios.index(bibliotecario)

      opcao = 0

      while opcao < 1 or opcao > 5:
  
        header()
        print('\n**Menu - Editar bibliotecário**\n')

        print('-=' * 16)
        print('Nome: ', listaBibliotecarios[indiceBibliotecario].getNome())
        print('Turno: ', listaBibliotecarios[indiceBibliotecario].getTurno())
        print('CPF: ', listaBibliotecarios[indiceBibliotecario].getCpf())
        print('ID: ', listaBibliotecarios[indiceBibliotecario].getId())
        print('-=' * 16)

        print('\n1 - Editar nome')
        print('2 - Editar turno')
        print('3 - Editar CPF')
        print('4 - Editar todas as informações')
        print('5 - Retornar ao menu')

        opcao = int(input('\nDigite uma opção: '))

      if opcao == 1:
  
        header()
        print('\n**Menu - Editar bibliotecário**\n')

        novoNome = input('[0 - Menu] Digite o novo nome: ').upper()

        if novoNome == '0':
          menuAdministrador()

        header()
        print('\n**Menu - Editar bibliotecário**\n')
        print('-=' * 16)
        print('Antes:')
        print('-=' * 16)
        print('Nome: ', listaBibliotecarios[indiceBibliotecario].getNome())
        print('Turno: ', listaBibliotecarios[indiceBibliotecario].getTurno())
        print('CPF: ', listaBibliotecarios[indiceBibliotecario].getCpf())
        print('ID: ', listaBibliotecarios[indiceBibliotecario].getId())
        print('-=' * 16)

        listaBibliotecarios[indiceBibliotecario].setNome(novoNome)

        atualizaListaBibliotecarios()

        print('Depois:')
        print('-=' * 16)
        print('Nome: ', listaBibliotecarios[indiceBibliotecario].getNome())
        print('Turno: ', listaBibliotecarios[indiceBibliotecario].getTurno())
        print('CPF: ', listaBibliotecarios[indiceBibliotecario].getCpf())
        print('ID: ', listaBibliotecarios[indiceBibliotecario].getId())
        print('-=' * 16)

        opcao = ''

        while opcao != '1':
          opcao = input('\nDigite 1 para voltar ao menu: ')

        menuAdministrador()

      elif opcao == 2:
  
        header()
        print('\n**Menu - Editar bibliotecário**\n')

        novoTurno = input('[0 - Menu] Digite o novo turno [M/T/N]: ').upper()

        if novoTurno == '0':
          menuAdministrador()

        while novoTurno != 'M' and novoTurno != 'T' and novoTurno != 'N':
          novoTurno = input('[0 - Menu] Digite o novo turno [M/T/N]: ').upper()
            
          if novoTurno == '0':
            menuAdministrador()

        header()
        print('\n**Menu - Editar bibliotecário**\n')
        print('-=' * 16)
        print('Antes:')
        print('-=' * 16)
        print('Nome: ', listaBibliotecarios[indiceBibliotecario].getNome())
        print('Turno: ', listaBibliotecarios[indiceBibliotecario].getTurno())
        print('CPF: ', listaBibliotecarios[indiceBibliotecario].getCpf())
        print('ID: ', listaBibliotecarios[indiceBibliotecario].getId())
        print('-=' * 16)

        listaBibliotecarios[indiceBibliotecario].setTurno(novoTurno)

        atualizaListaBibliotecarios()

        print('Depois:')
        print('-=' * 16)
        print('Nome: ', listaBibliotecarios[indiceBibliotecario].getNome())
        print('Turno: ', listaBibliotecarios[indiceBibliotecario].getTurno())
        print('CPF: ', listaBibliotecarios[indiceBibliotecario].getCpf())
        print('ID: ', listaBibliotecarios[indiceBibliotecario].getId())
        print('-=' * 16)

        opcao = ''

        while opcao != '1':
          opcao = input('\nDigite 1 para voltar ao menu: ')

        menuAdministrador()

      elif opcao == 3:
  
        header()
        print('\n**Menu - Editar bibliotecário**\n')

        novoCPF = input('[0 - Menu] Digite o novo CPF: ')

        if novoCPF == '0':
          menuAdministrador()

        cpfExistente = novoCPF not in listaCpfBibliotecarios

        while cpfExistente != True:
          print('[CPF já registrado, tente novamente!]')
          novoCPF = input('[0 - Menu] Digite o novo CPF: ')

          if novoCPF == '0':
            menuAdministrador()

          cpfExistente = novoCPF not in listaCpfBibliotecarios

        header()
        print('\n**Menu - Editar bibliotecário**\n')
        print('-=' * 16)
        print('Antes:')
        print('-=' * 16)
        print('Nome: ', listaBibliotecarios[indiceBibliotecario].getNome())
        print('Turno: ', listaBibliotecarios[indiceBibliotecario].getTurno())
        print('CPF: ', listaBibliotecarios[indiceBibliotecario].getCpf())
        print('ID: ', listaBibliotecarios[indiceBibliotecario].getId())
        print('-=' * 16)

        listaCpfBibliotecarios[indiceBibliotecario] = novoCPF

        listaBibliotecarios[indiceBibliotecario].setCpf(novoCPF)

        atualizaListaCpfBibliotecarios()

        atualizaListaBibliotecarios()

        print('Depois:')
        print('-=' * 16)
        print('Nome: ', listaBibliotecarios[indiceBibliotecario].getNome())
        print('Turno: ', listaBibliotecarios[indiceBibliotecario].getTurno())
        print('CPF: ', listaBibliotecarios[indiceBibliotecario].getCpf())
        print('ID: ', listaBibliotecarios[indiceBibliotecario].getId())
        print('-=' * 16)

        opcao = ''

        while opcao != '1':
          opcao = input('\nDigite 1 para voltar ao menu: ')

        menuAdministrador()

      elif opcao == 4:
  
        header()
        print('\n**Menu - Editar bibliotecário**\n')

        novoNome = input('[0 - Menu] Digite o novo nome: ').upper()

        if novoNome == '0':
          menuAdministrador()

        novoTurno = input('[0 - Menu] Digite o novo turno [M/T/N]: ').upper()

        if novoTurno == '0':
          menuAdministrador()

        while novoTurno != 'M' and novoTurno != 'T' and novoTurno != 'N':
          novoTurno = input('[0 - Menu] Digite o novo turno [M/T/N]: ').upper()

          if novoTurno == '0':
            menuAdministrador()

        novoCPF = input('[0 - Menu] Digite o CPF: ')

        if novoCPF == '0':
          menuAdministrador()

        cpfExistente = novoCPF not in listaCpfBibliotecarios

        while cpfExistente != True:
          print('[CPF já registrado, tente novamente!]')
          novoCPF = input('[0 - Menu] Digite o CPF: ')

          if novoCPF == '0':
            menuAdministrador()

          cpfExistente = novoCPF not in listaCpfBibliotecarios

        header()
        print('\n**Menu - Editar bibliotecário**\n')
        print('-=' * 16)
        print('Antes:')
        print('-=' * 16)
        print('Nome: ', listaBibliotecarios[indiceBibliotecario].getNome())
        print('Turno: ', listaBibliotecarios[indiceBibliotecario].getTurno())
        print('CPF: ', listaBibliotecarios[indiceBibliotecario].getCpf())
        print('ID: ', listaBibliotecarios[indiceBibliotecario].getId())
        print('-=' * 16)

        listaCpfBibliotecarios[indiceBibliotecario] = novoCPF

        listaBibliotecarios[indiceBibliotecario].setNome(novoNome)
        listaBibliotecarios[indiceBibliotecario].setTurno(novoTurno)
        listaBibliotecarios[indiceBibliotecario].setCpf(novoCPF)

        atualizaListaCpfBibliotecarios()

        atualizaListaBibliotecarios()

        print('Depois:')
        print('-=' * 16)
        print('Nome: ', listaBibliotecarios[indiceBibliotecario].getNome())
        print('Turno: ', listaBibliotecarios[indiceBibliotecario].getTurno())
        print('CPF: ', listaBibliotecarios[indiceBibliotecario].getCpf())
        print('ID: ', listaBibliotecarios[indiceBibliotecario].getId())
        print('-=' * 16)

        opcao = ''

        while opcao != '1':
          opcao = input('\nDigite 1 para voltar ao menu: ')

        menuAdministrador()

      else:
        menuAdministrador()

    elif opcao == 2:

      bibliotecarioEncontrado = False

      while bibliotecarioEncontrado == False:

        header()
        print('\n**Menu - Editar bibliotecário**\n')

        cpfPesquisa = input('[0 - Menu] Digite o CPF: ')

        if cpfPesquisa == '0':
          menuAdministrador()

        if cpfPesquisa in listaCpfBibliotecarios:
          indiceBibliotecario = listaCpfBibliotecarios.index(cpfPesquisa)
          bibliotecarioEncontrado = True

      opcao = 0

      while opcao < 1 or opcao > 5:

        header()
        print('\n**Menu - Editar bibliotecário**\n')

        print('-=' * 16)
        print('Nome: ', listaBibliotecarios[indiceBibliotecario].getNome())
        print('Turno: ', listaBibliotecarios[indiceBibliotecario].getTurno())
        print('CPF: ', listaBibliotecarios[indiceBibliotecario].getCpf())
        print('ID: ', listaBibliotecarios[indiceBibliotecario].getId())
        print('-=' * 16)

        print('\n1 - Editar nome')
        print('2 - Editar turno')
        print('3 - Editar CPF')
        print('4 - Editar todas as informações')
        print('5 - Retornar ao menu')

        opcao = int(input('\nDigite uma opção: '))

      if opcao == 1:

        header()
        print('\n**Menu - Editar bibliotecário**\n')

        novoNome = input('[0 - Menu] Digite o novo nome: ').upper()
        
        if novoNome == '0':
          menuAdministrador()

        header()
        print('\n**Menu - Editar bibliotecário**\n')
        print('-=' * 16)
        print('Antes:')
        print('-=' * 16)
        print('Nome: ', listaBibliotecarios[indiceBibliotecario].getNome())
        print('Turno: ', listaBibliotecarios[indiceBibliotecario].getTurno())
        print('CPF: ', listaBibliotecarios[indiceBibliotecario].getCpf())
        print('ID: ', listaBibliotecarios[indiceBibliotecario].getId())
        print('-=' * 16)

        listaBibliotecarios[indiceBibliotecario].setNome(novoNome)

        atualizaListaBibliotecarios()

        print('Depois:')
        print('-=' * 16)
        print('Nome: ', listaBibliotecarios[indiceBibliotecario].getNome())
        print('Turno: ', listaBibliotecarios[indiceBibliotecario].getTurno())
        print('CPF: ', listaBibliotecarios[indiceBibliotecario].getCpf())
        print('ID: ', listaBibliotecarios[indiceBibliotecario].getId())
        print('-=' * 16)

        opcao = ''

        while opcao != '1':
          opcao = input('\nDigite 1 para voltar ao menu: ')

        menuAdministrador()

      elif opcao == 2:

        header()
        print('\n**Menu - Editar bibliotecário**\n')

        novoTurno = input('[0 - Menu] Digite o novo turno [M/T/N]: ').upper()

        if novoTurno == '0':
          menuAdministrador()

        while novoTurno != 'M' and novoTurno != 'T' and novoTurno != 'N':
          novoTurno = input('[0 - Menu] Digite o novo turno [M/T/N]: ').upper()

          if novoTurno == '0':
            menuAdministrador()

        header()
        print('\n**Menu - Editar bibliotecário**\n')
        print('-=' * 16)
        print('Antes:')
        print('-=' * 16)
        print('Nome: ', listaBibliotecarios[indiceBibliotecario].getNome())
        print('Turno: ', listaBibliotecarios[indiceBibliotecario].getTurno())
        print('CPF: ', listaBibliotecarios[indiceBibliotecario].getCpf())
        print('ID: ', listaBibliotecarios[indiceBibliotecario].getId())
        print('-=' * 16)

        listaBibliotecarios[indiceBibliotecario].setTurno(novoTurno)

        atualizaListaBibliotecarios()

        print('Depois:')
        print('-=' * 16)
        print('Nome: ', listaBibliotecarios[indiceBibliotecario].getNome())
        print('Turno: ', listaBibliotecarios[indiceBibliotecario].getTurno())
        print('CPF: ', listaBibliotecarios[indiceBibliotecario].getCpf())
        print('ID: ', listaBibliotecarios[indiceBibliotecario].getId())
        print('-=' * 16)

        opcao = ''

        while opcao != '1':
          opcao = input('\nDigite 1 para voltar ao menu: ')

        menuAdministrador()

      elif opcao == 3:

        header()
        print('\n**Menu - Editar bibliotecário**\n')

        novoCPF = input('[0 - Menu] Digite o CPF: ')

        if novoCPF == '0':
          menuAdministrador()

        cpfExistente = novoCPF not in listaCpfBibliotecarios

        while cpfExistente != True:
          print('[CPF já registrado, tente novamente!]')
          novoCPF = input('[0 - Menu] Digite o CPF: ')

          if novoCPF == '0':
            menuAdministrador()

          cpfExistente = novoCPF not in listaCpfBibliotecarios

        header()
        print('\n**Menu - Editar bibliotecário**\n')
        print('-=' * 16)
        print('Antes:')
        print('-=' * 16)
        print('Nome: ', listaBibliotecarios[indiceBibliotecario].getNome())
        print('Turno: ', listaBibliotecarios[indiceBibliotecario].getTurno())
        print('CPF: ', listaBibliotecarios[indiceBibliotecario].getCpf())
        print('ID: ', listaBibliotecarios[indiceBibliotecario].getId())
        print('-=' * 16)

        listaCpfBibliotecarios[indiceBibliotecario] = novoCPF

        listaBibliotecarios[indiceBibliotecario].setCpf(novoCPF)

        atualizaListaCpfBibliotecarios()

        atualizaListaBibliotecarios()

        print('Depois:')
        print('-=' * 16)
        print('Nome: ', listaBibliotecarios[indiceBibliotecario].getNome())
        print('Turno: ', listaBibliotecarios[indiceBibliotecario].getTurno())
        print('CPF: ', listaBibliotecarios[indiceBibliotecario].getCpf())
        print('ID: ', listaBibliotecarios[indiceBibliotecario].getId())
        print('-=' * 16)

        opcao = ''

        while opcao != '1':
          opcao = input('\nDigite 1 para voltar ao menu: ')

        menuAdministrador()

      elif opcao == 4:

        header()
        print('\n**Menu - Editar bibliotecário**\n')

        novoNome = input('[0 - Menu] Digite o novo nome: ').upper()

        if novoNome == '0':
          menuAdministrador()

        novoTurno = input('[0 - Menu] Digite o novo turno [M/T/N]: ').upper()

        if novoTurno == '0':
          menuAdministrador()

        while novoTurno != 'M' and novoTurno != 'T' and novoTurno != 'N':
          novoTurno = input('[0 - Menu] Digite o novo turno [M/T/N]: ').upper()

          if novoTurno == '0':
            menuAdministrador()

        novoCPF = input('Digite o CPF: ')

        if novoCPF == '0':
          menuAdministrador()

        cpfExistente = novoCPF not in listaCpfBibliotecarios

        while cpfExistente != True:
          print('[CPF já registrado, tente novamente!]')
          novoCPF = input('Digite o CPF: ')

          if novoCPF == '0':
            menuAdministrador()

          cpfExistente = novoCPF not in listaCpfBibliotecarios

        header()
        print('\n**Menu - Editar bibliotecário**\n')
        print('-=' * 16)
        print('Antes:')
        print('-=' * 16)
        print('Nome: ', listaBibliotecarios[indiceBibliotecario].getNome())
        print('Turno: ', listaBibliotecarios[indiceBibliotecario].getTurno())
        print('CPF: ', listaBibliotecarios[indiceBibliotecario].getCpf())
        print('ID: ', listaBibliotecarios[indiceBibliotecario].getId())
        print('-=' * 16)

        listaCpfBibliotecarios[indiceBibliotecario] = novoCPF

        listaBibliotecarios[indiceBibliotecario].setNome(novoNome)
        listaBibliotecarios[indiceBibliotecario].setTurno(novoTurno)
        listaBibliotecarios[indiceBibliotecario].setCpf(novoCPF)

        atualizaListaCpfBibliotecarios()

        atualizaListaBibliotecarios()

        print('Depois:')
        print('-=' * 16)
        print('Nome: ', listaBibliotecarios[indiceBibliotecario].getNome())
        print('Turno: ', listaBibliotecarios[indiceBibliotecario].getTurno())
        print('CPF: ', listaBibliotecarios[indiceBibliotecario].getCpf())
        print('ID: ', listaBibliotecarios[indiceBibliotecario].getId())
        print('-=' * 16)

        opcao = ''

        while opcao != '1':
          opcao = input('\nDigite 1 para voltar ao menu: ')

        menuAdministrador()
      
      else:
        menuAdministrador()

    else:
      menuAdministrador()

  elif opcao == 4:

    opcao = 0

    while opcao < 1 or opcao > 3:

      header()
      print('\n**Menu - Remover bibliotecário**\n')

      print('1 - Remover bibliotecário utilizando id')
      print('2 - Remover bibliotecário utilizando cpf')
      print('3 - Retornar ao menu')

      opcao = int(input('\nDigite uma opção: '))  
     
    if opcao == 1:

      bibliotecarioEncontrado = False

      while bibliotecarioEncontrado == False:
  
        header()
        print('\n**Menu - Remover bibliotecário**\n')

        idBibliotecarioRemocao = input('[0 - Menu] Digite o id: ')
        
        if idBibliotecarioRemocao == '0':
          menuAdministrador()

        if idBibliotecarioRemocao in listaIdBibliotecario:
          bibliotecarioEncontrado = True
          indiceBibliotecario = listaIdBibliotecario.index(idBibliotecarioRemocao)

      header()
      print('\n**Menu - Remover bibliotecário**\n')

      print('-=' * 16)
      print('Nome: ', listaBibliotecarios[indiceBibliotecario].getNome())
      print('Turno: ', listaBibliotecarios[indiceBibliotecario].getTurno())
      print('CPF: ', listaBibliotecarios[indiceBibliotecario].getCpf())
      print('ID: ', listaBibliotecarios[indiceBibliotecario].getId())
      print('-=' * 16)

      opcao = 0

      while opcao < 1 or opcao > 2:

        opcao = int(input('\n[1 - Sim | 2 - Não] Tem certeza de que deseja remover o bibliotecário ? '))

      if opcao == 1:

        del listaIdBibliotecario[indiceBibliotecario]
        del listaSenhaBibliotecario[indiceBibliotecario]
        del listaBibliotecarios[indiceBibliotecario]
        del listaCpfBibliotecarios[indiceBibliotecario] 

        atualizaListaCpfBibliotecarios()

        atualizaListaBibliotecarios()

        atualizaListaIdBibliotecarios()

        atualizaListaSenhaBibliotecarios()

      else:
        menuAdministrador()

      menuAdministrador()

    elif opcao == 2:

      bibliotecarioEncontrado = False

      while bibliotecarioEncontrado == False:
  
        header()
        print('\n**Menu - Remover bibliotecário**\n')      

        cpfBibliotecarioRemocao = input('[0 - Menu] Digite o cpf: ')

        if cpfBibliotecarioRemocao == '0':
          menuAdministrador()

        if cpfBibliotecarioRemocao in listaCpfBibliotecarios:
          bibliotecarioEncontrado = True
          indiceBibliotecario = listaCpfBibliotecarios.index(cpfBibliotecarioRemocao)

      header()
      print('\n**Menu - Remover bibliotecário**\n')

      print('-=' * 16)
      print('Nome: ', listaBibliotecarios[indiceBibliotecario].getNome())
      print('Turno: ', listaBibliotecarios[indiceBibliotecario].getTurno())
      print('CPF: ', listaBibliotecarios[indiceBibliotecario].getCpf())
      print('ID: ', listaBibliotecarios[indiceBibliotecario].getId())
      print('-=' * 16)

      opcao = 0

      while opcao < 1 or opcao > 2:
        opcao = int(input('\n[1 - Sim | 2 - Não] Tem certeza de que deseja remover o bibliotecário ? '))

      if opcao == 1:

        del listaIdBibliotecario[indiceBibliotecario]
        del listaSenhaBibliotecario[indiceBibliotecario]
        del listaBibliotecarios[indiceBibliotecario]
        del listaCpfBibliotecarios[indiceBibliotecario]

        atualizaListaCpfBibliotecarios()

        atualizaListaBibliotecarios()

        atualizaListaIdBibliotecarios()

        atualizaListaSenhaBibliotecarios()

      else:
        menuAdministrador()
        
      menuAdministrador()

    else:
      menuAdministrador()

  elif opcao == 5:
    
    senhaAtual = '-1'

    global senhaAdministrador
    global idAdministrador

    while senhaAtual != senhaAdministrador:

      header()
      print('\n**Menu - Alterar senha**\n')

      senhaAtual = input('[0 - Menu] Digite a senha atual: ')

      if senhaAtual == '0':
        menuAdministrador()

    header()
    print('\n**Menu - Alterar senha**\n')

    novaSenha = input('[0 - Menu] Digite a nova senha: ')

    if novaSenha == '0':
      menuAdministrador()

    novaSenhaConfirmacao = input('[0 - Menu] Digite a nova senha novamente: ')

    if novaSenhaConfirmacao == '0':
      menuAdministrador()

    while novaSenha != novaSenhaConfirmacao:

      header()
      print('\n**Menu - Alterar senha**\n')

      print('As senhas digitadas são diferentes, tente novamente!')
      novaSenha = input('\n[0 - Menu] Digite a nova senha: ')
      
      if novaSenha == '0':
        menuAdministrador()

      novaSenhaConfirmacao = input('[0 - Menu] Digite a nova senha novamente: ')

      if novaSenhaConfirmacao == '0':
        menuAdministrador()

    senhaAdministrador = novaSenha

    atualizaSenhaAdmin()

    menuPrincipal()

  elif opcao == 6:

    opcao = 0
    while opcao < 1 or opcao > 5:

      header()
      print('\n**Menu - Alterar informações do administrador**\n')

      print('1 - Editar ID')
      print('2 - Editar nome')
      print('3 - Editar telefone')
      print('4 - Editar todas as informações acima')
      print('5 - Retornar ao menu')

      opcao = int(input('\nDigite a opção: '))

    if opcao == 1:

      idAtual = '-1'
      while idAtual != idAdministrador:
  
        header()
        print('\n**Menu - Alterar informações do administrador**\n')

        idAtual = input('[0 - Menu] Digite o ID atual: ')

        if idAtual == '0':
          menuAdministrador()

      header()
      print('\n**Menu - Alterar informações do administrador**\n')

      novoID = input('[0 - Menu] Digite o novo ID: ')

      if novoID == '0':
        menuAdministrador()

      novoIDConfirmacao = input('[0 - Menu] Digite o novo ID novamente: ')

      if novoIDConfirmacao == '0':
        menuAdministrador()

      while novoID != novoIDConfirmacao:
  
        header()
        print('\n**Menu - Alterar informações do administrador**\n')

        print('Informações digitadas são diferentes, tente novamente!')
        novoID = input('\n[0 - Menu] Digite o novo ID: ')

        if novoID == '0':
          menuAdministrador()

        novoIDConfirmacao = input('[0 - Menu] Digite o novo ID novamente: ')  

        if novoIDConfirmacao == '0':
          menuAdministrador()

      header()
      print('\n**Menu - Alterar informações do administrador**\n')
      print('-=' * 16)
      print('Antes:')
      print('-=' * 16)
      print('Nome: ', administrador.getNome())
      print('Telefone: ', administrador.getTelefone())
      print('ID: ', administrador.getId())
      print('-=' * 16)

      idAdministrador = novoID

      administrador.setId(novoID)

      atualizaIdAdmin()

      print('Depois:')
      print('-=' * 16)
      print('Nome: ', administrador.getNome())
      print('Telefone: ', administrador.getTelefone())
      print('ID: ', administrador.getId())
      print('-=' * 16)

      opcao = ''

      while opcao != '1':
        opcao = input('\nDigite 1 para voltar ao menu: ')

      menuPrincipal()

    elif opcao == 2:

      header()
      print('\n**Menu - Alterar informações do administrador**\n')

      novoNome = input('[0 - Menu] Digite o novo nome: ').upper()

      if novoNome == '0':
        menuAdministrador()

      novoNomeConfirmacao = input('[0 - Menu] Digite o novo nome novamente: ').upper()

      if novoNomeConfirmacao == '0':
        menuAdministrador()

      while novoNome != novoNomeConfirmacao:
  
        header()
        print('\n**Menu - Alterar informações do administrador**\n')

        print('Informações digitadas são diferentes, tente novamente!')
        novoNome = input('\n[0 - Menu] Digite o novo nome: ').upper()

        if novoNome == '0':
          menuAdministrador()

        novoNomeConfirmacao = input('[0 - Menu] Digite o novo nome novamente: ').upper()

        if novoNomeConfirmacao == '0':
          menuAdministrador()

      header()
      print('\n**Menu - Alterar informações do administrador**\n')
      print('-=' * 16)
      print('Antes:')
      print('-=' * 16)
      print('Nome: ', administrador.getNome())
      print('Telefone: ', administrador.getTelefone())
      print('ID: ', administrador.getId())
      print('-=' * 16)

      administrador.setNome(novoNomeConfirmacao)

      atualizaAdmin()

      print('Depois:')
      print('-=' * 16)
      print('Nome: ', administrador.getNome())
      print('Telefone: ', administrador.getTelefone())
      print('ID: ', administrador.getId())
      print('-=' * 16)

      opcao = ''

      while opcao != '1':
        opcao = input('\nDigite 1 para voltar ao menu: ')

      menuAdministrador()

    elif opcao == 3:

      header()
      print('\n**Menu - Alterar informações do administrador**\n')

      novoTelefone = input('[0 - Menu] Digite o novo telefone: ')

      if novoTelefone == '0':
        menuAdministrador()

      novoTelefoneConfirmacao = input('[0 - Menu] Digite o novo telefone novamente: ')

      if novoTelefoneConfirmacao == '0':
        menuAdministrador()

      while novoTelefone != novoTelefoneConfirmacao:
  
        header()
        print('\n**Menu - Alterar informações do administrador**\n')

        print('Informações digitadas são diferentes, tente novamente!')
        novoTelefone = input('\n[0 - Menu] Digite o novo telefone: ')

        if novoTelefone == '0':
          menuAdministrador()

        novoTelefoneConfirmacao = input('[0 - Menu] Digite o novo telefone novamente: ')

        if novoTelefoneConfirmacao == '0':
          menuAdministrador()

      header()
      print('\n**Menu - Alterar informações do administrador**\n')
      print('-=' * 16)
      print('Antes:')
      print('-=' * 16)
      print('Nome: ', administrador.getNome())
      print('Telefone: ', administrador.getTelefone())
      print('ID: ', administrador.getId())
      print('-=' * 16)

      administrador.setTelefone(novoTelefoneConfirmacao)

      atualizaAdmin()

      print('Depois:')
      print('-=' * 16)
      print('Nome: ', administrador.getNome())
      print('Telefone: ', administrador.getTelefone())
      print('ID: ', administrador.getId())
      print('-=' * 16)

      opcao = ''

      while opcao != '1':
        opcao = input('\nDigite 1 para voltar ao menu: ')

      menuAdministrador()

    elif opcao == 4:

      idAtual = '-1'
      while idAtual != idAdministrador:
  
        header()
        print('\n**Menu - Alterar informações do administrador**\n')

        idAtual = input('[0 - Menu] Digite o ID atual: ')

        if idAtual == '0':
          menuAdministrador()
          
      header()
      print('\n**Menu - Alterar informações do administrador**\n')

      novoID = input('[0 - Menu] Digite o novo ID: ')

      if novoID == '0':
        menuAdministrador()

      novoIDConfirmacao = input('[0 - Menu] Digite o novo ID novamente: ')

      if novoIDConfirmacao == '0':
        menuAdministrador()

      while novoID != novoIDConfirmacao:
        header()
        print('\n**Menu - Alterar informações do administrador**\n')

        print('Informações digitadas são diferentes, tente novamente!')
        novoID = input('\n[0 - Menu] Digite o novo ID: ')
        
        if novoID == '0':
          menuAdministrador()

        novoIDConfirmacao = input('[0 - Menu] Digite o novo ID novamente: ')
    
        if novoIDConfirmacao == '0':
          menuAdministrador()

      header()
      print('\n**Menu - Alterar informações do administrador**\n')

      novoNome = input('[0 - Menu] Digite o novo nome: ').upper()

      if novoNome == '0':
        menuAdministrador()

      novoNomeConfirmacao = input('[0 - Menu] Digite o novo nome novamente: ').upper()

      if novoNomeConfirmacao == '0':
        menuAdministrador()

      while novoNome != novoNomeConfirmacao:
        header()
        print('\n**Menu - Alterar informações do administrador**\n')

        print('Informações digitadas são diferentes, tente novamente!')
        novoNome = input('\nDigite o novo nome: ').upper()

        if novoNome == '0':
          menuAdministrador()

        novoNomeConfirmacao = input('Digite o novo nome novamente: ').upper()

        if novoNomeConfirmacao == '0':
          menuAdministrador()

      header()
      print('\n**Menu - Alterar informações do administrador**\n')

      novoTelefone = input('[0 - Menu] Digite o novo telefone: ')

      if novoTelefone == '0':
        menuAdministrador()

      novoTelefoneConfirmacao = input('[0 - Menu] Digite o novo telefone novamente: ')

      if novoTelefoneConfirmacao == '0':
        menuAdministrador()

      while novoTelefone != novoTelefoneConfirmacao:
        header()
        print('\n**Menu - Alterar informações do administrador**\n')

        print('Informações digitadas são diferentes, tente novamente!')
        novoTelefone = input('\n[0 - Menu] Digite o novo telefone: ')
        
        if novoTelefone == '0':
          menuAdministrador()

        novoTelefoneConfirmacao = input('[0 - Menu] Digite o novo telefone novamente: ')

        if novoTelefoneConfirmacao == '0':
          menuAdministrador()

      header()
      print('\n**Menu - Alterar informações do administrador**\n')
      print('-=' * 16)
      print('Antes:')
      print('-=' * 16)
      print('Nome: ', administrador.getNome())
      print('Telefone: ', administrador.getTelefone())
      print('ID: ', administrador.getId())
      print('-=' * 16)

      idAdministrador = novoID
      administrador.setId(novoID)
      administrador.setNome(novoNomeConfirmacao)
      administrador.setTelefone(novoTelefoneConfirmacao)

      atualizaAdmin()

      atualizaIdAdmin()

      print('Depois:')
      print('-=' * 16)
      print('Nome: ', administrador.getNome())
      print('Telefone: ', administrador.getTelefone())
      print('ID: ', administrador.getId())
      print('-=' * 16)

      opcao = ''

      while opcao != '1':
        opcao = input('\nDigite 1 para voltar ao menu: ')

      menuPrincipal()

    else:
      menuAdministrador()

  elif opcao == 7:

    menuPrincipal()

def menuInformacaoBiblioteca():

  opcao = 0

  while opcao < 1 or opcao > 2:
    
    header()
    print()
    print('Nome: ', biblioteca.getNome())
    print('Endereço: ', biblioteca.getEndereco())
    print('Telefone: ', biblioteca.getTelefone())
    print(f'\nEm caso de problemas entrar em contato com o administrador {administrador.getNome()}, Tel: {administrador.getTelefone()}')
    print('\n1 - Modificar informações (necessário ser administrador)')
    print('2 - Retornar ao menu')

    opcao = int(input('\nDigite uma opção: '))

  if opcao == 1:
    
    opcao = 0

    while opcao < 1 or opcao > 2:

      header()
      print('\n**Menu para modificação das informações da biblioteca**')
      print('!Lembre-se, é preciso ter acesso de ADMINISTRADOR!')
      opcao = int(input('\nDeseja retornar ao menu [1] ou prosseguir [2] ? '))

    if opcao == 1:
      menuPrincipal()

    elif opcao == 2:

      idInput = 0
      senhaInput = 0

      while validacaoLogin(3, idInput, senhaInput) == False:
  
        header()

        idInput = input('\n[0 - Menu] Digite o seu id: ')

        if idInput == '0':
          menuPrincipal()

        senhaInput = input('[0 - Menu] Digite a sua senha: ')

        if senhaInput == '0':
          menuPrincipal()

        validacaoLogin(3, idInput, senhaInput)

      opcao = 0

    opcao = 0

    while opcao < 1 or opcao > 5:

      header()
      print('\n**Menu - Alterar informações da biblioteca**\n')
      print('1 - Modificar nome')
      print('2 - Modificar endereço')
      print('3 - Modificar telefone')
      print('4 - Modificar todas as informações')
      print('5 - Retornar ao menu')

      opcao = int(input('\nDigite uma opção: '))

    if opcao == 1:

      header()
      print('\n**Menu - Alterar informações da biblioteca**\n')
      novoNomeBiblioteca = input('[0 - Menu] Digite o novo nome: ')

      if novoNomeBiblioteca == '0':
        menuPrincipal()

      header()
      print('\n**Menu - Alterar informações da biblioteca**\n')
      print('-=' * 16)
      print('Antes:')
      print('-=' * 16)
      print('Nome: ', biblioteca.getNome())
      print('Telefone: ', biblioteca.getTelefone())
      print('Endereço: ', biblioteca.getEndereco())
      print('-=' * 16)

      biblioteca.setNome(novoNomeBiblioteca)

      atualizaBiblioteca()

      print('Depois:')
      print('-=' * 16)
      print('Nome: ', biblioteca.getNome())
      print('Telefone: ', biblioteca.getTelefone())
      print('Endereço: ', biblioteca.getEndereco())
      print('-=' * 16)

      opcao = ''

      while opcao != '1':
        opcao = input('\nDigite 1 para voltar ao menu: ')

      menuPrincipal()

    elif opcao == 2:

      header()
      print('\n**Menu - Alterar informações da biblioteca**\n')
      novoEnderecoBiblioteca = input('[0 - Menu] Digite o novo endereço: ')

      if novoEnderecoBiblioteca == '0':
        menuPrincipal()

      header()
      print('\n**Menu - Alterar informações da biblioteca**\n')
      print('-=' * 16)
      print('Antes:')
      print('-=' * 16)
      print('Nome: ', biblioteca.getNome())
      print('Telefone: ', biblioteca.getTelefone())
      print('Endereço: ', biblioteca.getEndereco())
      print('-=' * 16)

      biblioteca.setEndereco(novoEnderecoBiblioteca)

      atualizaBiblioteca()

      print('Depois:')
      print('-=' * 16)
      print('Nome: ', biblioteca.getNome())
      print('Telefone: ', biblioteca.getTelefone())
      print('Endereço: ', biblioteca.getEndereco())
      print('-=' * 16)

      opcao = ''

      while opcao != '1':
        opcao = input('\nDigite 1 para voltar ao menu: ')

      menuPrincipal()

    elif opcao == 3:

      header()
      print('\n**Menu - Alterar informações da biblioteca**\n')
      novoTelefoneBiblioteca = input('[0 - Menu] Digite o novo telefone: ')

      if novoTelefoneBiblioteca == '0':
        menuPrincipal()

      header()
      print('\n**Menu - Alterar informações da biblioteca**\n')
      print('-=' * 16)
      print('Antes:')
      print('-=' * 16)
      print('Nome: ', biblioteca.getNome())
      print('Telefone: ', biblioteca.getTelefone())
      print('Endereço: ', biblioteca.getEndereco())
      print('-=' * 16)

      biblioteca.setTelefone(novoTelefoneBiblioteca)

      atualizaBiblioteca()

      print('Depois:')
      print('-=' * 16)
      print('Nome: ', biblioteca.getNome())
      print('Telefone: ', biblioteca.getTelefone())
      print('Endereço: ', biblioteca.getEndereco())
      print('-=' * 16)

      opcao = ''

      while opcao != '1':
        opcao = input('\nDigite 1 para voltar ao menu: ')

      menuPrincipal()

    elif opcao == 4:

      header()
      print('\n**Menu - Alterar informações da biblioteca**\n')

      novoNomeBiblioteca = input('[0 - Menu] Digite o novo nome: ')

      if novoNomeBiblioteca == '0':
        menuPrincipal()

      novoEnderecoBiblioteca = input('[0 - Menu] Digite o novo endereço: ')

      if novoEnderecoBiblioteca == '0':
        menuPrincipal()

      novoTelefoneBiblioteca = input('[0 - Menu] Digite o novo telefone: ')

      if novoTelefoneBiblioteca == '0':
        menuPrincipal()

      header()
      print('\n**Menu - Alterar informações da biblioteca**\n')
      print('-=' * 16)
      print('Antes:')
      print('-=' * 16)
      print('Nome: ', biblioteca.getNome())
      print('Telefone: ', biblioteca.getTelefone())
      print('Endereço: ', biblioteca.getEndereco())
      print('-=' * 16)

      biblioteca.setNome(novoNomeBiblioteca)      
      biblioteca.setEndereco(novoEnderecoBiblioteca)
      biblioteca.setTelefone(novoTelefoneBiblioteca)

      atualizaBiblioteca()

      print('Depois:')
      print('-=' * 16)
      print('Nome: ', biblioteca.getNome())
      print('Telefone: ', biblioteca.getTelefone())
      print('Endereço: ', biblioteca.getEndereco())
      print('-=' * 16)

      opcao = ''

      while opcao != '1':
        opcao = input('\nDigite 1 para voltar ao menu: ')

      menuPrincipal()

    else:
      menuPrincipal()

  elif opcao == 2:
    menuPrincipal()

def menuPrincipal():

  opcao = -1

  while opcao < 1 or opcao > 5:
    
    header()

    print('\n1 - Bibliotecário')
    print('2 - Membro')
    print('3 - Administrador')
    print('4 - Informações sobre a biblioteca')
    print('5 - Encerrar o programa')
    
    opcao = int(input('\nDigite uma opção: '))

  if opcao == 1:
    idInput = login(opcao)
    menuBibliotecario(idInput)

  elif opcao == 2:
    idInput = login(opcao)
    menuMembro(idInput)

  elif opcao == 3:
    login(opcao)
    menuAdministrador()

  elif opcao == 4:
    menuInformacaoBiblioteca()

  else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Programa encerrado')
    raise SystemExit

menuPrincipal()