from abc import ABC, abstractmethod

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Sacar(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta._saldo -= self.valor  # Exemplo simplificado

class Depositar(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta._saldo += self.valor

class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def adicionar_conta(self, conta):
        self._contas.append(conta)

class Conta:
    def __init__(self, saldo, agencia, numero, cliente, historico):
        self._saldo = saldo
        self._agencia = agencia
        self._numero = numero
        self._cliente = cliente
        self._historico = historico

    @property
    def saldo(self):
        return self._saldo

class ContaCorrente(Conta):
    def __init__(self, saldo, agencia, numero, cliente, historico, limite, limite_saques):
        super().__init__(saldo, agencia, numero, cliente, historico)
        self.limite = limite
        self.limite_saques = limite_saques

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nas, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nas = data_nas
