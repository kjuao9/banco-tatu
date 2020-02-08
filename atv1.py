class cliente():
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        
class conta():
    def __init__(self, clientes, numero, saldo = 0):
        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.historico = list()
        self.deposito(saldo)

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.historico.append(["Saque",valor])

    def deposito(self, valor):
        self.saldo += valor
        self.historico.append(["Depósito",valor])


    def resumo(self):
        print('CC Número: {} Saldo: R$ {}'
                .format(self.numero, self.saldo))

    def extrato(self):
        print("-"*30)
        print("Extrato CC Nº: {}".format(self.numero))
        print("-"*30)
        for op in self.historico:
            print("{}\t R$ {}".format(op[0], op[1]))
            print("Saldo: {}".format(self.saldo))

class contaEspecial(conta):
    def __init__(self, clientes, numero, saldo = 0, limite = 0):
        conta.__init__(self, clientes, numero, saldo)
        self.limite = limite
      

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.historico.append(["Saque",valor])

        

