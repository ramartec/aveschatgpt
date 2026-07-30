import customtkinter as ctk

from util.tema import *


class BotonPrimario(ctk.CTkButton):

    def __init__(self, master, **kwargs):

        super().__init__(

            master,

            fg_color=COLOR_PRIMARIO,

            hover_color=COLOR_PRIMARIO_HOVER,

            text_color="white",

            font=BOTON,

            corner_radius=RADIO,

            height=ALTO_BOTON,

            width=ANCHO_BOTON,

            cursor="hand2",

            **kwargs

        )


# ==========================================================


class BotonSecundario(ctk.CTkButton):

    def __init__(self, master, **kwargs):

        super().__init__(

            master,

            fg_color=COLOR_SECUNDARIO,

            hover_color="#EAECEF",

            border_width=1,

            border_color=COLOR_BORDE,

            text_color=COLOR_TEXTO,

            font=BOTON,

            corner_radius=RADIO,

            height=ALTO_BOTON,

            width=ANCHO_BOTON,

            cursor="hand2",

            **kwargs

        )


# ==========================================================


class BotonPeligro(ctk.CTkButton):

    def __init__(self, master, **kwargs):

        super().__init__(

            master,

            fg_color=COLOR_ERROR,

            hover_color="#B91C1C",

            text_color="white",

            font=BOTON,

            corner_radius=RADIO,

            height=ALTO_BOTON,

            width=ANCHO_BOTON,

            cursor="hand2",

            **kwargs

        )