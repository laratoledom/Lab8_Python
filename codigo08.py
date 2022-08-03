#Entrada
num_frases = int(input())
frases = []
for i in range(num_frases):
    a = (input()).lower()
    a = a.replace(".", "")
    a = a.replace(",", "")
    a = a.replace(":", "")
    a = a.replace(";", "")
    a = a.replace("!", "")
    a = a.replace("?", "")
    nova_lista = a.split()
    frases = frases + nova_lista

#Leitura e Saída
ja_usados = []
for i in frases:
    if i not in ja_usados:
        if i == i[::-1]:
            print(i, frases.count(i))
            ja_usados.append(i)
