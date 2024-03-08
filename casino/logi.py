from datetime import datetime

def func():
    ts = datetime.now()
    ts = ts.strftime('%Y%m%d_%H%M%S')
    filename = f'ruletka_{ts}.txt'
    file = open(filename , 'w' , encoding='utf-8')
    return file