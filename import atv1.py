from atv1 import cliente
from atv1 import conta
from atv1 import contaEspecial

#                                        ____________________________
#                                       | Orientação a objeto               |
#                                       | Polimofismo                              |
#                                       |____________________________|

joao = cliente("João da Silva", "555-1234")
maria = cliente("Maria da Silva", "999-4567")

print("Nome: {} Telefone: {}"
         .format(joao.nome,  joao.telefone))

print("Nome: {} Telefone: {}"
         .format(maria.nome,  maria.telefone))

conta1 = conta([joao], 1,1000)
conta2 = conta([joao,maria],2,500)
conta1.deposito(250)
conta1.saque(15)
conta2.saque(25)
conta1.extrato()
conta2.resumo()

contaE = contaEspecial([maria], 2, 100, 500)
contaE.saque(550)
contaE.extrato()
