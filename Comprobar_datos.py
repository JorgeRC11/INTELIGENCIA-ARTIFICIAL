colores = ('rojo','verde','azul','morado')
entrada = input("Ingrese un color: \n")
if entrada in colores[0]:
    print('El color rojo esta admitido')
elif entrada in colores[1]:
    print('El color verde esta admitido')
elif entrada in colores[2]:
    print('El color azul esta admitido')
elif entrada in colores[3]:
    print('El color morado esta admitido')
else:
    print('El color no esta admitido')

