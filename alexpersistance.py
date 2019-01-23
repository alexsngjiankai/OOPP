import shelve

meds = shelve.open('meds')
class medication():
    def __init__(self):
        self.med_name=""
        self.amount=0
        self.description=""


def add_medinfo(user,name, amount, description):
#=====================================For new users
    exist=False
    for i in meds:

        if i == user:
            med = create_one_med(name, amount, description)
            list=meds[i]
            list.append(med)

            del meds[i]
            meds[i] = list
            exist=True


    if exist==False:
        med=create_one_med(name,amount,description)
        list=[]
        list.append(med)
        meds[user] = list

def get_medinfo(name):
    return meds[name]

def create_one_med(name,amount,description):
    med = medication()
    med.med_name = name
    med.amount = amount
    med.description = description
    return med

def return_list_med(user):
    for i in meds:
        if i ==user:
            return meds[i]

def delete_med(id):
    for i in meds:
        if id == i:
            del meds[id]
