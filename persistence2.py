import random
import shelve
import time

class diffcuity:
    def __init__(self, game, difficuity):
        self.__difficuity = difficuity
        self.__game = game

    def get_game(self):
        return self.__game

    def get_difficuity(self):
        return self.__difficuity

    def set_game(self, game):
        self.__game = game

    def set_difficuty(self, gameMode):
        self.__difficuity = gameMode
class tester:

    def __init__(self,diff,test1=0,test2=0):
        self.__test1=test1
        self.__test2=test2
        self.__answer=0
        self.__answer2=0
        self.Calgame(diff)
    def Calgame(self,diff):

        self.__answer=random.randint(self.__test1,self.__test2)
        self.__answer2 = random.randint(self.__test1, self.__test2)

        while True:
            if self.__answer<self.__answer2:
                self.__answer2 = random.randint(self.__test1, self.__test2)
                continue
            else:
                break

                # return "%d + %d"%(r,r2)
    def get_answer1(self):
        return self.__answer
    def get_answer2(self):
        return self.__answer2
    Num1Cal = shelve.open('Num1Cal')
    Num2Cal = shelve.open('Num2Cal')
    Total = shelve.open('TotalCal')
    userAnswer=shelve.open('UserAnswer')
    testList=[]
    testList2=[]
    def storeNum(self):
        if len(tester.Num1Cal)==0:
            tester.testList.append(self.get_answer1())
            tester.testList2.append(self.get_answer2())
            tester.Num1Cal[0]=tester.testList
            tester.Num2Cal[0] =tester.testList2
        else:
            for i in tester.Num1Cal:
                testing=tester.Num1Cal[i].append(self.get_answer1())
                tester.Num1Cal[0] =testing
            for i in tester.Num2Cal:
                testing = tester.Num2Cal[i].append(self.get_answer2())
                tester.Num2Cal[0] = testing
        if len(tester.Num2Cal)==0:
                print("klkl")
        return tester.Num1Cal
    def AllAnsCal(self):
        num=0
        for i in tester.Num1Cal:
            for u in tester.Num2Cal:
                answer=tester.Num1Cal[i]+tester.Num2Cal[u]
                tester.Total[num]=answer
                num+=1


    def deleteAll(self):
        tester.Num1Cal={}
        tester.Num2Cal={}
        tester.Total={}
        tester.userAnswer={}
