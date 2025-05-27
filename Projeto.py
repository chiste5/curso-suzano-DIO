from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime


class trasacoes(ABC):
   @abstractclassmethod
   def registrar(Conta):
      pass
      

class sacar(trasacoes):
    def __init__(self,_valor):
      self.valor = _valor

class depositar(trasacoes):
   def __init__(self,_valor):
      self.valor = _valor

class Cliente(trasacoes):
  def __init__(self,endereco,contas):
     self._endereco = endereco
     self._contas = contas
   

class Conta(Cliente):
    def __init__(self,saldo,agencia,numero,cliente,historico):
        self._saldo = saldo
        self._agencia = agencia
        self._numero = numero
        self._cliente = cliente
        self._historico = historico

    @property
    def saldo(self):
        return self._saldo
    
    def nova_conta(self,endereco,contas):
       super().__init__(endereco,contas)
       numero = self._numero

    def sacar(self):
       pass
    def depositar(self):
       pass


class Contacorrente(Conta):
   def __init__(self, saldo, agencia, numero, cliente, historico,limite,limite_saques):
      super().__init__(saldo, agencia, numero, cliente, historico)
      self.limite = limite
      self.limite_saques = limite_saques


class PessoaFisica(Cliente):
   def __init__(self,cpf,nome,data_nas):
      super().__init__()
      self.cpf = cpf
      self.nome = nome
      self.data_nas = data_nas
      
   