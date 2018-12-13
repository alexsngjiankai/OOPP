import random
import shelve
import time



#ace Start
def give_random(num1,num2):
    E1=random.randint(num1,num2)


    return E1
storeE1=shelve.open("E1")
temStore=shelve.open('Chall')
#storeE2=shelve.open("E2")
#store_UAnswer=shelve.open("userAnswer")


class All():
    def __init__(self):
        self.EQ1=0
        self.EQ2=0
        self.A=0
        self.U=0
        self.S=""
        self.C=""
        self.timer=0
def store(E1,E2):

    all=All()
    all.EQ1=give_random(E1,E2)
    all.EQ2=give_random(E1,E2)

    while True:
        if all.EQ1<all.EQ2:
            all.EQ2 = give_random(E1, E2)
        else:
            break

    choosePlusMinus = give_random(1, 2)
    if choosePlusMinus == 1:
        all.S = "+"
        all.A = all.EQ1 + all.EQ2
    else:
        all.S = "-"
        all.A = all.EQ1 - all.EQ2
        while True:
            if all.A<=0:
                all.EQ1 = give_random(E1, E2)
                all.EQ2 = give_random(E1, E2)
                while True:
                    if all.EQ1 < all.EQ2:
                        all.EQ2 = give_random(E1, E2)
                    else:
                            break
                all.A = all.EQ1 - all.EQ2
            else:
                all.A = all.EQ1 - all.EQ2
                break
    #all.A=all.EQ1+all.EQ2
    number = str(len(storeE1))
    storeE1[number]=all


def storeUserAnswer(UserAnswer):
    while True:
        if str(UserAnswer).startswith("0"):
            UserAnswer=str(UserAnswer)[1:]
        else:
            number = str(len(storeE1)-2)
            all = storeE1[number]
            all.U = int(UserAnswer)

            if all.U==all.A:
                all.C="Correct"
            else:
                all.C="Incorrect"

            storeE1[number] = all
            break
def giveE1():
    number = str(len(storeE1)-1)
    all=storeE1[number]
    return all.EQ1

def giveE2():
    number = str(len(storeE1)-1)
    all=storeE1[number]
    return all.EQ2


def save_The_Time(timer):
    temStore["StoreTime"]=timer
def give_Back_Time():
    t=temStore["StoreTime"]
    return t



def checkrange():
    count=0
    listing=[]
    while True:
        if count!=len(storeE1):

            count+=1
        else:
            return count
def give_Sign():
    number = str(len(storeE1) - 1)
    all = storeE1[number]
    return all.S


def test_print():
    klist = list(storeE1.keys())
    x = []
    for i in klist:
        x.append(storeE1[i])
    return x

def delete_All():
    for i in storeE1:
        del storeE1[i]

    for i in temStore:
        del temStore[i]

def sendTitleCal():
    return "Cal"
class challage:
    def __init__(self):
        self.Start=0
        self.End=0
        self.Range=0
def settingChallage(Start,End,Range,Time):
    tem=challage()
    tem.Start=Start
    tem.End=End
    tem.Range=Range
    save_The_Time(Time)
    temStore['temCha']=tem
def ChallageStartInP():

    CQ=temStore['temCha']
    store(int(CQ.Start),int(CQ.End))

    return CQ.Range
def get_NumberOfQ():
    Q=temStore['temCha']
    return Q.Range
#ace END
