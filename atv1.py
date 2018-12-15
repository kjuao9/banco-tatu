class tatu():
    def __init__(self, nome, telefone):

        self.nome = nome
        self.telefone = telefone

    def conta():
        saldo = int(input("Digite o seu saldo: "))
        sd = 0
        sq = 0
        somadeposito = 0
        somasaque = 0
        while True:
            print("""
                     1 - Saque
                     2 - Depósito
                     3 - Sair
                    """)
            op = int(input("Digite a opção que deseja realizar: "))
            if op == 1:
                saque = int(input("Digite a quantia que deseja sacar: "))
                if saque >= saldo:
                    print("""---Operação Inválida---
                            Não pode sacar uma quantia maior que o seu saldo.
                            """)
                if saque < saldo:
                    saldo = saldo - saque
                    sq = sq + 1
                    somasaque = somasaque + saque
                    
            if op == 2:
                deposito = int(input("Digite a quantia que deseja depositar: "))
                saldo = saldo + deposito
                sd = sd + 1
                somadeposito = somadeposito + 1
                
            if op == 3:
                break
        print("Nº: ",self.telefone,"Nome: ",self.nome,"O seu saldo é de",saldo,"R$, você realizou ",sq,"saques, somando",somasaque,"R$, você tambem realizou",sd,"depósitos, somando",somadeposito,"R$.")
                
        
