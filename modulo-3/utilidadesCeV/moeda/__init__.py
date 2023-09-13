def metade(num, text_format=True):
      resp = num // 2

      if text_format:
            resp = f'R$ {resp:2.0f},00'
      return resp


def dobro(num, tex_format=True):
      resp = num * 2

      if tex_format:
            resp = f'R$ {resp:2.0f},00'
      return resp


def aumentar(prec=0, por_cent=10, text_format=True):
      value = (prec / 100) * por_cent
      resp = prec + value

      if text_format:
            resp = f'R$ {resp:2.0f},00'
      return resp


def reduzir(prec=0, por_cent=10, text_format=True):
      value = (prec / 100) * por_cent
      resp = prec - value

      if text_format:
            resp = f'R$ {resp:2.0f},00'
      return resp


def moeda(num):
      text = f'R$ {num:2.0f},00'
      return text


def resumo(prec, por_cent_max, por_cent_min):
      print(f'{"_" * 50}\n{"RESUMO DO VALOR":^50}\n{"_" * 50}')
      print(f'{"Preço analisado:":<25} {moeda(prec):<25}')
      print(f'{"Dobro do preço:":<25} {dobro(prec):<25}')
      print(f'{"Metade do preço:":<25} {metade(prec):<25}')
      print(f'{str(por_cent_max) + "% de aumento:":<25} R$ {aumentar(prec, por_cent_max, text_format=True):<25}')
      print(f'{str(por_cent_min) + "% de redução:":<25} R$ {reduzir(prec, por_cent_min, text_format=True)}')
      print('_' * 50)
