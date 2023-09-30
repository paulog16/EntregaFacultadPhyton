import funciones5
cantdias=int(input('ingrese cantidad de dias: '))
for i in range(1,cantdias+1):
    print(f'indique temp max y temp min del dia {i}')
    t_max=float(input(''))
    t_min=float(input(''))
    media=funciones5.prom(t_max,t_min)
    print(f'la media del dia {i} es {media}')