import os
import datetime
import shutil
from PIL import Image

folder = 'C:/Users/valfr.VAL/Pictures/Fotos'

photo_id = 0

if not os.path.isdir(folder+'/no_analyzable/'):
    os.makedirs(folder+'/no_analyzable/')


extensions = ['png', 'PNG', 'jpg', 'JPG', 'jpeg',
              'JPEG', 'webp', 'WEBP', 'tiff', 'TIFF']

entries = os.listdir(folder)
entries = [str(item) for item in entries]
no_analizables = entries.copy()


def funcion(x):
    return any(ext in x for ext in extensions)


def no_funcion(x):
    return not (funcion(x)) and not (os.path.isdir(folder+'/'+x))


entries = list(filter(funcion, entries))
entries.sort()

no_analizables = list(filter(no_funcion, no_analizables))
no_analizables.sort()
print(no_analizables)

for element in no_analizables:
    original = folder + '/' + element
    target = folder + '/no_analyzable/' + element
    shutil.move(original, target)


print("imagenes encontradas", entries)


def funcion2(x):
    ext = ''
    for c in reversed(x):
        if c != '.':
            ext += c
        else:
            ext += '.'
            break
    return ext[::-1]


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
        name = f'{anho2}{month2}{day2}_{hour2}{minute2}{second2}_{photo_id}'

    except:

        c_time = os.path.getctime(path)
        dt_c = datetime.datetime.fromtimestamp(c_time)

        anho = f(dt_c.year)
        month = f(dt_c.month)
        day = f(dt_c.day)
        hour = f(dt_c.hour)
        minute = f(dt_c.minute)
        second = f(dt_c.second)
        name = f'{anho}{month}{day}_{hour}{minute}{second}_{photo_id}'

    old_name = path
    new_name = folder+'/' + name+funcion2(entry)
    os.rename(old_name, new_name)

    photo_id += 1
