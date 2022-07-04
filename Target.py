"""
Gabriel de Almeida Gazziro
(16)936180401
gabgazziro@gmail.com
"""

###################### EXERCICIO 2 ######################

def fibo(num):
    a = 0
    b = 1
    lista = []
    while a <=num:
        lista.append(a)
        a, b = b, a + b
    print(lista)
    if num not in lista:
        print('Esse número NÃO existe na sequência')
    else:
        print("Esse número EXISTE na sequência")

###################### EXERCICIO 3 ######################


def distribuidora():
    import json
    import statistics
    lista_datas= []
    menor_valor = 99999999
    menor_dia = ""
    maior_valor = -1
    maior_dia = ""
    lista_valores = []
    lista_acima_media = []
    dias_sem_faturamento = []
    with open('Target/dados.json') as f:
        data = json.loads(f.read())
        for i in data:
            if i['valor'] != 0:
                lista_datas.append(i)
            else:
                dias_sem_faturamento.append(i)
        print("DIAS SEM FATURAMENTO: ",dias_sem_faturamento)
        for i in lista_datas:
            if i['valor'] < menor_valor:
                menor_valor = i['valor']
                menor_dia = i
        print("\nMENOR FATURAMENTO DO MÊS: ",menor_dia)
        for i in lista_datas:
            if i['valor'] > maior_valor:
                maior_valor = i['valor']
                maior_dia = i
        print("\nMAIOR FATURAMENTO DO MÊS: ",maior_dia)
        for i in lista_datas:
            lista_valores.append(i['valor'])
        media = statistics.mean(lista_valores)
        print("\nMEDIA FATURAMENTO MENSAL: ",media)
        
        for i in lista_datas:
            if i['valor'] > media:
                lista_acima_media.append(i)
        print("\nDIAS ACIMA DA MEDIA: ",lista_acima_media)

###################### EXERCICIO 4 ######################

def percentual():
    sp = 67836.43
    rj = 36678.66
    mg = 29229.88
    es = 27165.48
    outros = 19849.53
    somador = sp + rj+ mg+ es+ outros
    sp_percentual = (100*sp) /somador 
    rj_percentual = (100*rj) /somador 
    mg_percentual = (100*mg) /somador 
    es_percentual = (100*es) /somador 
    outros_percentual = (100*outros) /somador 
    
    print("\nSP ",sp_percentual,"%")
    print("\nRJ ",rj_percentual,"%")
    print("\nMG ",mg_percentual,"%")
    print("\nES ",es_percentual,"%")
    print("\nOUTROS ",outros_percentual,"%")
    print("\nPROVA REAL", sp_percentual + rj_percentual + mg_percentual + es_percentual + outros_percentual,"%")

###################### EXERCICIO 5 ######################

def inverte(palavra):
    invertedor = ""
    for i in palavra:
        invertedor = i + invertedor 
    print(invertedor)


escolha = int(input("Olá, qual exercício você deseja ver:\n1. Fibonacci\n2. Distribuidora\n3. Percentual\n4. Inverte\n0. Sair\nDigite apenas o número: "))
while escolha != 0:
    if escolha == 1:
        escolha_fibonacci = int(input("Escolha um número para checar se existe na sequência: "))
        fibo(escolha_fibonacci)
        escolha = int(input("Olá, qual exercício você deseja ver:\n1. Fibonacci\n2. Distribuidora\n3. Percentual\n4. Inverte\n0. Sair\nDigite apenas o número: "))

    if escolha == 2:
        distribuidora()
        escolha = int(input("Olá, qual exercício você deseja ver:\n1. Fibonacci\n2. Distribuidora\n3. Percentual\n4. Inverte\n0. Sair\nDigite apenas o número: "))

    if escolha == 3:
        percentual()
        escolha = int(input("Olá, qual exercício você deseja ver:\n1. Fibonacci\n2. Distribuidora\n3. Percentual\n4. Inverte\n0. Sair\nDigite apenas o número: "))

    if escolha == 4:
        inverte_palavra = input("Escolha uma palavra para invertê-la: ")
        inverte(inverte_palavra)
        escolha = int(input("Olá, qual exercício você deseja ver:\n1. Fibonacci\n2. Distribuidora\n3. Percentual\n4. Inverte\n0. Sair\nDigite apenas o número: "))
    if escolha == 0:
        exit()