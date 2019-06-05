from tkinter import  *
from matplotlib import pyplot
import matplotlib, Pyro4
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox

class Calculadora():
    def __init__(self):
        self.principal = Tk()
        self.principal.title("Calculadora")
        self.principal.resizable(False,False)
        self.ancho_boton = 4
        self.alto_boton = 1
        self.color_boton = "#A9BCF5"
        self.fuente_btn = ('Consolas', '22')
        self.padx_btn = 2
        self.pady_btn = 2
        self.pady_btn = 2
        self.bg_gral = "#EFEFFB"
        self.ventana()
        #self.calculadora_sencilla()
        self.principal.mainloop()

    def On_Clik_btn(self, bton):
        texto = self.campo_pantalla.get()+str(bton)
        self.input_text.set(texto)

    def de_sencilla_a_funciones(self):
        self.marco02.destroy()
        self.calculadora_funciones()

    def de_funciones_a_sencilla(self):
        self.marco02.destroy()
        self.calculadora_sencilla()

    def borrar_todo(self):
        self.input_text.set("")

    def borrar_ultimo(self):
        texto = self.campo_pantalla.get()
        texto = texto[:len(texto)-1]
        self.input_text.set(texto)

    def conectar_server(self):
        dns = Pyro4.locateNS()
        #uri = dns.lookup("daniel.com")
        #self.conexion = Pyro4.Proxy(uri)

        try:
            uri = dns.lookup(self.campo_pyro.get())
            self.conexion = Pyro4.Proxy(uri)
            self.calculadora_sencilla()
            self.marco00.destroy()
            self.marco10.destroy()
        except:
            messagebox.showinfo("Error", "No Hay Conexión al servidor")
            self.principal.quit()
            self.principal.destroy()

    def resultado(self):
        texto = self.campo_pantalla.get()
        try:
            resultado=self.conexion.calcular(texto)
        except:
            resultado="NO HAY CONEXIÓN"
        self.input_text.set(resultado)

    def crear_ventana_grafica(self, x, y):
        #self.grafica_vent = Toplevel(bg="#FFFFFF", )
        self.grafica_vent = Tk()
        pos_pantalla_x = self.principal.winfo_x()
        pos_pantalla_y = self.principal.winfo_y()
        ancho_pantalla_ppal = self.principal.winfo_width()
        posicion = '650x490' + '+' + str(pos_pantalla_x + ancho_pantalla_ppal) + '+' + str(pos_pantalla_y)
        self.grafica_vent.geometry(posicion)
        f = pyplot.figure(1)
        pyplot.ion()

        pyplot.title("Gráfica")
        pyplot.xlabel("Eje X")
        pyplot.ylabel("Eje Y")
        grafico = pyplot.plot(x, y)  # se crea la gráfica

        canvas = FigureCanvasTkAgg(f, master=self.grafica_vent)
        self.plot_widget = canvas.get_tk_widget()
        self.plot_widget.grid(row=0, column=0)
        self.grafica_vent.protocol("WM_DELETE_WINDOW", self.cerrando)

        self.grafica_vent.mainloop()

    def cerrando(self):
        self.plot_widget.destroy()
        self.grafica_vent.quit()
        self.grafica_vent.destroy()

    def cerrando_p(self):
        self.principal.quit()
        self.principal.destroy()

    def graficar_lineal(self):
        try:
            m = int(self.entry_m.get().strip())
            a = int(self.entry_b_lineal.get().strip())
            try:
                x,y=self.conexion.valores_graficas(1,0,m,a) #parametro 1 = grado de la funcion, parametro2 = a en cuadratica, parametro 3 = b en cuadratica, parametro 4 = a en cuadratica
                self.crear_ventana_grafica(x,y)
            except:
                messagebox.showinfo("Error", "No Hay Conexión al servidor")
        except:
            messagebox.showinfo("Error", "Ingrese todos los valores")


    def graficar_cuadratica(self):
        try:
            a = int(self.entry_a_cuadratica.get().strip())
            b = int(self.entry_b_cuadratica.get().strip())
            c = int(self.entry_c_cuadratica.get().strip())
            try:
                x,y=self.conexion.valores_graficas(2,a,b,c) #parametro 1 = grado de la funcion, parametro2 = a en cuadratica, parametro 3 = b en cuadratica, parametro 4 = a en cuadratica
                self.crear_ventana_grafica(x,y)
            except:
                messagebox.showinfo("Error", "No Hay Conexión al servidor")
        except:
            messagebox.showinfo("Error", "Ingrese todos los valores")

    def calculadora_funciones(self):
        self.principal.geometry("420x360")
        # self.marco para la fila 2, columna 0
        self.marco02 = Frame(self.principal, bg="#BDBDBD")
        self.marco02.pack(fill=BOTH, side=TOP, pady=20, padx=8, ipady=30)

        #botones y labels para graficar funcion lineal
        lineal00 = Frame(self.marco02)
        lineal00.pack(fill=X, expand=True, side=TOP)
        label_lineal = Label(lineal00, font=('Consolas', 12, 'bold'), width=22, bg="#A9F5A9", bd=3,
                             text="Función Lineal (y = mX + b)", justify="left", relief="groove")
        label_lineal.pack(fill=X, side=TOP)
        lineal10 = Frame(self.marco02)
        lineal10.pack(fill=X, expand=True, side=TOP)

        label_m = Label(lineal10, font=('Consolas', 12, 'bold'), bg=self.color_boton, bd=2,
                        text="m =", justify="right", relief="groove", width=11)
        label_m.grid(column=0, row=0, sticky='E')
        self.entry_m = Entry(lineal10, bd=2, relief="groove", width=15)
        self.entry_m.grid(column=1, row=0, sticky='E')


        label_b_lineal = Label(lineal10, font=('Consolas', 12, 'bold'), bg=self.color_boton, bd=2,
                               text="b =", justify="right", relief="groove", width=11)
        label_b_lineal.grid(column=4, row=0, sticky='E')
        self.entry_b_lineal = Entry(lineal10, bd=2, relief="groove", width=15)
        self.entry_b_lineal.grid(column=5, row=0, sticky='E')

        #boton con comando para graficar la función lineal
        btn_lineal = Button(self.marco02, text="Graficar", font=('Consolas', 12, 'bold'), bd=self.pady_btn, bg="#A9A9A9",command=lambda: self.graficar_lineal()).pack()

        # botones y labels para graficar funcion cuadratica
        cuadratica00 = Frame(self.marco02)
        cuadratica00.pack(fill=X, expand=True, side=TOP)
        label_cuadratica = Label(cuadratica00, font=('Consolas', 12, 'bold'), width=22, bg="#A9F5A9", bd=3,
                                 text="Función cuadrática (y = aX^2 + bX + c)", justify="left", relief="groove")
        label_cuadratica.pack(fill=X, side=TOP)

        cuadratica10 = Frame(self.marco02)
        cuadratica10.pack(fill=X, expand=True, side=TOP)


        label_a = Label(cuadratica10, font=('Consolas', 12, 'bold'), bg=self.color_boton, bd=2,
                        text="a =", justify="right", relief="groove", width=7)
        label_a.grid(column=2, row=0, sticky='E')
        self.entry_a_cuadratica = Entry(cuadratica10, bd=2, relief="groove", width=10)
        self.entry_a_cuadratica.grid(column=3, row=0, sticky='E')

        label_b_cuadratica = Label(cuadratica10, font=('Consolas', 12, 'bold'), bg=self.color_boton, bd=2,
                                   text="b =", justify="right", relief="groove", width=7)
        label_b_cuadratica.grid(column=4, row=0, sticky='E')
        self.entry_b_cuadratica = Entry(cuadratica10, bd=2, relief="groove", width=10)
        self.entry_b_cuadratica.grid(column=5, row=0, sticky='E')

        label_c_cuadratica = Label(cuadratica10, font=('Consolas', 12, 'bold'), bg=self.color_boton, bd=2,
                                   text="c =", justify="right", relief="groove", width=7)
        label_c_cuadratica.grid(column=6, row=0, sticky='E')
        self.entry_c_cuadratica = Entry(cuadratica10, bd=2, relief="groove", width=10)
        self.entry_c_cuadratica.grid(column=7, row=0, sticky='E')

        btn_cuadratica = Button(self.marco02, text="Graficar", font=('Consolas', 12, 'bold'), bd=self.pady_btn,
                                bg="#A9A9A9", command=lambda: self.graficar_cuadratica()).pack()

        btn_cuadratica = Button(self.marco02, text="Atrás", font=('Consolas', 12, 'bold'), bd=self.pady_btn,
                                bg="#B22222", command=lambda: self.de_funciones_a_sencilla()).pack(fill=X, side="right")



    def calculadora_sencilla(self):
        self.principal.geometry("420x590")
        # self.marco para la fila 2, columna 0
        self.marco02 = Frame(self.principal, bg="#BDBDBD")
        self.marco02.pack(fill=Y, side=TOP, pady=20, padx=8, ipady=30)

        pantalla = Frame(self.marco02)
        pantalla.pack(fill=X, expand=True, side=TOP)
        self.campo_pantalla = Entry(pantalla, font=('Consolas', 20, 'bold'), width=22, bg="#A9F5A9", bd=20,
                                    insertwidth=4, textvariable=self.input_text, justify="right")  # , state=DISABLED)
        self.campo_pantalla.pack(fill=X, side=TOP, expand=True)

        botones = Frame(self.marco02)
        botones.pack(fill=X, expand=True, side=TOP, pady=30)

        # FILA 0 DE BOTONES
        bton_c = Button(botones, text="CE", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton, width=self.ancho_boton,
                        height=self.alto_boton, command=lambda: self.borrar_todo()).grid(row=0, column=0, padx=self.padx_btn,
                                                                                         pady=self.pady_btn)
        bton_del = Button(botones, text="←", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton, width=self.ancho_boton,
                          height=self.alto_boton, command=lambda: self.borrar_ultimo()).grid(row=0, column=1, padx=self.padx_btn,
                                                                                             pady=self.pady_btn)
        bton_Iparent = Button(botones, text="(", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton, width=self.ancho_boton,
                              height=self.alto_boton, command=lambda: self.On_Clik_btn("(")).grid(row=0, column=2,
                                                                                                  padx=self.padx_btn,
                                                                                                  pady=self.pady_btn)
        bton_Fparent = Button(botones, text=")", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton, width=self.ancho_boton,
                              height=self.alto_boton, command=lambda: self.On_Clik_btn(")")).grid(row=0, column=3,
                                                                                                  padx=self.padx_btn,
                                                                                                  pady=self.pady_btn)
        bton_power = Button(botones, text="OFF", font=self.fuente_btn, bd=self.pady_btn, bg="#B22222", width=self.ancho_boton,
                            height=self.alto_boton, command=lambda: self.cerrando_p()).grid(row=0, column=4, padx=self.padx_btn,
                                                                                           pady=self.pady_btn)
        # FILA 1 DE BOTONES
        bton_7 = Button(botones, text="7", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton, width=self.ancho_boton,
                        height=self.alto_boton, command=lambda: self.On_Clik_btn("7")).grid(row=1, column=0, padx=self.padx_btn,
                                                                                            pady=self.pady_btn)
        bton_8 = Button(botones, text="8", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton, width=self.ancho_boton,
                        height=self.alto_boton, command=lambda: self.On_Clik_btn("8")).grid(row=1, column=1, padx=self.padx_btn,
                                                                                            pady=self.pady_btn)
        bton_9 = Button(botones, text="9", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton, width=self.ancho_boton,
                        height=self.alto_boton, command=lambda: self.On_Clik_btn("9")).grid(row=1, column=2, padx=self.padx_btn,
                                                                                            pady=self.pady_btn)
        bton_div = Button(botones, text="/", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton, width=self.ancho_boton,
                          height=self.alto_boton, command=lambda: self.On_Clik_btn("/")).grid(row=1, column=3, padx=self.padx_btn,
                                                                                              pady=self.pady_btn)
        bton_fx = Button(botones, text="f(x)", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton,
                            width=self.ancho_boton,
                            height=self.alto_boton, command=lambda: self.de_sencilla_a_funciones()).grid(row=1,
                                                                                                         column=4,
                                                                                                         padx=self.padx_btn,
                                                                                                         pady=self.pady_btn)

        # FILA 2 DE BOTONES
        bton_4 = Button(botones, text="4", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton, width=self.ancho_boton,
                        height=self.alto_boton, command=lambda: self.On_Clik_btn("4")).grid(row=2, column=0, padx=self.padx_btn,
                                                                                            pady=self.pady_btn)
        bton_5 = Button(botones, text="5", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton, width=self.ancho_boton,
                        height=self.alto_boton, command=lambda: self.On_Clik_btn("5")).grid(row=2, column=1, padx=self.padx_btn,
                                                                                            pady=self.pady_btn)
        bton_6 = Button(botones, text="6", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton, width=self.ancho_boton,
                        height=self.alto_boton, command=lambda: self.On_Clik_btn("6")).grid(row=2, column=2, padx=self.padx_btn,
                                                                                            pady=self.pady_btn)
        bton_mult = Button(botones, text="*", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton, width=self.ancho_boton,
                           height=self.alto_boton, command=lambda: self.On_Clik_btn("*")).grid(row=2, column=3,
                                                                                               padx=self.padx_btn, pady=self.pady_btn)
        bton_igual = Button(botones, text="=", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton,
                            width=self.ancho_boton,
                            height=self.alto_boton, command=lambda: self.resultado()).grid(row=2, column=4,
                                                                                           padx=self.padx_btn,
                                                                                           pady=self.pady_btn,
                                                                                           rowspan=3,
                                                                                           sticky=N + S)
        # FILA 3 DE BOTONES
        bton_1 = Button(botones, text="1", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton, width=self.ancho_boton,
                        height=self.alto_boton, command=lambda: self.On_Clik_btn("1")).grid(row=3, column=0, padx=self.padx_btn,
                                                                                            pady=self.pady_btn)
        bton_2 = Button(botones, text="2", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton, width=self.ancho_boton,
                        height=self.alto_boton, command=lambda: self.On_Clik_btn("2")).grid(row=3, column=1, padx=self.padx_btn,
                                                                                            pady=self.pady_btn)
        bton_3 = Button(botones, text="3", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton, width=self.ancho_boton,
                        height=self.alto_boton, command=lambda: self.On_Clik_btn("3")).grid(row=3, column=2, padx=self.padx_btn,
                                                                                            pady=self.pady_btn)
        bton_men = Button(botones, text="-", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton, width=self.ancho_boton,
                          height=self.alto_boton, command=lambda: self.On_Clik_btn("-")).grid(row=3, column=3, padx=self.padx_btn,
                                                                                              pady=self.pady_btn)
        # FILA 4 DE BOTONES
        bton_0 = Button(botones, text="0", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton, width=self.ancho_boton,
                        height=self.alto_boton, command=lambda: self.On_Clik_btn("0")).grid(row=4, column=0, padx=self.padx_btn,
                                                                                            pady=self.pady_btn, columnspan=2,
                                                                                            sticky=W + E)
        bton_coma = Button(botones, text=",", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton, width=self.ancho_boton,
                           height=self.alto_boton, command=lambda: self.On_Clik_btn(".")).grid(row=4, column=2,
                                                                                               padx=self.padx_btn, pady=self.pady_btn)
        bton_sum = Button(botones, text="+", font=self.fuente_btn, bd=self.pady_btn, bg=self.color_boton, width=self.ancho_boton,
                          height=self.alto_boton, command=lambda: self.On_Clik_btn("+")).grid(row=4, column=3, padx=self.padx_btn,
                                                                                              pady=self.pady_btn)

    def ventana(self):
        self.principal.config(bg=self.bg_gral,relief="ridge")
        self.principal.geometry("420x150")
        self.input_text=StringVar()

        #self.marco para la fila 0, columna 0
        self.marco00 = Frame(self.principal)
        self.marco00.pack(fil=X, side=TOP, pady=10, padx=8)

        #Etiqueta y campo para solicitar URI
        etiqueta_dir_pyro = Label(self.marco00, text="URI:")
        etiqueta_dir_pyro.pack(side=LEFT, fil=X, expand=True)
        self.campo_pyro = Entry(self.marco00 )
        self.campo_pyro.pack(side=LEFT, fil=X, expand=True)

        #self.marco para la fila 1, columna 0
        self.marco10 = Frame(self.principal, bg=self.bg_gral)
        self.marco10.pack(fil=X, side=TOP)

        boton_conectar = Button(self.marco10, text="Conectar", command=lambda: self.conectar_server())
        boton_conectar.pack(side=TOP)
        self.principal.protocol("WM_DELETE_WINDOW", self.cerrando_p)


def main():
    app = Calculadora()

if __name__ == "__main__":
    main()