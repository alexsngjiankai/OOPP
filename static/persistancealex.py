from datetime import datetime

class medicationinput:
    def __init__(self, name, amount, description):
        self.__name = name
        self.__amount = amount
        self.__description = description

    def get_name(self):
        return self.__name

    def get_amount(self):
        return self.__amount

    def get_description(self):
        return self.__description

    def set_name(self):
        self.__name = name

    def set_amount(self):
        self.__amount = amount

    def set_description(self):
        self.__description = description

class medtable(medicationinput):
    def __init__(self, name, amount, description, date, tablelength):
        medicationinput.__init__(self, name, amount, description)
        self.__date = ''
        self.set_date = date
    def get_date(self):
        return self.__date
    def set_date(self):
        if date_diff == '-1':
            #clear the date in the table

    def get_tablelength(self):
        return self.__tablelength

    def set_tablelength(self):
        self.__tablelength = tablelength
        if tablelength > '7':
            #hide table columns over index 7

#end of classes


#functions

def date_diff():
    diff = table_date - datetime.now()



def checktable():












