                  #1
#Создайте класс одной из геометрических фигур
# (например, прямоугольника),
# где в конструкторе задаются атрибуты:
# начальные координаты x, y, width и height
# (или другие в зависимости от выбранной фигуры).

#Создайте метод, который возвращает
# атрибуты прямоугольника как строку
# ( постарайтесь применить магический метод __str__).
# Для объекта прямоугольника со значениями атрибута
# x = 5, y = 10, width = 50, height = 100
# метод должен вернуть строку Rectangle : 5, 10, 50, 100.

class Rectangle:
    def __init__(self,x,y,widht,height):
        self.x = x
        self.y = y
        self.widht = widht
        self.height = height
    def __str__(self):
        return f'Rectangle: {self.x},{self.y},{self.widht},{self.height}.'
rect_1 = Rectangle(5, 10, 50, 100)
print(rect_1)
# Rectangle: 5,10,50,100.


                     #2
#Напишите код для описания геометрической фигуры.
#Создайте класс «прямоугольник» с помощью метода init().
# На выходе в консоли вам необходимо получить
# площадь данной фигуры.

class Rectangle:
    def __init__(self,x,y,wight,height):
        self.x = x
        self.y = y
        self.wight = wight
        self.height = height
    def __str__(self):
        return f'Rectangle:{self.x},{self.y},{self.wight},{self.height}.'

    def get_area(self):
        return self.wight * self.height
rect_1 = Rectangle(5,10,50,100)
print(rect_1)
print(rect_1.get_area())
#Rectangle:5,10,50,100.
#5000


#                      3
#В проекте «Дом питомца» добавим новую услугу
# — электронный кошелек.
# Необходимо создать класс «Клиент»,
# который будет содержать данные о клиентах
# и их финансовых операциях.
# О клиенте известна следующая информация:
# имя, фамилия, город, баланс.

#Далее сделайте вывод о клиентах в консоль в формате:

#«Иван Петров. Москва. Баланс: 50 руб.»

class Customers:
    def __init__(self,first_name,second_name,city,balance):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city
        self.balance = balance
    def __str__(self):
        return f'''"{self.first_name} {self.second_name}". {self.city}. Баланс: {self.balance} руб.'''
customer_1 = Customers('Иван','Петров','Москва',25)
print(customer_1)
# "Иван Петров". Москва. Баланс: 25 руб.


                   #4
#Команда проекта «Дом питомца» планирует
# большой корпоратив для своих клиентов.
# Вам необходимо написать программу,
# которая позволит составить список гостей.
# В класс «Клиент» добавьте метод,
# который будет возвращать информацию только об
# имени, фамилии и городе клиента.

#Затем создайте список,
# в который будут добавлены все клиенты,
# и выведете его в консоль.

class Customers:
    def __init__(self, first_name,second_name,city):
        self.first_name = first_name
        self.second_name = second_name
        self.city= city
    def get_guest(self):
        return f'{self.first_name} {self.second_name}, г.{self.city}'
costomer_1 = Customers('Иван','Иванов','Москва')
costomer_2 = Customers('Елена','Тихонова','Москва')
costomer_3 = Customers('Анна','Ивановна','Москва')

guest_list = [costomer_1,costomer_2,costomer_3]
for guest in guest_list:
    print(guest.get_guest())
#Иван Иванов, г.Москва
#Елена Тихонова, г.Москва
#Анна Ивановна, г.Москва