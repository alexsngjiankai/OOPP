import shelve

meds = shelve.open('meds')
class medication():
    def __init__(self):
        self.med_name=""
        self.amount=0
        self.description=""
def add_medinfo(user,name, amount, description):
#=====================================For new users
    med=create_one_med(name,amount,description)
    list=[]
    list.append(med)
    meds[user] = med

def get_medinfo(name):
    return meds[name]

def create_one_med(name,amount,description):
    med = medication()
    med.med_name = name
    med.amount = amount
    med.description = description
    return med

def return_list_med():
    klist = list(meds.keys())
    x = []
    for i in klist:
        x.append(meds[i])
    return x