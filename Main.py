class Main:

       def __init__(self, nome, datanasc, cpf, tel, saldo=float):
              self.Nome = nome
              self.DataNasc = datanasc
              self.CPF = cpf
              self.Tel = tel
              self.Saldo = saldo
       print('='*30)
       print('Banco OnlyCoins'.center(30))
       print('='*30)

       def imprimeDados(self):
              print( f'Nome: {self.Nome} \nData de nascimento: {self.DataNasc}'
                     f'\nCPF: {self.CPF} \nTelefone: {self.Tel} \nSaldo Disponível:R$ {self.Saldo}')



       def deposito(self, valor):
              self.Saldo += valor

       def saque(self, valor):
              while self.Saldo < valor:
                     print('Valor Insuficiente!')
              else:
                     self.Saldo -= valor
                        

#atribuir dados à conta
Dados = Main(nome='gian', datanasc='03/08/04', cpf='000.000.000-00', tel='(035)9.9706-1666', saldo=500)
       

#atribuir valores           
Dados.imprimeDados()
#depositar
Dados.deposito(valor = 0)
#saque
Dados.saque(valor = 510)



print('='*30)





 
