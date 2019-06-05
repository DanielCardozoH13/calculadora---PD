from matplotlib import pyplot

lenguajes = ('python', 'c', 'java')
slices = (100, 130, 90)
colores = ('red', 'blue', 'green')

pyplot.pie(slices, colors=colores)
#pyplot.show()
pyplot.savefig('prueba.png')