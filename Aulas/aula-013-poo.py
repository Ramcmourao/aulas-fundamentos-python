# Criar uma conta bancária
from traceback import print_tb

#titular
#saldo
#iban
#limite

#levantar/sacar
#consultar saldo
#depositar

class Conta:
    def __init__(self, titular, saldo, iban):
        self.titular = titular
        self.saldo = saldo
        self.iban = 'PT50123456' + iban
        self.limite = 400
        self.pin = '1234'

    def levantar(self, valor):
        if valor > self.limite:
            print('Só pode levantar até 400€ por dia')
        else:
            pin = input('Digite o pin: ')
            if pin == self.pin:
                self.saldo -= valor
                print('Valor levantado com sucesso')
            else:
                print('Erro no pin')

    def consultar_saldo(self):
        print(f'Olá {self.titular}, o seu saldo é de {self.saldo:.2f}€')

nova_conta = Conta('Ricardo', 500, '789')
outra_conta = Conta('Purfazz', 20, '987')

nova_conta.levantar(20)
outra_conta.levantar(10)

nova_conta.consultar_saldo()
outra_conta.consultar_saldo()