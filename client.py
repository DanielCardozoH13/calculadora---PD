from tkinter import  *
import Pyro4

class Calculadora():
    def __init__(self):
        self.ventana()

    def On_Clik_btn(self, bton):
        texto = self.campo_pantalla.get()+str(bton)
        self.input_text.set(texto)

    def borrar_todo(self):
        self.input_text.set("")

    def borrar_ultimo(self):
        texto = self.campo_pantalla.get()
        texto = texto[:len(texto)-1]
        self.input_text.set(texto)

    def conectar_server(self):
        dns = Pyro4.locateNS()
        try:
            uri = dns.lookup(self.campo_pyro.get())
            self.conexion = Pyro4.Proxy(uri)
        except:
            pass

    def resultado(self):
        texto = self.campo_pantalla.get()
        try:
            resultado=self.conexion.calcular(texto)
        except:
            resultado="NO HAY CONEXIÓN"
        self.input_text.set(resultado)

    def ventana(self):
        bg_gral="#EFEFFB"

        principal = Tk()
        principal.title("Calculadora")
        principal.geometry("420x590")
        principal.maxsize(420,590)
        principal.minsize(420,590)
        principal.config(bg=bg_gral,relief="ridge")


        ancho_boton=4
        alto_boton=1
        color_boton="#A9BCF5"
        fuente_btn=('Consolas', '22')
        padx_btn=2
        pady_btn=2
        bd_btn=2
        self.input_text=StringVar()

        #marco para la fila 0, columna 0
        marco00 = Frame(principal)
        marco00.pack(fil=X, side=TOP, pady=10, padx=8)

        #Etiqueta y campo para solicitar URI
        etiqueta_dir_pyro = Label(marco00, text="URI:")
        etiqueta_dir_pyro.pack(side=LEFT, fil=X, expand=True)
        self.campo_pyro = Entry(marco00 )
        self.campo_pyro.pack(side=LEFT, fil=X, expand=True)

        #etiquera y campo para solicitar libreria
        etiqueta_libreria = Label(marco00, text="Librería:")
        etiqueta_libreria.pack(side=LEFT, fil=X, expand=True)
        campo_libreria = Entry(marco00 )
        campo_libreria.pack(side=LEFT, fil=X, expand=True)

        #marco para la fila 1, columna 0
        marco10 = Frame(principal, bg=bg_gral)
        marco10.pack(fil=X, side=TOP)

        boton_conectar = Button(marco10, text="Conectar", command=lambda: self.conectar_server())
        boton_conectar.pack(side=TOP)



        #marco para la fila 2, columna 0
        marco02 = Frame(principal, bg="#BDBDBD")
        marco02.pack(fill=Y, side=TOP, pady=20, padx=8, ipady=30)

        pantalla = Frame(marco02)
        pantalla.pack(fill=X, expand=True, side=TOP)
        self.campo_pantalla = Entry(pantalla, font=('Consolas', 20, 'bold'), width=22,bg="#A9F5A9", bd=20, insertwidth=4, textvariable=self.input_text, justify="right")#, state=DISABLED)
        self.campo_pantalla.pack(fill=X, side=TOP, expand=True)

        botones = Frame(marco02)
        botones.pack(fill=X, expand=True, side=TOP, pady=30)

        #FILA 0 DE BOTONES
        bton_c = Button(botones,text="CE", font=fuente_btn,bd=bd_btn, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:self.borrar_todo()).grid(row=0, column=0, padx=padx_btn, pady=pady_btn)
        bton_del = Button(botones,text="←", font=fuente_btn,bd=bd_btn, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:self.borrar_ultimo()).grid(row=0, column=1, padx=padx_btn, pady=pady_btn)
        bton_Iparent = Button(botones,text="(", font=fuente_btn,bd=bd_btn, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:self.On_Clik_btn("(")).grid(row=0, column=2, padx=padx_btn, pady=pady_btn)
        bton_Fparent = Button(botones,text=")", font=fuente_btn,bd=bd_btn, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:self.On_Clik_btn(")")).grid(row=0, column=3, padx=padx_btn, pady=pady_btn)
        bton_power = Button(botones,text="ON",font=fuente_btn,bd=bd_btn, bg=color_boton,width=ancho_boton,height=alto_boton).grid(row=0, column=4, padx=padx_btn, pady=pady_btn)
        #FILA 1 DE BOTONES
        bton_7 = Button(botones,text="7", font=fuente_btn,bd=bd_btn, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:self.On_Clik_btn("7")).grid(row=1, column=0, padx=padx_btn, pady=pady_btn)
        bton_8 = Button(botones,text="8", font=fuente_btn,bd=bd_btn, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:self.On_Clik_btn("8")).grid(row=1, column=1, padx=padx_btn, pady=pady_btn)
        bton_9 = Button(botones,text="9", font=fuente_btn,bd=bd_btn, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:self.On_Clik_btn("9")).grid(row=1, column=2, padx=padx_btn, pady=pady_btn)
        bton_div = Button(botones,text="/", font=fuente_btn,bd=bd_btn, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:self.On_Clik_btn("/")).grid(row=1, column=3, padx=padx_btn, pady=pady_btn)
        bton_igual = Button(botones,text="=", font=fuente_btn,bd=bd_btn, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:self.resultado()).grid(row=1, column=4, padx=padx_btn, pady=pady_btn, rowspan =4, sticky=N+S)
        #FILA 2 DE BOTONES
        bton_4 = Button(botones,text="4", font=fuente_btn,bd=bd_btn, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:self.On_Clik_btn("4")).grid(row=2, column=0, padx=padx_btn, pady=pady_btn)
        bton_5 = Button(botones,text="5", font=fuente_btn,bd=bd_btn, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:self.On_Clik_btn("5")).grid(row=2, column=1, padx=padx_btn, pady=pady_btn)
        bton_6 = Button(botones,text="6", font=fuente_btn,bd=bd_btn, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:self.On_Clik_btn("6")).grid(row=2, column=2, padx=padx_btn, pady=pady_btn)
        bton_mult = Button(botones,text="*", font=fuente_btn,bd=bd_btn, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:self.On_Clik_btn("*")).grid(row=2, column=3, padx=padx_btn, pady=pady_btn)
        #FILA 3 DE BOTONES
        bton_1 = Button(botones,text="1", font=fuente_btn,bd=bd_btn, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:self.On_Clik_btn("1")).grid(row=3, column=0, padx=padx_btn, pady=pady_btn)
        bton_2 = Button(botones,text="2", font=fuente_btn,bd=bd_btn, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:self.On_Clik_btn("2")).grid(row=3, column=1, padx=padx_btn, pady=pady_btn)
        bton_3 = Button(botones,text="3", font=fuente_btn,bd=bd_btn, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:self.On_Clik_btn("3")).grid(row=3, column=2, padx=padx_btn, pady=pady_btn)
        bton_men = Button(botones,text="-", font=fuente_btn,bd=bd_btn, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:self.On_Clik_btn("-")).grid(row=3, column=3, padx=padx_btn, pady=pady_btn)
        #FILA 4 DE BOTONES
        bton_0 = Button(botones,text="0", font=fuente_btn,bd=bd_btn, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:self.On_Clik_btn("0")).grid(row=4, column=0, padx=padx_btn, pady=pady_btn, columnspan=2, sticky=W+E)
        bton_coma = Button(botones,text=",", font=fuente_btn,bd=bd_btn, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:self.On_Clik_btn(".")).grid(row=4, column=2, padx=padx_btn, pady=pady_btn)
        bton_sum = Button(botones,text="+", font=fuente_btn,bd=bd_btn, bg=color_boton,width=ancho_boton,height=alto_boton,command=lambda:self.On_Clik_btn("+")).grid(row=4, column=3, padx=padx_btn, pady=pady_btn)
        principal.mainloop()


def main():
    app = Calculadora()

if __name__ == "__main__":
    main()