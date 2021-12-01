# -*- coding: utf-8 -*-
import secrets, string

def senha_tk(tamanho):
    pwd_char = string.ascii_letters + string.digits + ('!@#*'*3)
    pwd = ''.join(secrets.choice(pwd_char) for i in range(tamanho))
    return pwd

def criar_ramais():
    print('================= Criar Ramais em massa ==================')
    print('Quantos ramais deseja criar?')
    qtd = int(input())
    qtd = qtd if qtd > 0 else 1
    
    print('Qual o range inicial? (ex: 10x... 20x... 30x...)')
    ramal_inicial = int(input())
    ramal_inicial = ramal_inicial if ramal_inicial >0 else 1

    senha_padrao = False
    print('Deseja colocar uma senha aleatória?\nS / N?')
    senha_padrao = input()


    if qtd and ramal_inicial:
        ramais =""
        for cada in range(int(qtd)):
                senha = "DefinaSeuPadrao#{}".format(ramal_inicial)
                if senha_padrao.lower() in ['s', 'sim', 'y', 'yes']:
                    senha = senha_tk(6)
                ramal = """\n[{}]
type=friend
username={}
secret={}
dtmfmode=rfc2833
qualify=yes
nat=force_rport,comedia
host=dynamic
port=5060
context=rota-saida
insecure=invite
callgroup=1
pickupgroup=1
disallow=all
allow=ulaw
allow=alaw""".format(ramal_inicial, ramal_inicial, senha)
                ramal_inicial = ramal_inicial +1
                ramais = "{}\n{}".format(ramais, ramal)

        return ramais
if __name__ == '__main__':
    ramais = criar_ramais()
    criar_conf = open('ramais.conf', 'w')
    criar_conf.write(ramais)
    criar_conf.close()
    print('================= FINALIZADO !!! ==================')
