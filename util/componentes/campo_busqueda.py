# campo_busqueda.py

import customtkinter as ctk

from util.tema import *


class CampoBusqueda(ctk.CTkFrame):

    def __init__(
        self,
        master,
        titulo="",
        placeholder="Buscar...",
        **kwargs
    ):

        super().__init__(
            master,
            fg_color="transparent",
            **kwargs
        )

        self.grid_columnconfigure(0, weight=1)

        self._datos = []
        self._seleccion = None

        # -----------------------------------------
        # Etiqueta
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
            pady=(0,5)
        )

        # -----------------------------------------
        # Caja de texto
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

        self.entry.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        self.entry.bind(
            "<KeyRelease>",
            self._filtrar
        )

        # -----------------------------------------
        # Lista
        # -----------------------------------------

        self.lista = ctk.CTkScrollableFrame(

            self,

            fg_color="white",

            height=180,

            corner_radius=RADIO,

            border_width=1,

            border_color=COLOR_BORDE

        )

        self.lista.grid(
            row=2,
            column=0,
            sticky="ew",
            pady=(5,0)
        )

        self.lista.grid_remove()

    # =====================================================

    def cargar(self, elementos):

        """
        elementos:
        [
            (texto,objeto),
            ...
        ]
        """

        self._datos = elementos

        self._refrescar(elementos)

    # =====================================================

    def _filtrar(self, event=None):

        texto = self.entry.get().lower().strip()

        if texto == "":

            self.lista.grid_remove()

            return

        resultado = []

        for nombre, objeto in self._datos:

            if texto in nombre.lower():

                resultado.append(

                    (nombre,objeto)

                )

        self._refrescar(resultado)

    # =====================================================

    def _refrescar(self, datos):

        for widget in self.lista.winfo_children():

            widget.destroy()

        if len(datos)==0:

            self.lista.grid_remove()

            return

        self.lista.grid()

        for nombre,objeto in datos:

            boton = ctk.CTkButton(

                self.lista,

                text=nombre,

                fg_color="transparent",

                hover_color="#E8F5E9",

                text_color=COLOR_TEXTO,

                anchor="w",

                command=lambda n=nombre,o=objeto:
                    self._seleccionar(n,o)

            )

            boton.pack(
                fill="x",
                padx=2,
                pady=1
            )

    # =====================================================

    def _seleccionar(self,nombre,objeto):

        self.entry.delete(0,"end")

        self.entry.insert(0,nombre)

        self.lista.grid_remove()

        self._seleccion = objeto

    # =====================================================

    def get(self):

        return self._seleccion

    # =====================================================

    def limpiar(self):

        self.entry.delete(0,"end")

        self.lista.grid_remove()

        self._seleccion=None