class Family:
    def __init__(self  ,who , name , year , work = None ,study = None):
        self.who = who
        self.name = name
        self.year = int(year)
        self.work = work
        self.study = study


    def __str__(self):
        return f'name - {self.name} , year - {self.year} , work - {self.work} , study - {self.study}'



class Mama(Family):
    def __init__(self ,who , name , year , work ,money):
        super().__init__( who , name , year ,work)
        self.money = int(money)

    def work_(self , who_):
        self.who_ = who_
        self.money = 30000
        return f'{self.who} на должности {self.who_} получает {self.money} гривен '




class Sun(Family):
    def __init__(self ,who , name , year ,work, study , money):
        super().__init__( who , name , year ,work,study)
        self.money  = money

    def study_(self , where):
        self.where = where
        return f'{self.who} обучаеться на {self.where}'

    def work_(self , who_):
        self.who_=who_
        self.money = 500
        return f'{self.who} на подроботки в {self.who_} получает {self.money} гривен в день'



class Sister_1(Family):
    def __init__(self ,who , name , year ,study):
        super().__init__( who , name , year ,study   )

    def study_(self , where , class_):
        self.where = where
        self.class_ = class_
        return f'{self.who} обучаеться в {self.where} в {self.class_}'


class Sister_2(Family):
    def __init__(self ,who , name , year , study):
        super().__init__( who , name , year ,study)

    def study_(self, where , class_):
        self.where = where
        self.class_ = class_
        return f'{self.who} обучаеться в {self.where} в {self.class_}'


class Father(Family):
    def __init__(self ,who , name , year , work):
        super().__init__( who , name , year ,work   )

    def work_(self , who_):
        self.who_ = who_
        self.money = 60000
        return f'{self.who} на должности {self.who_} получает {self.money} гривен '


class Grandmother(Family):
    def __init__(self ,who , name , year , work):
        super().__init__( who , name , year ,work   )

    def work_(self , who_):
        self.who_ = who_
        self.money = 15000
        return f'{self.who} на должности {self.who_} получает {self.money} гривен '


s = Family('Brather' , 'Vlad' , 2000 , None , 'School')












