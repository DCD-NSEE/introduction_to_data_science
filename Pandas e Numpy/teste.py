class teste():
    def __init__(self):
        self.preparaPYNB1()
        # self.preparaPYNB3()

    def preparaPYNB1(self):
        self.resposta_1_1 = 272.25
        self.resposta_1_2_3 = 284.05584
        self.resposta_1_5 = 4.08248290463863
        self.respostas_PYNB1 = {'1_1': self.resposta_1_1,'1_2_3': self.resposta_1_2_3,'1_5': self.resposta_1_5}

    def preparaPYNB3(self):
        self.resposta_4_2 = [7, 9, 5, 2, 0]
        self.resposta_4_5a = True
        self.resposta_4_5b = True
        self.resposta_4_6a = True
        self.resposta_4_5b = True
        self.resposta_4_7 = 47
        self.respostas_PYNB3 = {'4_2': self.resposta_4_2,'4_5a': self.resposta_4_5a,'4_5b': self.resposta_4_5b,'4_6a': self.resposta_4_6a,'4_5b': self.resposta_4_5b,'4_7': self.resposta_4_7}


    def testa(self, nb, lista):
        if nb == 0:
            gabarito = self.respostas_PYNB1
        elif nb == 2:
            gabarito = self.respostas_PYNB3


        print("="*23)
        print("CORRIGINDO RESPOSTAS...")
        print("="*23)

        for i in range(len(lista)):
            print(f"Questão {list(gabarito.keys())[i]}: ")
            print("Correta" if lista[i] ==  list(gabarito.values())[i] else "Incorreta")







    
