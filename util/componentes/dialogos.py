#dialogos.py

import customtkinter as ctk

from util.tema import *


class Dialogo(ctk.CTkToplevel):

    def __init__(
        self,
        master,
        titulo,
        mensaje,
        icono="ℹ"
    ):

        super().__init__(master)

        self.resultado = None

        self.title(titulo)

        self.geometry("420x220")

        self.resizable(False, False)

        self.transient(master)

        self.grab_set()

        self.configure(
            fg_color=COLOR_FONDO
        )

        # -----------------------------------------

        frame = ctk.CTkFrame(

            self,

            fg_color=COLOR_TARJETA,

            corner_radius=RADIO

        )

        frame.pack(

            fill="both",

            expand=True,

            padx=20,

            pady=20

        )

        # -----------------------------------------

        ctk.CTkLabel(

            frame,

            text=icono,

            font=(FUENTE,40)

        ).pack(

            pady=(20,10)

        )

        ctk.CTkLabel(

            frame,

            text=titulo,

            font=SUBTITULO

        ).pack()

        ctk.CTkLabel(

            frame,

            text=mensaje,

            font=TEXTO,

            wraplength=340,

            justify="center"

        ).pack(

            pady=15

        )

        self.frameBotones = ctk.CTkFrame(

            frame,

            fg_color="transparent"

        )

        self.frameBotones.pack(

            pady=(0,20)

        )

    # =====================================================

    def esperar(self):

        self.wait_window()

        return self.resultado

class DialogoInformacion(Dialogo):

    def __init__(self,master,mensaje):

        super().__init__(

            master,

            "Información",

            mensaje,

            "ℹ"

        )

        from componentes.boton import BotonPrimario

        BotonPrimario(

            self.frameBotones,

            text="Aceptar",

            command=self.cerrar

        ).pack()

    def cerrar(self):

        self.resultado=True

        self.destroy()

class DialogoError(Dialogo):

    def __init__(self,master,mensaje):

        super().__init__(

            master,

            "Error",

            mensaje,

            "⛔"

        )

        from componentes.boton import BotonPeligro

        BotonPeligro(

            self.frameBotones,

            text="Aceptar",

            command=self.cerrar

        ).pack()

    def cerrar(self):

        self.resultado=True

        self.destroy()

class DialogoConfirmacion(Dialogo):

    def __init__(self,master,mensaje):

        super().__init__(

            master,

            "Confirmación",

            mensaje,

            "⚠"

        )

        from componentes.boton import (

            BotonPrimario,

            BotonSecundario

        )

        BotonSecundario(

            self.frameBotones,

            text="Cancelar",

            command=self.cancelar

        ).pack(

            side="left",

            padx=5

        )

        BotonPrimario(

            self.frameBotones,

            text="Aceptar",

            command=self.aceptar

        ).pack(

            side="left",

            padx=5

        )

    def aceptar(self):

        self.resultado=True

        self.destroy()

    def cancelar(self):

        self.resultado=False

        self.destroy()

