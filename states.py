from aiogram.fsm.state import StatesGroup , State
#Получение данных 
class Newlog(StatesGroup):
    Name = State()
    Surname = State()
    Number = State()
#Изменения данных в профиле 
class Change(StatesGroup):
    newname = State()
    newsurname = State()
    newnumber = State()
# Класс чтобы высчитывать объемный вес
class Calc(StatesGroup):
    length = State()
    width = State()
    height = State()
    kilos = State()
#Отправка рассылки всем пользователям которые есть в базе данных.
class sendall(StatesGroup):
    getphoto = State()
    gettext = State()
    getbutton = State() #
    getlink = State() #
    
# photo > 