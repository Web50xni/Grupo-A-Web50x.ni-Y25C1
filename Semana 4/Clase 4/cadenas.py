word = input("Escribe una palabra: ")
letters = {}

for char in word:
    if char in letters:
        letters[char] += 1
    else:
        letters[char] = 1

print("Frecuencia de letras:")
for char, count in letters.items():
    print(f"{char}: {count}")