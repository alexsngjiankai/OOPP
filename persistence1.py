import shelve
import uuid
from datetime import date
# today = str(date.today())

class User:
    def __init__(self, id):
        self.__id = id
        self.__username = ''
        self.__password = ''
        self.__name = ''
        self.__age = ''
        self.__contactnumber = ''
        self.__doctor = ''
        self.__hospital = ''
        self.__firstvisit = ''
        self.__language = ''

    def get_id(self):
        return self.__id

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_contactnumber(self, contactnumber):
        self.__contactnumber = contactnumber

    def set_doctor(self, doctor):
        self.__doctor = doctor

    def set_hospital(self, hospital):
        self.__hospital = hospital

    def set_firstvisit(self, firstvisit):
        self.__firstvisit = firstvisit

    def set_language(self, language):
        self.__language = language

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_contactnumber(self):
        return self.__contactnumber

    def get_doctor(self):
        return self.__doctor

    def get_hospital(self):
        return self.__hospital

    def get_firstvisit(self):
        return self.__firstvisit

    def get_language(self):
        return self.__language

class Blog:
    def __init__(self, id):
        self.id = id
        self.username = ''
        self.title = ''
        self.body = ''
        self.created = ''

users = shelve.open('user')
blogs = shelve.open('blog')

def create_blog(username, title, body):
    id = str(uuid.uuid4())
    blog = Blog(id)
    blog.title = title
    blog.username = username
    blog.body = body
    blog.created = str(date.today())
    blogs[id] = blog

def update_blog(blog):
    blogs[blog.id] = blog

def delete_blog(id):
    if id in blogs:
        del blogs[id]

def get_blogs():
    klist = list(blogs.keys())
    x = []
    for i in klist:
        x.append(blogs[i])
    return x

def get_blog(id):
    if id in blogs:
        return blogs[id]

def create_user(username, password, name, age, contactnumber, doctor, hospital, firstvisit, language):
    id = str(uuid.uuid4())
    user = User(id)
    user.set_username(username)
    user.set_password(password)
    user.set_name(name)
    user.set_age(age)
    user.set_contactnumber(contactnumber)
    user.set_doctor(doctor)
    user.set_hospital(hospital)
    user.set_firstvisit(firstvisit)
    user.set_language(language)
    users[id] = user

def get_user(username, password):
    klist = list(users.keys())
    for key in klist:
        user = users[key]
        print(user.get_username(), username, user.get_password())
        if user.get_username() == username and user.get_password() == password:
            return user
    return None

def update_user(id, user):
    users[id] = user
    return users[id]

def clear_user():
    klist = list(users.keys())
    for key in klist:
        del users[key]

def clear_blog():
    klist = list(blogs.keys())
    for key in klist:
        del blogs[key]

def add_user(user):
    users[user.get_id()] = user

def init_db():
    clear_user()
    clear_blog()
    for i in range(5):
        create_user('user'+str(i), 'pass'+str(i))
        create_blog('user'+str(i), 'title'+str(i), 'body'+str(i))



def check_hosipital(hospital):
    if hospital == "Khoo Teck Puat":
        hospitalcontact = '6555 8000'
        return hospitalcontact
    if hospital == "Tan Tock Seng":
        hospitalcontact = '6256 6011'
        return hospitalcontact
    return "none"

def check_doctor(doctor):
    if doctor == 'Dr Tan':
        doctorcontact = '9856 2560'
        return doctorcontact
    if doctor == "Dr Lim":
        doctorcontact = '8562 4562'
        return doctorcontact
    return "none"
