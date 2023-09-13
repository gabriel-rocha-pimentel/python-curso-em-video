from utilidadesCeV import moeda, dado

value = dado.leiaDinheiro('Digite o preço = R$ ')
float(value)
moeda.resumo(value, 80, 35)
