import shelve

meds = shelve.open('meds')

def add_medinfo(name, amount, description):
    meds[name] = [name, amount, description]

def get_medinfo(name):
    return meds[name]