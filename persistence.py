import random
import shelve
import time



#Ace Start
def give_random(num1,num2):
    E1=random.randint(num1,num2)


    return E1
storeE1=shelve.open("E1")
temStore=shelve.open('Chall')
History_All_Game = shelve.open('HistoryOfAllGame')
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
        self.diff=""
def store(E1,E2,diff):

    all=All()
    all.EQ1=give_random(E1,E2)
    all.EQ2=give_random(E1,E2)
    all.diff=diff
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
class Guess(challage):
    def __init__(self):
        super().__init__()
        self.Time=0
def settingChallage(Start,End,Range,Time):
    if give_App_Name()=="Cal":
        tem=challage()
        tem.Start=Start
        tem.End=End
        tem.Range=Range
        save_The_Time(Time)
        temStore['temCha']=tem
    else:
        tem=Guess()
        tem.Start=Start
        tem.End=End
        tem.Range=Range
        tem.Time=Time
        temStore['temGuess']=tem
def ChallageStartInP():

    CQ=temStore['temCha']
    store(int(CQ.Start),int(CQ.End),"challenge")

    return CQ.Range
def get_NumberOfQ():
    Q=temStore['temCha']
    return Q.Range

def Store_game_name(name):

    temStore["AppName"]=name

def give_App_Name():
    theName=temStore["AppName"]
    return theName

def StoreHistory(id):
    exist=False
    for i in History_All_Game:
        if i == id:
            All_History=History_All_Game[i]#take first dict value
            for o in All_History:
                if o == give_App_Name():
                    All_content=All_History[o]#take second dict value
                    if len(All_content)==3:#not done
                        del All_content[0]
                        current_List=test_print()
                        del current_List[-1]
                        All_content.append(current_List)


                        All_History[give_App_Name()] = All_content

                        del History_All_Game[id]
                        History_All_Game[id] = All_History
                        exist = True

                        break
                    else:#working

                        current_List = test_print()
                        del current_List[-1]

                        All_content.append(current_List)

                        All_History[give_App_Name()]=All_content

                        del History_All_Game[id]
                        History_All_Game[id] =All_History
                        exist = True

                        break

            break
    if exist==False:#working
        dict_Tem = {}
        list_Tem = []
        current_List = test_print()
        del current_List[-1]
        App_name = give_App_Name()
        list_Tem.append(current_List)

        if id in History_All_Game:
            haveData=History_All_Game[id]
            haveData[give_App_Name()] = list_Tem
            del History_All_Game[id]
            History_All_Game[id] = haveData
        else:

            dict_Tem[App_name] = list_Tem

            History_All_Game[id] = dict_Tem


def give_history_cal(id,GameName):
    have=False

    for d in History_All_Game:
        if d== id:

            dict_IThink=History_All_Game[id] #take first dic value
            for i in dict_IThink:
                if i == GameName:
                    The_list=dict_IThink[i]# got two list in here take second dict value
                    have=True
                    return The_list

    if have==False:
        return ""


class guess_Number:
    def init(self):
        self.Question=0
        self.User_answer=0
        self.diff=""
        self.correction=""

def generate_Guess(start,end,diff):


    generated_num=give_random(start,end)

    guess=guess_Number()
    guess.Question=generated_num
    guess.User_answer=0
    guess.diff=diff
    storeE1[str(len(storeE1))]=guess



def send_guess_num():
    showcurrent=str(len(storeE1)-1)
    number=storeE1[showcurrent]
    return number.Question


def send_guess_list_amount():
    number=len(storeE1)-1
    return number

def store_answer(answer):
    count=0
    del storeE1[str(len(answer)+1)]
    del storeE1[str(len(answer))]
    for i in storeE1:
        value=storeE1[i]
        if value.User_answer == 0:
            while True:
                if answer[count].startswith("0"):
                    print("test1")
                    print(answer[count])
                    answer[count] = answer[count][1:]
                else:
                    print(answer[count])
                    print("test2")

                    value.User_answer = answer[count]
                    break
            if int(answer[count])==int(value.Question):
                value.correction="Correct"
            else:
                value.correction="Incorrect"
            storeE1[i]=value
        count+=1
    #Past work
   # for i in storeE1:

   #     if storeE1[i].User_answer==0:

     #       storeE1[i].User_answer=answer
     #       break
     #   count+=1


def storeGuessHistory(id):
    exist = False
    for i in History_All_Game:
        if i == id:
            All_History = History_All_Game[i]  # take first dict value
            for o in All_History:
                if o == give_App_Name():
                    All_content = All_History[o]  # take second dict value
                    if len(All_content) == 3:  # done
                        del All_content[0]
                        current_List = test_print()
                        All_content.append(current_List)



                        All_History[give_App_Name()] = All_content


                        del History_All_Game[id]
                        History_All_Game[id] = All_History
                        exist = True

                        break
                    else:  # working

                        current_List = test_print()

                        All_content.append(current_List)

                        All_History[give_App_Name()] = All_content

                        del History_All_Game[id]
                        History_All_Game[id] = All_History
                        exist = True

                        break

            break
    if exist == False:  # working

        dict_Tem = {}
        list_Tem = []
        current_List = test_print()
        App_name = give_App_Name()
        list_Tem.append(current_List)



        if id in History_All_Game:
            haveData = History_All_Game[id]
            haveData[give_App_Name()]=list_Tem
            del History_All_Game[id]
            History_All_Game[id]=haveData
        else:

            dict_Tem[App_name] = list_Tem

            History_All_Game[id] = dict_Tem


def start_challage_guess():
    data=temStore['temGuess']

    generate_Guess(int(data.Start),int(data.End),"challenge")
def give_back_time_guess():
    data = temStore['temGuess']

    return data.Time
def give_back_range_guess():
    data = temStore['temGuess']

    return data.Range



#Ace END



def sendImgToTem(img):
    temStore["test1"]=img

def testShowImg():
    tem=temStore["test1"]
    return tem




