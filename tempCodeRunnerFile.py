divisores=[]
number=int(input('ingrese numero: '))
for num in range(1,number+1):
    if number%num==0:
        divisores.append(num)

print(f'los divisores de ese numero son {divisores}')  