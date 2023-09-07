nums=[2,3,4,5,2,1,4,8,9]
numE=int(input('what search a number: '))
for i in nums:
    if nums[i]==numE:
        break
    print(i)
print(f'la lista salio en el numero: {numE} y era la posicion {i}')