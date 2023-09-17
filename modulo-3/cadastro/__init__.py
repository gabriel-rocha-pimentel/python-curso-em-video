def cadastrar(nome='<DESCONHECIDO>', idade=0, email='<DESCONHECIDO@GMAIL.COM>', usuario='<DESCONHECIDO>'):
      """
      :param nome: Insira seu Nome aqui;
      :param idade: Insira sua Idade aqui;
      :param email: Insira seu Email aqui;
      :param usuario: Insira seu Nome de Usuário aqui;
      :return: Será tetornado um arquivo de texto com as informações
      que foram pedidas anteriomente;
      """
      people = list()

      people.append(str(nome).strip())
      people.append(int(idade))
      people.append(str(email).strip())
      people.append(str(usuario).strip())
      return people


def listPeople(*people):
      for text in people:
            with open('cadastro.txt', 'w') as arquivo:
                  arquivo.write('LISTA DE CADASTRO\n')
                  arquivo.write(f'{text}\n')
