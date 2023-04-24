#q1
'''
linguagens = open("linguagens.txt","w")
inversao = open("inversão.txt", "w")
lista_language = ["Python","Java","C/C++","PHP","SQL","R","JavaScript","Ruby","CSS"]
for linha in lista_language:
    linguagens.write("%s"%linha)
linguagens.close()
'''
#q2
'''
linguagens = open("linguagens.txt","w")
inversao = open("inversão.txt", "w")
lista_language = ["Python","Java","C/C++","PHP","SQL","R","JavaScript","Ruby","CSS"]
for linha in lista_language:
    linguagens.write("%s"%linha)
lista_language.reverse()
for linhaTwo in lista_language:
    inversao.write("%s"%linhaTwo)
linguagens.close()
inversao.close()
'''
#q3
'''
linguagens = open("linguagens.txt","w")
inversao = open("inversão.txt", "w")
ordenado = open("ordenado.txt","w")
lista_language = ["Python","Java","C/C++","PHP","SQL","R","JavaScript","Ruby","CSS"]
for linha in lista_language:
    linguagens.write("%s"%linha)
lista_language.reverse()
for linhaTwo in lista_language:
    inversao.write("%s"%linhaTwo)
lista_language.sort()
for linhaTree in lista_language:
    ordenado.write("%s"%linhaTree)
linguagens.close()
inversao.close()
ordenado.close()
'''

#4
'''
linguagens = open("linguagens.txt","w")
inversao = open("inversão.txt", "w")
ordenado = open("ordenado.txt","w")
enumerado = open("enumerado.txt","w")
lista_language = ["Python","Java","C/C++","PHP","SQL","R","JavaScript","Ruby","CSS"]
for linha in lista_language:
    linguagens.write("%s"%linha)
lista_language.reverse()
for linhaTwo in lista_language:
    inversao.write("%s"%linhaTwo)
lista_language.sort()
for linhaTree in lista_language:
    ordenado.write("%s"%linhaTree)
for ind, language in enumerate(lista_language):
    enumerado.write(f"{ind}:{language}")
linguagens.close()
inversao.close()
ordenado.close()
enumerado.close()
'''