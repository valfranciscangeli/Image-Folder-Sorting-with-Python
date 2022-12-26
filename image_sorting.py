from PIL import Image
import os
import shutil
import datetime

folder = 'C:/Users/valfr.VAL/Pictures/Fotos'


if not os.path.isdir(folder+'/no_sortable/'):
    os.makedirs(folder+'/no_sortable/')


extensions = ['png', 'PNG', 'jpg', 'JPG', 'jpeg',
              'JPEG', 'webp', 'WEBP', 'tiff', 'TIFF']

entries = os.listdir(folder)
entries = [str(item) for item in entries]
no_sortable = entries.copy()



def funcion(x):
    return any(ext in x for ext in extensions)


def no_funcion(x):
    return not (funcion(x)) and not (os.path.isdir(folder+'/'+x))


entries = list(filter(funcion, entries))
entries.sort()

no_sortable = list(filter(no_funcion, no_sortable))
no_sortable.sort()
print(no_sortable)

for element in no_sortable:
    original = folder + '/' + element
    target = folder + '/no_sortable/' + element
    shutil.move(original, target)


for entry in entries:
    path = folder+'/' + entry
    print('path:', path)

    def f(x):
        return str(x) if x > 9 else "0"+str(x)

    def f2(x):
        year = ''
        month = ''
        day = ''
        hr = ''
        minute = ''
        second = ''

        count = 0
        for c in x:
            if count == 0:
                if c != ':':
                    year += c
                else:
                    count += 1
            elif count == 1:
                if c != ':':
                    month += c
                else:
                    count += 1
            elif count == 2:
                if c != ' ':
                    day += c
                else:
                    count += 1
            elif count == 3:
                if c != ':':
                    hr += c
                else:
                    count += 1
            elif count == 4:
                if c != ':':
                    minute += c
                else:
                    count += 1
            elif count == 5:
                if c != ' ':
                    second += c
                else:
                    count += 1
    
        return f(int(year)), f(int(month)), f(int(day)), f(int(hr)), f(int(minute)), f(int(second))
            

    try:
        t_time = Image.open(path)._getexif()[36867]

        anho2, month2, day2, hour2, minute2, second2 = f2(t_time)
        name = anho2

    except:

        c_time = os.path.getctime(path)
        dt_c = datetime.datetime.fromtimestamp(c_time)

        anho = f(dt_c.year)
        name = anho


    if not os.path.isdir(folder+f'/{name}'):
        os.makedirs(folder+f'/{name}')

    original = path
    target = f"{folder}/{name}/{entry}"
    shutil.move(original, target)