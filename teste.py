class teste():
    def __init__(self):
        self.preparaPYNB1()
        self.preparaPYNB2()
        self.preparaPYNB3()

    def preparaPYNB1(self):
        self.resposta_2_3 = 100*(1.1**25)
        self.respostas_PYNB1 = {'2_3': self.resposta_2_3}

    def preparaPYNB2(self):
        self.resposta_2_7 = True+True 
        self.resposta_2_10 = (" ".join([str(i) for i in range(100, 1001,100)])).replace(" ",',')
        self.respostas_PYNB2 = {'2_7': self.resposta_2_7,'2_10': self.resposta_2_10}
    
    def preparaPYNB3(self):
        self.resposta_3_1 = "Hello world".find("r")
        self.resposta_3_2 =  'The white spaces in this string must be replaced by underscores.'.replace(" ","_")
        self.resposta_3_4 = {'SP': 45538936, 'RJ': 17159960, 'MG': 21040662, 'BA': 14812617}
        self.resposta_3_5 = self.resposta_3_4['PR'] = 11348937
        self.resposta_3_10 = [1, 0, 2, 4, 8, 1, 7, 1]
        self.respostas_PYNB3 = {'3_1' : self.resposta_3_1,'3_2': self.resposta_3_2,'3_4': self.resposta_3_4,'3_5': self.resposta_3_5,'3_10': self.resposta_3_10}

    def preparaPYNB4(self):
        self.resposta_4_1 = [7, 9, 5, 2, 0]
        self.resposta_4_5a,self.resposta_4_5b,self.resposta_4_6a,self.resposta_4_5b = True
        self.resposta_4_7 = 47
        self.respostas_PYNB3 = {'4_1': self.resposta_4_1,'4_5a': self.resposta_4_5a,'4_5b': self.resposta_4_5b,'4_6a': self.resposta_4_6a,'4_5b': self.resposta_4_5b,'4_7': self.resposta_4_7}


    def testa(self, nb, lista):
        if nb == 0:
            gabarito = self.respostas_PYNB1
        elif nb == 1:
            gabarito = self.respostas_PYNB2
        elif nb == 2:
            gabarito = self.respostas_PYNB3

        print("="*23)
        print("CORRIGINDO RESPOSTAS...")
        print("="*23)

        for i in range(len(lista)):
            print(f"Questão {list(gabarito.keys())[i]}: ")
            print("Correta" if lista[i] ==  list(gabarito.values())[i] else "Incorreta")







    
