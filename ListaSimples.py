
class No:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None

        # um no possui um valor e seu proximo 'companheiro'

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor

    def setProx(self, prox):
        self.prox = prox

    def getProx(self):
        return self.prox

class ListaSimples:
    def __init__(self):
        self.ultimo = self.prim = None
        self.tam = 0

    def getTam(self):
        return self.tam

    def inserir(self, valor, indice):
        novoNo = No(valor)
        # Se a lista está vazia, insere no inicio
        if self.getTam() == 0:
            self.indice = indice
            self.prim = self.ultimo = novoNo
        else:
            if indice == 0:
                # inserir no indice zero
                self.prox = self.prim
                self.prim = novoNo
                self.indice = indice
            elif indice >= self.getTam():
                # inserir no final
                self.ultimo.setProx(novoNo)
                self.ultimo = novoNo
            else:
                #inserir no meio
                noAnterior = self.prim
                noAtual = self.prim.getProx()
                indiceAtual = 1
                # percorre ate achar o item a ser removido da lista
                while indiceAtual != None:
                    if indiceAtual == indice:
                        novoNo.setProx(noAtual)
                        noAnterior.setProx(novoNo)
                    noAnterior = noAtual
                    noAtual = noAtual.getProx()
                    indiceAtual += 1
        self.tam += 1

    def mostrar(self):
        aux = self.prim
        print("------")
        while aux != None:
            print(aux.getValor())
            aux = aux.getProx()
        print("------")

lista = ListaSimples()
lista.inserir("Denys",0)
lista.inserir("Chris",1)
lista.inserir("Leon",2)
lista.inserir("Muller",3)
lista.inserir("Emanuel",4)
lista.mostrar()
