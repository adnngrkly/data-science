# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from operator import itemgetter, attrgetter

class Worker():    
    staff_object = []
    def __init__(self,name,surname,age,mail,salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.mail = mail
        self.salary = salary        
        self.__class__.staff_object.append(self)
        
    def __repr__(self):
        return repr((self.name, self.age, self.mail, self.salary))
   
    def increase(rate): # rate degeri sayi olarak girilecek %10 zam icin : 10 
        old_sum_salary = 0
        for each in Worker.staff_object:
            old_sum_salary += each.salary
            each.salary = each.salary * ((100+rate)/100)        
            
        print("""Tum calisanlara %{} oraninda zam yapildi.
yapilan zammin firmamiza maliyeti {} Euro dur.
""".format(rate,old_sum_salary*(rate/100)))
                
    def worker_sort(value): 
        #  value degeri olarak name, surname, age, salary degerleri
        #   string olarak girilecek 'name', 'age' .. gibi
        Worker.staff_object.sort(key=attrgetter(value))
    
             
    
        

worker1 = Worker("ahmet","yildiz",41,'abc',2600)
worker2 = Worker("serap","cicek",35,'dfs',2000)
worker3 = Worker("ali","maytap",28,'ryu',3000)
worker4 = Worker("ayse","elmali",25,'gsd',2500)
worker5 = Worker("selami","puslu",33,'tewq',2800)
worker6 = Worker("fatma","kursun",19,'oyu',1800)
worker7 = Worker("esra","yagur",20,'qweqw',1900)
worker8 = Worker("halil","talha",32,'uytur',2000)
worker9 = Worker("kamil","gulumser",40,'zcxzc',2000)
worker10 = Worker("hakki","kara",41,'hkjghk',2300)
worker11 = Worker("salih","turk",25,'piuu',2800)
worker12 = Worker("hatip","karalar",23,'nbvcv',4000)
worker13 = Worker("mehtap","sevgi",29,'zxsax',3000)
worker14 = Worker("erdogan","uzun",31,'tregfds',1800)
worker15 = Worker("gunay","uzun",35,'yjhj',1900)
worker16 = Worker("mustafa","kisa",38,'qweds',2600)
worker17 = Worker("ismail","hizli",18,'yuujh',2700)
worker18 = Worker("omer","ortlek",24,'ewrfds',3200)
worker19 = Worker("atilla","uysal",25,'iyujh',3200)
worker20 = Worker("mert","kale",25,'xzfs',6000)


Worker.worker_sort('name') # isme gore siraliyor

for i in Worker.staff_object:
    print(i.name ," : ", i.salary)
   
Worker.increase(15)  # yuzde 15 maaslara zam yapiyor

for i in Worker.staff_object:
    print(i.name , " : ", i.salary)

