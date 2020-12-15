
# esse arquivo está apenas inserindo
# ainda irei termina-lo, se quiser praticar faça vc mesmo a funcao remover(), fica como licao de casa :)

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
                novoNo.setProx(self.prim)
                self.prim = novoNo
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
                        break
                    noAnterior = noAtual
                    noAtual = noAtual.getProx()
                    indiceAtual += 1
        self.tam += 1

    def mostrar(self):
        aux = self.prim
        while aux != None:
            print(aux.getValor())
            aux = aux.getProx()
        print("------")

    # todo metodo a ser feito
    def remover(self, indice):
        if self.getTam() == 0:
            print("lista vazia, remocao impossivel")
        else:
            if indice == 0:
                # remover no indice zero
                self.prim = self.prim.getProx()
                #novoNo.setProx(self.prim)
                #self.prim = novoNo
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
                        break
                    noAnterior = noAtual
                    noAtual = noAtual.getProx()
                    indiceAtual += 1
        self.tam += 1

lista = ListaSimples()
lista.inserir("Denys Silva",0)
lista.inserir("Chris Headfield",1)
lista.inserir("Leon S. Kennedy",2)
lista.inserir("Veronica",1)
lista.mostrar()

lista.remover(0)
lista.mostrar()



