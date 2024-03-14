texto = ('Nossa aula manipulando String.')

print(texto[0:20:2])
print(len(texto))
print(texto.count('a'))
print(texto.count('a',5,30))
print(texto.find('aula'))
print('String' in texto)

novotxt = texto.replace('Nossa', "A")

print(texto)
print(novotxt)
print(texto.upper())
print(texto.lower())
print(texto.capitalize())
print(texto.title())

nome = str(input('Digite seu nome: '))
print(nome)
print(nome.strip())

print(nome.rstrip())
print(nome.lstrip())
