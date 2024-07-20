a = 5
b = "oii"
c = [1, 2, 3, 4, 5, 6]
d = ('oi', 4)

d_list = d + ('adicionei um novo valor a tupla', 'mais um',)
d_list = list(d)#converti o valor de uma tupla para list
d_list[1] = ('modifiquei o valor')#modifiquei o segundo item da lista 
d = tuple(d_list)#modifiquei de volta pra uma tuple

print(d)# ('oi', 'modifiquei o valor')
