def colores(*args):
    print('El color', args[1],'es mi favorito.','El color',args[0],'tampoco esta mal.')

colores('verde','gris')

def suma(*args):
    sum =0
    for x in args:
        sum = sum + x
    print(sum)

suma(5,10,13,45,2,6)