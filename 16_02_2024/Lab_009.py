# multiple assignment
#a,b = 23,43
#c,d,e = (34,21,56)

hero1 = (["Batman", "Spiderman","superman"])
hero2 = (["Wonder woman","Alice in wonderland"])
super_heroes = hero1 + hero2 # concatenation
super_heroes = hero1 , hero2 # without concatination
print(super_heroes)
#nested tuple is tuple within tuple
print(super_heroes[0])
print(super_heroes[1])
print(super_heroes[0][0])
print(super_heroes[1][0])
print(super_heroes[1][1])
print(super_heroes[0][2])
print(super_heroes[0][1])

#search in tuple
cities = ("London","Paris","Canada","USA","Italy")
print("Italy" in cities)
print("Ney york" in cities)