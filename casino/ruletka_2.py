from random import choice
from logi import func
f = func()
class Ruletca:
    def __init__(self):
        self.pockets = [ 0 , 1 , 2 , 3 ,4 ,5 ,6 ,7, 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24 , 25 , 26 , 27 ,28 , 29 ,30 , 31 , 32 , 33 , 34 , 35 , 36]
        self.color = {0: 'green' , 1: 'red', 2:'black' , 3: 'red', 4: 'black', 5: 'red', 6: 'black', 7: 'red', 8: 'black', 9: 'red', 10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red', 15: 'black', 16: 'red', 17: 'black', 18: 'red', 19: 'red', 20: 'black', 21: 'red', 22: 'black', 23: 'red', 24: 'black', 25: 'red', 26: 'black', 27: 'red', 28: 'black', 29: 'black', 30: 'red', 31: 'black', 32: 'red', 33: 'black', 34: 'red', 35: 'black', 36: 'red'}

    def spin(self):
        pocket = choice(self.pockets)
        color =self.color[pocket]
        return pocket , color

    def game(self):
        balance = int(input('Сумма пополнения баланса : \n'))
        print('Сумма пополнения баланса : \n' , file=f)
        print(f'Баланс : {balance}')
        print(f'Баланс : {balance}' , file=f)
        try:
            while True:
                game = input('На что будете ставить:\n1- цифры \n2- на цвет \n3- выход \n')
                print(f'На что будете ставить:\n1- цифры \n2- на цвет \n3- выход \n Вариант:{game} ', file=f)
                if game == '1':
                    stavka = []
                    for i in range(10):
                        number = int(input(f'Введите число - {i + 1}:'))
                        print(f'Введите число - {i + 1}:{number}' , file=f)
                        if balance < 0:
                            print('Не достаточно средств ')
                            print('Не достаточно средств ' , file=f)
                            break
                        amount = int(input(f'Введите сумму ставки на число {number}:'))
                        print(f'Введите сумму ставки на число {number}:{amount}' , file=f)
                        stavka.append((number , amount))
                        balance-=amount


                    pocket , _ = self.spin()
                    color = self.color[pocket]
                    winning = 0
                    if balance < 0:
                        print('Не достаточно средств ')
                        print('Не достаточно средств ' , file=f)
                        break
                    for number , amount in stavka:
                        if pocket == number:
                            winning+= amount*35
                        if winning>0:
                            balance+=winning
                            print(f'Выигрыш, выпало число {pocket, color}\nВаш баланс: {balance}')
                            break
                            continue
                            print(f'Выигрыш, выпало число {pocket, color}\nВаш баланс: {balance}' , file=f)


                        else:
                            balance= balance
                            print( f'Проигрыш, выпало число {pocket, color}\nВаш баланс: {balance}')
                            break
                            continue
                            print( f'Проигрыш, выпало число {pocket, color}\nВаш баланс: {balance}' , file=f)


                elif game =='2':
                    money = int(input(f'Баланс : {balance}\nВведите сумму ставки:\n'))
                    print(f'Баланс : {balance}\nВведите сумму ставки:\n Вариант:{money}' , file=f)
                    stavka = input('red or black \n')
                    print(f'red or black \n{stavka}' , file=f)
                    pocket , _ = self.spin()
                    color = self.color[pocket]
                    if stavka == color and money<=balance:
                        balance = money*2 + (balance - money)
                        print( f'Выигрыш, выпало число {pocket, color}\nВаш баланс: {balance}')
                        print(f'Выигрыш, выпало число {pocket, color}\nВаш баланс: {balance}' , file=f)
                    elif stavka!=color and money<=balance:
                        balance = balance - money
                        print( f'Проигрыш , выпало число {pocket, color}\nВаш баланс: {balance}')
                        print( f'Проигрыш , выпало число {pocket, color}\nВаш баланс: {balance}' , file=f)
                    else:
                        print( 'Не достаточно средств ')
                        print( 'Не достаточно средств ' , file=f)
                elif game == '3':
                    return 'Выход...'
                else:
                    print('Вы ввели неправильный выбор. Попробуйте снова.')
                    print('Вы ввели неправильный выбор. Попробуйте снова.' , file=f)
        except ValueError:
            print('Вы ввели значение не по форме\nВыход........')
            print('Вы ввели значение не по форме\nВыход........' , file=f)




r = Ruletca()
res = r.game()
print(res)

