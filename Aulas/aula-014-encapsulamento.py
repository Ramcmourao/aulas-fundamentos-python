# Como crio uma class?
class Conta:
    def __init__(self):
        self.__titular = 'Ricardo'
        self.__saldo = 500
        self.__pin = '1234'
        self.__limite = 400

    @property
    def titular(self):
        print('Fui buscar indiretamente')
        return self.__titular

    @titular.setter
    def titular(self, novo_titular):
        self.__titular = novo_titular

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        self.__saldo = valor


    @property
    def pin(self):
        return None


    @pin.setter
    def pin(self, novo_pin):
        self.__pin = novo_pin

    def altera_pin(self):
        pin_antigo = input('Digite o PIN antigo: ')
        if pin_antigo == self.__pin:
            novo_pin = input('Digite o novo PIN: ')
            novo_repete = input('Digite novamente o novo PIN: ')
            if novo_pin == novo_repete:
                self.pin = novo_pin
                print('PIN alterado com sucesso.')
            else:
                print('PIN distinto.')
        else:
            print('PIN antigo inválido.')

    @property
    def limite(self):
        return self.__limite



class ATM:
    def __init__(self, conta: Conta):
        self.conta = conta
        self.acesso = False


    def depositar(self):
        valor_depositar = float(input('Valor a depositar: '))
        self.conta.saldo = valor_depositar
        print('Saldo atualizado')


    def levantar(self):
        valor_levantar = float(input('Valor a levantar: '))
        if  valor_levantar <= self.conta.limite:
            self.conta.saldo = self.conta.saldo - valor_levantar
            print('Levantamento efetuado com sucesso!')
        else:
            print(f'Só pode levantar até {self.conta.limite:.2f}€')

    def mostra_saldo(self):
        print(self.conta.saldo)

    def menu(self):
        while True:
            print('[ 1 ] - Levantamentos')
            print('[ 2 ] - Depósitos')
            print('[ 3 ] - Ver saldo')
            print('[ 4 ] - Sair')

            opcao = int(input('--> '))

            if opcao == 1:
                self.levantar()
            elif opcao == 2:
                self.depositar()
            elif opcao == 3:
                self.mostra_saldo()
            elif opcao == 4:
                break


def main():
    nova_conta = Conta()
    atm = ATM(nova_conta)
    atm.menu()

if __name__ == '__main__':
    main()
