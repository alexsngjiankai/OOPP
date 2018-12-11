class medtable:
    def __init__(self,medname, meddate, meddescription, medamount):
        self.__medname = medname
        self.__meddate = meddate
        self.__meddescription = meddescription
        self.__medamount = medamount

    def get_medname(self):
        return self.__medname

    def set_medname(self, medname):
        self.__medname = medname

    def get_meddate(self):
        return self.__meddate

    def set_meddate(self,meddate):
        self.__meddate = meddate

    def get_meddescription(self):
        return self.__meddescription

    def set_meddescription(self, meddescription):
        self.__meddescription = meddescription

    def get_medamount(self):
        return self.__medamount

    def set_medamount(self, medamount):
        self.__medamount = medamount



