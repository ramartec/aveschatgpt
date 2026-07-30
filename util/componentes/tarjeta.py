import customtkinter as ctk

from util.tema import *


class Tarjeta(ctk.CTkFrame):

    def __init__(
        self,
        master,
        **kwargs
    ):

        super().__init__(

            master,

            fg_color=COLOR_TARJETA,

            corner_radius=RADIO,

            border_width=1,

            border_color=COLOR_BORDE,

            **kwargs

        )

        self.grid_columnconfigure(
            0,
            weight=1
        )

    # =====================================================

    def titulo(
        self,
        texto
    ):

        lbl = ctk.CTkLabel(

            self,

            text=texto,

            font=SECCION,

            text_color=COLOR_TEXTO

        )

        lbl.grid(

            row=0,

            column=0,

            sticky="w",

            padx=ESPACIADO_GRANDE,

            pady=(ESPACIADO_GRANDE, ESPACIADO)

        )

        return lbl

    # =====================================================

    def contenido(self):

        frame = ctk.CTkFrame(

            self,

            fg_color="transparent"

        )

        frame.grid(

            row=1,

            column=0,

            sticky="nsew",

            padx=ESPACIADO_GRANDE,

            pady=(0, ESPACIADO_GRANDE)

        )

        frame.grid_columnconfigure(
            0,
            weight=1
        )

        return frame