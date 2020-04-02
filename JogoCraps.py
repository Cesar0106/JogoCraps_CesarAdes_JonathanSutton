import random
quant_fichas = 20
print ("Bem vindo ao jogo de Craps! Nesse jogo voce poderá escolher entre 4 modalidades de apostas, sendo elas: Field, Twelve, Any Craps e Pass Line Bet. Você começara o jogo com 20 fichas, e ao chegar ao zero perderá.Você poderá sair do jogo ao digitar 'sair do jogo'.Por favor digite todos os camandos em lowercase(letra minuscula).Obrigado por jogar e bom jogo!")



while quant_fichas > 0:

    tipo_aposta = input("Qual tipo de aposta voce quer fazer? ")
    if tipo_aposta == "sair do jogo":
        print ("Obrigado por jogar! Você acabou com {0} fichas.".format(quant_fichas))
        break
    num_fichas = int(input("Quantas fichas voce quer apostar? "))
    
    sorteio = random.randint(2,12)
    if num_fichas > quant_fichas:
        print ("Voce não tem fichas suficientes.")
    elif tipo_aposta == 'twelve':
        if sorteio == 12:
            quant_fichas += (30*num_fichas)
            print ('O número sorteado foi {0}'.format(sorteio))
            print ('Você possui agora {0} fichas'.format(quant_fichas))

        if sorteio != 12:
            quant_fichas += (- num_fichas)
            print ('O número sorteado foi {0}'.format(sorteio))
            print ('Você possui agora {0} fichas'.format(quant_fichas))
    elif tipo_aposta == 'field':
        if sorteio == 12:
            quant_fichas += (3*num_fichas)
            print ('O número sorteado foi {0}'.format(sorteio))
            print ('Você possui agora {0} fichas'.format(quant_fichas))

        elif sorteio == 2:    
            quant_fichas += (num_fichas*2)
            print ('O número sorteado foi {0}'.format(sorteio))
            print ('Você possui agora {0} fichas'.format(quant_fichas))

        elif sorteio == 3 or sorteio == 4 or sorteio == 9 or sorteio == 10 or sorteio == 11:
            quant_fichas += num_fichas
            print ('O número sorteado foi {0}'.format(sorteio))
            print ('Você possui agora {0} fichas'.format(quant_fichas))
        elif sorteio == 5 or sorteio == 6 or sorteio == 7 or sorteio == 8:
            quant_fichas += (- num_fichas)
            print ('O número sorteado foi {0}'.format(sorteio))
            print ('Você possui agora {0} fichas'.format(quant_fichas))
    
    elif tipo_aposta == 'any craps':
        if sorteio ==2 or sorteio ==3 or sorteio == 12:
            quant_fichas += (7*num_fichas)
            print ('O número sorteado foi {0}'.format(sorteio))
            print ('Você possui agora {0} fichas'.format(quant_fichas))

        elif sorteio != 2 or sorteio != 3 or sorteio != 12:
            quant_fichas += (- num_fichas)
            print ('O número sorteado foi {0}'.format(sorteio))
            print ('Você possui agora {0} fichas'.format(quant_fichas))

    elif tipo_aposta == 'pass line bet':
        if sorteio == 7 or sorteio == 11:
            quant_fichas += num_fichas
            print ("A soma dos dados deu {0}".format(sorteio))
            print ("Voce tem {0} fichas".format(quant_fichas))
 
        elif sorteio == 2 or sorteio == 3 or sorteio == 12:
            quant_fichas += (- num_fichas)
            print ("A soma dos dados deu {0}".format(sorteio))
            print ("Voce tem {0} fichas".format(quant_fichas))

        elif sorteio == 4 or sorteio == 5 or sorteio == 6 or sorteio == 8 or sorteio == 9 or sorteio == 10:
            print ("A soma dos dados deu {0}".format(sorteio))
            print ("Voce passou para a fase point")
            sorteio2 = 0
            while sorteio2 != sorteio or sorteio2 != 7:
                sorteio2 = random.randint(2,12)
                if sorteio2 == sorteio:
                    quant_fichas += num_fichas
                    print ("A soma dos novos dados deu {0}".format(sorteio))
                    print ("Voce tem {0} fichas".format(quant_fichas))
                    break
                elif sorteio2 == 7:
                    quant_fichas += (-num_fichas)
                    print ("A soma dos novos dados deu {0}".format(sorteio2))
                    print ("Voce tem {0} fichas".format(quant_fichas))
                    break
