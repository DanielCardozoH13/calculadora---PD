import Pyro4

@Pyro4.expose
class Calculadora():
    def calcular(self, texto):
        try:
            resultado = str(eval(texto))
        except:
            resultado = "ERROR"
        return resultado


demonio=Pyro4.Daemon()
uri = demonio.register(Calculadora)
dns = Pyro4.locateNS()
dns.register("daniel.com", uri)
demonio.requestLoop()

