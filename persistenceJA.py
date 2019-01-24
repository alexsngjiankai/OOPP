import shelve

appointmentStorage=shelve.open("apStore")
class AppointmentStore():

    def __init__(self, location, date, timehour, reason, referral='NIL'):
        self.location = location
        self.date = date
        self.timehour = timehour
        self.reason = reason
        self.referral = referral

    def __str__(self):
        return 'Location: {}, Date: {} , Time: {}, scheme: {}'.format(self.location, self.date, self.timehour, self.reason, self.referral)


def generate_list():
        pass


def create_element(id, location, date, time ,reason, referral):
    exist=False
    for i in appointmentStorage:
        if i == id:
            listvalue=appointmentStorage[id]
            tst=AppointmentStore(location,date,time,reason, referral)
            listvalue.append(tst)
            del appointmentStorage[id]
            appointmentStorage[id]=listvalue
            exist=True

    if exist==False:
        list=[]

        tst = AppointmentStore(location, date, time, reason, referral)
        list.append(tst)
        appointmentStorage[id]=list


def send_appointment(user):

    x = appointmentStorage[user]
    return x
