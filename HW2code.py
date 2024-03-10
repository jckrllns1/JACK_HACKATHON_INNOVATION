import numpy as np

a, b, c, d = map(float, input("Enter four float values separated by spaces: ").split())

four1 = np.log(1/(1-a))
five1 = np.log(1/(1-b))

four2 = (1/c)
five2 = (1/d)

print(four1, five1, four2, five2)

#print(four1-five1)/(four2-five2)
x = ((four1-five1)/(four2-five2))

print(x*8.31/-1000)

