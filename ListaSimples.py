
# ai segue a lista simples encadeada, acredito não estar do melhor jeito, assim, desafio voces a melhorem-na :D

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
                # percorre ate achar o item a ser inserido da lista
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
        contador = 0
        while aux != None:
            print(contador, aux.getValor())
            aux = aux.getProx()
            contador += 1
        print("------")

    def remover(self, indice):
        # caso a lista nao tenha nada
        if self.getTam() == 0:
            print("lista vazia, remocao impossivel")
        else:
            if indice == 0:
                # remover o primeiro da lista
                self.prim = self.prim.getProx()
            elif (indice <= self.getTam() and indice > 0):
                # remover no meio e fim
                noAnterior = self.prim
                noAtual = self.prim.getProx()
                indiceAtual = 1
                # percorre ate achar o item a ser removido da lista
                while indiceAtual != None:
                    if indiceAtual == indice:
                        noAnterior.setProx(noAtual.getProx())
                        noAtual.setProx(None)
                        break
                    noAnterior = noAtual
                    noAtual = noAtual.getProx()
                    indiceAtual += 1
            else:
                # caso seja digitado um numero invalido
                print("Digite um numero que esteja dentro dos limites da lista!!!")
        self.tam -= 1

lista = ListaSimples()

lista.inserir("Denys Silva",0)
lista.inserir("Chris Redfield",1)
lista.inserir("Leon S. Kennedy",2)
lista.inserir("Ada Wong",3)
lista.inserir("Jack Krauser",4)
lista.inserir("Claire Redfield",5)
lista.inserir("Albert Wesker",6)
lista.inserir("Hunk",7)
lista.inserir("Ramon Salazar",8)
lista.mostrar()
lista.remover(8)
lista.mostrar()

'''
# removendo no inicio, fim e meio
lista.inserir("Denys Silva",0)
lista.inserir("Chris Headfield",1)
lista.inserir("Leon S. Kennedy",2)
lista.inserir("Veronica",3)
lista.inserir("Ada Wong",4)
lista.mostrar()
lista.remover(0)
lista.mostrar()
# inserindo no comeco, meio e fim
lista.inserir("Denys Silva",0)
lista.inserir("Chris Headfield",5)
lista.mostrar()
lista.inserir("Leon S. Kennedy",1)
lista.inserir("Veronica",3)
lista.inserir("Ada Wong",2)
lista.mostrar()
'''
