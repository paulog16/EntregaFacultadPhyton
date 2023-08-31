vowels=set()
sentence=input('ingrese frase: ')
for v in sentence:
    if v=='a' or v=='e' or v=='i' or v=='o' or v=='u':
        vowels.add(v)
print(f'las vocales en la oracion son {vowels}')   