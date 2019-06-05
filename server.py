import Pyro4



@Pyro4.expose
class Calculadora():
    def calcular(self, texto):
        try:
            resultado = str(eval(texto))
        except:
            resultado = "ERROR"
        return resultado

    def valores_graficas(self, grado, a, b, c):
        x=[]
        y=[]
        i=-10
        if grado ==1:
            while i <= 10:
                x.append(i)
                y.append((b*i)+c)
                i=i+1
        elif grado == 2:
            while i <= 10:
                x.append(i)
                y.append((a*(i**2))+(b*i)+c)
                i=i+1
        return x, y

demonio=Pyro4.Daemon()
uri = demonio.register(Calculadora)
dns = Pyro4.locateNS()
dns.register("daniel.com", uri)
demonio.requestLoop()

