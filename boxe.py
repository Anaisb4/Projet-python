from time import sleep
from random import randint

class Boxer:
    name = ""
    health = 0
    strenght = 0
    speed = 0
    dodge = 0


    def __init__(self, name, health, strength, speed, dodge):
        self.name = name
        self.health = health
        self.strenght = strength
        self.speed = speed
        self.dodge = dodge

    def hit(self, opponent):
        self.opponent = opponent
        luck = 100 - opponent.dodge

        rand = randint(1, 100)

        if(rand <= luck):
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            print(self.name + " reussit son coup !")
            self.opponent.health = self.opponent.health - opponent.strenght
            opponent.isKo()
        else:
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            print(self.name + " rate son coup..")


    def isKo(self):
        if(self.health <= 0):
            return True
        else:
            return False

def fight(boxer1, boxer2):
        while not boxeur_1.isKo() and not boxeur_2.isKo():
            if not boxeur_1.isKo():
                boxeur_1.hit(boxeur_2)
                print(boxeur_1.name + ": " + str(boxeur_1.health) + "pv  /  " + boxeur_2.name + ": " + str(boxeur_2.health) + "pv")
                sleep(1)
            if not boxeur_2.isKo():
                boxeur_2.hit(boxeur_1)
                print(boxeur_1.name + ": " + str(boxeur_1.health) + "pv  /  " + boxeur_2.name + ": " + str(
                    boxeur_2.health) + "pv")
                sleep(1)

        if(boxeur_1.isKo()):
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            print(boxeur_2.name+ " gagne le match")
        else :
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            print(boxeur_1.name + " gagne le match.")

boxeur_1 = Boxer("Boxeur 1", 100, 10, 50, 50)
boxeur_2 = Boxer("Boxeur 2", 100, 10, 50, 50)



fight(boxeur_1, boxeur_2)


