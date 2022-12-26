from PIL import Image
import os
import shutil

photo_number = 1

folder = 'C:/Users/valfr.VAL/Pictures/Fotos'

if not os.path.isdir(folder+'/duplicates')
    os.makedirs(folder+'/duplicates')

if not os.path.isdir(folder+'/no_analyzable/'):
    os.makedirs(folder+'/no_analyzable/')


extensions = ['png', 'PNG', 'jpg', 'JPG', 'jpeg',
              'JPEG', 'webp', 'WEBP', 'tiff', 'TIFF']

entries = os.listdir(folder)
entries = [str(item) for item in entries]
no_analizables = entries.copy()

total = len(entries)
total_counter = 1

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


for entry in entries:
    im1 = Image.open(folder+'/'+entry)
    width1, height1 = im1.size

    for entry2 in entries:
        im2 = Image.open(folder+'/'+entry2)
        width2, height2 = im2.size

        print(f"archivos: {entry} y {entry2} ============ {total_counter}/{total*total} \n")
        total_counter +=1

        if entry == entry2:
            print("son la misma imagen \n")
        else:
            print("NO son la misma imagen \n")

            if width1 == width2 and height1 == height2 and any((ext in entry and ext in entry2) for ext in extensions):
                # si son de distinto tamaño no son iguales
                # anadir que dif extension son dif imagenes

                image1 = im1.load()
                image2 = im2.load()

                counter = 0
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
                            if (r1 == r2 and g1 == g2 and b1 == b2 and a1==a2):
                                counter += 1
                            else:
                                print("se descubre un pixel distinto, saliendo del loop x")
                                break
                        else:
                            if (r1 == r2 and g1 == g2 and b1 == b2):
                                counter += 1
                            else:
                                print("se descubre un pixel distinto, saliendo del loop x")
                                break
                        

                    if not (r1 == r2 and g1 == g2 and b1 == b2):
                        print("se descrubre un pixel distinto, saliendo del loop y")
                        break

                if counter == height1*width1:
                    print(f"{entry} y {entry2} son IGUALES")
                    if entry in entries:
                        entries.remove(entry)

                    # Renaming the file
                    name=f'/{entry2}_copy_orig_'

                    old_name = folder+'/' + entry
                    new_name = folder+name+ entry
                    os.rename(old_name, new_name)

                    original = new_name
                    target = folder+'/duplicates' + name+ entry
                    shutil.move(original, target)

                else:
                    print(f"{entry} y {entry2} NO son IGUALES")
