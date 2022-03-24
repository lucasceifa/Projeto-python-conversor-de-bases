loop = 1
fim = 0
while loop == 1: #comeco loop
    num = input('Digite um número: ')
    i=0
    aa=0
    bb=len(num)-1
    print('''Tipo do seu numero: 
    [ 1 ] BINARIO - DECIMAL;
    [ 2 ] OCTAL - DECIMAL;
    [ 3 ] HEXADECIMAL - DECIMAL;
    [ 4 ] DECIMAL - BINÁRIO.
    [ 5 ] DECIMAL - OCTADECIMAL;
    [ 6 ] DECIMAL - HEXADECIMAL;
   ''')
    opcao = int(input("SUA OPCAO: "))

    if opcao == 1:
        i=0
        bb=0
        aa=len(num)-1
        if num.isdigit():
            while i < len(num):
                numa = int(num[i]) * 2 ** bb
                bb -= 1
                aa += numa
                i += 1
            else:
                print(aa)
                fim = str(input('Deseja continuar? [s] ou [n] '))
                if fim == 'n':
                    break
                else:
                    loop == 1
        else:
            print('Digite um número válido. ')

    if opcao == 2:
        i=0
        aa=0
        bb=len(num)-1
        if num.isdigit():
            while i < len(num):
                numa = int(num[i]) * 8 ** bb
                bb -= 1
                aa += numa
                i += 1
            else:
                print(aa)
                fim = str(input('Deseja continuar? [s] ou [n] '))
                if fim == 'n':
                    break
                else:
                    loop == 1
        else:
            print('Digite um número válido. ')
    if opcao == 4:
        resto = 0
        new = int(num)
        rest = []
        while new > 0:
            resto = new % 2
            new = new // 2
            rest.append(resto)
        else:
            print(rest[::-1])
            fim = str(input('Deseja continuar? [s] ou [n] '))
            if fim == 'n':
                break
            else:
                loop == 1
    if opcao == 5:
        resto = 0
        new = int(num)
        rest = []
        while new > 0:
            resto = new % 8
            new = new // 8
            rest.append(resto)
        else:
            print(rest[::-1])
            fim = str(input('Deseja continuar? [s] ou [n] '))
            if fim == 'n':
                break
            else:
                loop == 1








