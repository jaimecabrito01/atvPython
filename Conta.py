class Conta:
    def __init__(self,numero,saldo):
        self.numero = numero
        self.saldo = saldo



    def consultarSaldo(self):
        return self.saldo
    
    def depositar(self,valorDeposito):
        if valorDeposito >0:
            self.saldo += valorDeposito
            return True
        else:
            return False
    
    def sacar(self,valorSaque):
        if valorSaque <= self.saldo:
            self.saldo -= self.saldo
            return True
        else:
            return False
