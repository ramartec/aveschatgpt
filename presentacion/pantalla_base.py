#pantalla_base.py# pantalla_base.py

import customtkinter as ctk

from util.tema import *
from util.componentes.boton import BotonSecundario


class PantallaBase(ctk.CTkFrame):

    def __init__(
        self,
        master,
        titulo="",
        mostrar_boton_volver=False,
        **kwargs
    ):

        super().__init__(
            master,
            fg_color=COLOR_FONDO,
            **kwargs
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # =====================================================
        # CABECERA
        # =====================================================

        self.cabecera = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.cabecera.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=ESPACIADO_GRANDE,
            pady=(ESPACIADO_GRANDE, ESPACIADO)
        )

        self.cabecera.grid_columnconfigure(1, weight=1)

        # =====================================================
        # BOTÓN VOLVER
        # =====================================================

        self.btnVolver = None

        if mostrar_boton_volver:

            self.btnVolver = BotonSecundario(
                self.cabecera,
                text="← Volver",
                width=110,
                command=self.volver
            )

            self.btnVolver.grid(
                row=0,
                column=0,
                padx=(0, 15)
            )

        # =====================================================
        # TÍTULO
        # =====================================================

        self.lblTitulo = ctk.CTkLabel(
            self.cabecera,
            text=titulo,
            font=TITULO,
            text_color=COLOR_TEXTO
        )

        self.lblTitulo.grid(
            row=0,
            column=1,
            sticky="w"
        )

        # =====================================================
        # ÁREA DE BOTONES SUPERIORES
        # =====================================================

        self.frameAcciones = ctk.CTkFrame(
            self.cabecera,
            fg_color="transparent"
        )

        self.frameAcciones.grid(
            row=0,
            column=2,
            sticky="e"
        )

    # =====================================================
    # UTILIDADES
    # =====================================================

    def set_titulo(self, titulo):

        self.lblTitulo.configure(
            text=titulo
        )

    # =====================================================

    def volver(self):
        """
        Las pantallas hijas pueden sobrescribir este método.
        """
        pass

    # =====================================================

    def actualizar(self):
        """
        Las pantallas hijas pueden sobrescribir este método.
        """
        pass

    # =====================================================

    def mostrar(self):
        """
        Se ejecuta cuando la pantalla se hace visible.
        """
        pass

    # =====================================================

    def ocultar(self):
        """
        Se ejecuta cuando la pantalla deja de mostrarse.
        """
        pass