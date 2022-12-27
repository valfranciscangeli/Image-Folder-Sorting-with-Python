from PIL import Image
import os
import shutil
import math
import itertools

photo_number = 1

folder = 'C:/Users/valfr.VAL/Pictures/Fotos/2015'

if not os.path.isdir(folder+'/duplicates'):
    os.makedirs(folder+'/duplicates')

if not os.path.isdir(folder+'/no_analyzable/'):
    os.makedirs(folder+'/no_analyzable/')


def funcion(x):
    return any(ext in x for ext in extensions)


def no_funcion(x):
    return not (funcion(x)) and not (os.path.isdir(folder+'/'+x))


extensions = ['png', 'PNG', 'jpg', 'JPG', 'jpeg',
              'JPEG', 'webp', 'WEBP', 'tiff', 'TIFF']

entries = os.listdir(folder)
entries = [str(item) for item in entries]
no_analizables = entries.copy()

entries = list(filter(funcion, entries))
entries.sort()

no_analizables = list(filter(no_funcion, no_analizables))
no_analizables.sort()


for element in no_analizables:
    original = folder + '/' + element
    target = folder + '/no_analyzable/' + element
    shutil.move(original, target)


print("imagenes encontradas", entries)
print('largo:', len(entries))
print()

""" combinations = list(itertools.combinations(entries, 2))
print(combinations)
print("largo:", len(c))

total = len(c) """
total = len(entries)
total_counter = 1


for i in range(total):
    entry = entries[i]
    im1 = Image.open(folder+'/'+entry)
    width1, height1 = im1.size

    for j in range(total):
        entry2 = entries[j]

        print(
            f"archivos: {entry} y {entry2} ============ {total_counter}/{total*total} \n")
        total_counter += 1

        if i == j:
            print("son la misma imagen \n")
        else:
            print("NO son la misma imagen \n")

        if i > j:
            print(f"imagen {entry2} ya revisada\n")

        if i < j:

            im2 = Image.open(folder+'/'+entry2)
            width2, height2 = im2.size

            if width1 == width2 and height1 == height2 and any((ext in entry and ext in entry2) for ext in extensions):
                # si son de distinto tamaño no son iguales
                # anadir que dif extension son dif imagenes

                image1 = im1.load()
                image2 = im2.load()

                counter = 0
                print("comenzamos a analizar pixeles")
                for y in range(height1):
                    for x in range(width1):

                        color1 = image1[x, y]
                        color2 = image2[x, y]

                        if len(color1) == 3:
                            r1, g1, b1 = image1[x, y]
                        else:
                            r1, g1, b1, a1 = image1[x, y]

                        if len(color2) == 3:
                            r2, g2, b2 = image2[x, y]
                        else:
                            r2, g2, b2, a2 = image2[x, y]

                        if len(color1) == 4 and len(color2) == 4:
                            if (r1 == r2 and g1 == g2 and b1 == b2 and a1 == a2):
                                counter += 1
                            else:
                                print(
                                    "se descubre un pixel distinto, saliendo del loop x")
                                break
                        else:
                            if (r1 == r2 and g1 == g2 and b1 == b2):
                                counter += 1
                            else:
                                print(
                                    "se descubre un pixel distinto, saliendo del loop x")
                                break

                    if not (r1 == r2 and g1 == g2 and b1 == b2):
                        print("se descrubre un pixel distinto, saliendo del loop y")
                        break

                if counter == height1*width1:
                    print(f"{entry} y {entry2} son IGUALES\n")
                    # if entry in entries:
                    #     entries.remove(entry)
                    #     total-=1

                    if os.path.exists(folder+'/' + entry):

                        name = f'{entry2}_copy_orig_{entry}'

                        old_name = folder+'/' + entry
                        print('old name:', old_name)
                        new_name = folder+'/'+name
                        print('new name:', new_name)
                        os.rename(old_name, new_name)

                        entries[i]=name

                        original = new_name
                        target = folder+'/duplicates/' + name
                        shutil.move(original, target)

                else:
                    print(f"{entry} y {entry2} NO son IGUALES\n")
