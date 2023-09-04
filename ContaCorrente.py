import Conta
class ContaCorrente(Conta):
    def __init__(self,numero,saldo,limiteAtual,limiteDaConta):
        super().__init__(numero,saldo)
        if self.saldo == 0:
            self.limiteDaConta = self.limiteDaConta
        self.limiteAtual = limiteAtual
     
    


    def ConsultarLimiteDaConta(self):
       return print(f"Limite da conta: {self.limiteDaConta}")
        
    def ConsultarSaldoTotal(self):
       return print(f"Saldo total: {self.saldo + self.limiteAtual}")
   
    def sacar(self,valor):
          if valor <= self.saldo + self.limiteAtual:
            if valor <= self.saldo:
                self.saldo -= valor
            else:
                valor_excedente = valor - self.saldo
                self.saldo = 0
                self.limiteAtual -= valor_excedente
            print(f"Saque de {valor} realizado.")
            
            print(f"Limite atual: {self.limiteAtual}")
            
    def depositar(self,valor):
        if self.limiteAtual < self.limiteDaConta:
            while self.limiteAtual == self.limiteDaConta:
                self.limiteAtual += self.limiteDaConta
            self.saldo += valor
