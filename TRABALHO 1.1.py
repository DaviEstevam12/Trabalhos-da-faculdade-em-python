class Pilha:
    def __init__(self, elementos = None):
        if isinstance(elementos, list):   #verificação se o objeto pertence a classe 
            self.elementos = elementos.copy()
            print(f"Pilha criada com sucesso, os elementos são {self.elementos}.")
        else:
            self.elementos = []
            print("Pilha criada: vazia")
    

    def empilhar(self, elementos):
        self.elementos.append(elementos)
        print(f"O objeto {self.elementos} foi empilhado a pilha.")


    def desempilhar(self,elementos):
        if self.elementos:
            removido = self.elementos.pop()
            print(f"O elementos {removido} foi removido da pilha.")
        else:
            print(f"Erro, pilha está vazia, não foi possível remover elementos.")
            return removido
        
    def lenPilha(self,elementos):
        return (len(self.elementos))
    
    def getPilha(self, elementos):
        copia = self.elementos.copy()
        print(copia)
    
    def __add__(self,other):
        if not isinstance(other, Pilha):
            print("Só é possível empilhar pilha com pilha")
            return None
        else:
            nova = self.getPilha() + other.Pilha()
        return nova
        
    


        
