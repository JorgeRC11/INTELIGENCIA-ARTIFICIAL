print('Cual es tu edad?\n')
edad = int(input())
if edad <= 0:
    print('Nadie puede tener esa edad.')

elif edad >0 and edad<18:
    print('Eres menor de edad')

elif edad >= 18 and edad <= 45:
    print('El descuento solo aplica a mayores de 45, lo sentimos')

elif edad ==100:
    print('Feliz centenario, pase usted')

elif edad >100 and edad<=120:
    print('No le recomendamos que entre a la sala 7')

else:
    print('Edad no valida')
