# presentacion/pantalla_especies.py

import customtkinter as ctk

from dao.especie_dao import EspecieDAO


class PantallaEspecies(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="#EEF2F6"
        )

        self.master = master

        self.dao = EspecieDAO()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # =====================================================
        # CABECERA
        # =====================================================

        cabecera = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        cabecera.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=20,
            pady=(20, 10)
        )

        cabecera.grid_columnconfigure(0, weight=1)

        self.lblTitulo = ctk.CTkLabel(
            cabecera,
            text="Especies",
            font=("Segoe UI", 28, "bold")
        )

        self.lblTitulo.grid(
            row=0,
            column=0,
            sticky="w"
        )

        self.btnNueva = ctk.CTkButton(
            cabecera,
            text="+ Nueva especie",
            width=180,
            height=40,
            fg_color="#16A34A",
            hover_color="#15803D",
            command=self.nueva_especie
        )

        self.btnNueva.grid(
            row=0,
            column=1,
            padx=(10, 0)
        )

        # =====================================================
        # TABLA
        # =====================================================

        self.tabla = ctk.CTkScrollableFrame(
            self,
            fg_color="white",
            corner_radius=12
        )

        self.tabla.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(0, 20)
        )

        encabezados = [

            ("Nombre común", 220),
            ("Nombre científico", 260),
            ("Familia", 180),
            ("Orden", 180),
            ("Observaciones", 120),
            ("", 40)

        ]

        fila = ctk.CTkFrame(
            self.tabla,
            fg_color="#F3F4F6",
            height=42
        )

        fila.pack(fill="x")

        for texto, ancho in encabezados:

            ctk.CTkLabel(
                fila,
                text=texto,
                width=ancho,
                anchor="w",
                font=("Segoe UI", 13, "bold")
            ).pack(
                side="left",
                padx=6,
                pady=8
            )

        self.cargar_especies()


    # =====================================================
    # CARGAR ESPECIES
    # =====================================================

    def cargar_especies(self):

        for widget in self.tabla.winfo_children()[1:]:

            widget.destroy()

        try:

            especies = self.dao.listar()

        except Exception as e:

            print(e)

            especies = []

        for especie in especies:

            fila = ctk.CTkFrame(
                self.tabla,
                fg_color="white",
                height=55
            )

            fila.pack(
                fill="x",
                pady=2
            )

            familia = ""

            orden = ""

            if especie.genero is not None:

                if especie.genero.familia is not None:

                    familia = especie.genero.familia.nombre

                    if especie.genero.familia.orden is not None:

                        orden = especie.genero.familia.orden.nombre

            columnas = [

                especie.nombre_comun,
                especie.nombre_cientifico,
                familia,
                orden,
                "0"

            ]

            anchos = [

                220,
                260,
                180,
                180,
                120

            ]

            for texto, ancho in zip(columnas, anchos):

                ctk.CTkLabel(
                    fila,
                    text=texto,
                    width=ancho,
                    anchor="w",
                    font=("Segoe UI", 13)
                ).pack(
                    side="left",
                    padx=6
                )

            ctk.CTkButton(
                fila,
                text="⋮",
                width=35,
                fg_color="transparent",
                hover_color="#EEEEEE",
                text_color="black",
                command=lambda e=especie: self.menu_especie(e)
            ).pack(
                side="right",
                padx=10
            )

        if not especies:

            ctk.CTkLabel(
                self.tabla,
                text="No hay especies registradas.",
                text_color="gray",
                font=("Segoe UI", 16)
            ).pack(
                pady=30
            )

    # =====================================================
    # NUEVA ESPECIE
    # =====================================================

    def nueva_especie(self):

        if hasattr(self.master, "mostrar_nueva_especie"):

            self.master.mostrar_nueva_especie()

        elif hasattr(self.master.master, "mostrar_nueva_especie"):

            self.master.master.mostrar_nueva_especie()

        else:

            print("Pantalla de nueva especie aún no implementada.")

    # =====================================================
    # MENÚ CONTEXTUAL
    # =====================================================

    def menu_especie(self, especie):

        print(
            f"Especie seleccionada: {especie.nombre_comun}"
        )

        # Aquí luego agregaremos:
        # Editar
        # Eliminar
        # Ver observaciones

    # =====================================================
    # ACTUALIZAR
    # =====================================================

    def actualizar(self):

        self.cargar_especies()
