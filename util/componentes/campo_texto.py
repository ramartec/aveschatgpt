import customtkinter as ctk

from util.tema import *


class CampoTexto(ctk.CTkFrame):

    def __init__(
        self,
        master,
        titulo="",
        placeholder="",
        ancho=None,
        **kwargs
    ):

        super().__init__(
            master,
            fg_color="transparent",
            **kwargs
        )

        self.grid_columnconfigure(0, weight=1)

        # -----------------------------------------

        self.lblTitulo = ctk.CTkLabel(

            self,

            text=titulo,

            font=ETIQUETA,

            text_color=COLOR_TEXTO

        )

        self.lblTitulo.grid(

            row=0,

            column=0,

            sticky="w",

            pady=(0, 5)

        )

        # -----------------------------------------

        self.entry = ctk.CTkEntry(

            self,

            placeholder_text=placeholder,

            height=ALTO_CAMPO,

            corner_radius=RADIO,

            border_width=1,

            border_color=COLOR_BORDE,

            font=TEXTO

        )

        if ancho:

            self.entry.configure(width=ancho)

        self.entry.grid(

            row=1,

            column=0,

            sticky="ew"

        )

    # =====================================================

    def get(self):

        return self.entry.get()

    # =====================================================

    def set(self, valor):

        self.entry.delete(0, "end")

        if valor is not None:

            self.entry.insert(0, str(valor))

    # =====================================================

    def limpiar(self):

        self.entry.delete(0, "end")

    # =====================================================

    def habilitar(self):

        self.entry.configure(state="normal")

    # =====================================================

    def deshabilitar(self):

        self.entry.configure(state="disabled")

    # =====================================================

    def enfocar(self):

        self.entry.focus()

    # =====================================================

    def widget(self):

        return self.entry