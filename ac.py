a= float(input('Entre com o valor de a:'))
b = float(input('Entre com o valor de b::'))
c = float(input('entre com o valor de c:'))

d = (b**2 - 4*a*c)
x1 = (-b-d**(1/2)) / (2*a)
x2 = (-b+d**(1/2)) / (2*a)

print("O valor de x1 e:", x1, "O valor de x2 e:",x2)

anobissexto= int(input("Digite qualquer ano:"))
bissexto= (anobissexto % 4 == 0 and anobissexto % 100 != 0) or (anobissexto % 400 == 0)
print(anobissexto and f'{anobissexto} e um ano bissexto' or f'{anobissexto}nao e um bissexto')