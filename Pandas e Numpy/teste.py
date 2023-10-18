class teste():
    def __init__(self):
        self.preparaPYNB1()

    def preparaPYNB1(self):
        self.resposta_1_1 = 272.25
        self.resposta_1_2_3 = 284.05584
        self.resposta_1_5 = 4.08248290463863
        self.respostas_PYNB1 = {'1_1': self.resposta_1_1,'1_2_3': self.resposta_1_2_3,'1_5': self.resposta_1_5}

   

    def testa(self, nb, lista):
        if nb == 0:
            gabarito = self.respostas_PYNB1



        print("="*23)
        print("CORRIGINDO RESPOSTAS...")
        print("="*23)

        for i in range(len(lista)):
            print(f"Questão {list(gabarito.keys())[i]}: ")
            print("Correta" if lista[i] ==  list(gabarito.values())[i] else "Incorreta")







    
