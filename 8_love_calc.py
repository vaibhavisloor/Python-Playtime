name1 = input("Enter name of first person ")
name2 = input("Enter name of your partner ")
name1 = name1.lower()
name2 = name2.lower()

name = name1 + name2

T = name.count("t")
R = name.count("r")
U = name.count("u")
E = name.count("e")
L = name.count("l")
O = name.count("o")
V = name.count("v")
E = name.count("e")

final_score = 10*(T+R+U+E) + (L+O+V+E)

print(final_score)



