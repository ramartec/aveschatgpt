import customtkinter as ctk

from dao.ubicacion_dao import UbicacionDAO


class PantallaUbicaciones(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="#EEF2F6"
        )

        self.master = master

        self.dao = UbicacionDAO()

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
            text="Ubicaciones",
            font=("Segoe UI", 28, "bold")
        )

        self.lblTitulo.grid(
            row=0,
            column=0,
            sticky="w"
        )

        self.btnNueva = ctk.CTkButton(
            cabecera,
            text="+ Nueva ubicación",
            width=180,
            height=40,
            fg_color="#16A34A",
            hover_color="#15803D",
            command=self.nueva_ubicacion
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

            ("Sitio", 220),
            ("Distrito", 170),
            ("Cantón", 170),
            ("Provincia", 170),
            ("Altitud", 110),
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

        self.cargar_ubicaciones()
    
    # =====================================================
    # CARGAR UBICACIONES
    # =====================================================

    def cargar_ubicaciones(self):

        for widget in self.tabla.winfo_children()[1:]:

            widget.destroy()

        ubicaciones = self.dao.listar()

        for ubicacion in ubicaciones:

            fila = ctk.CTkFrame(

                self.tabla,

                fg_color="white",

                height=55

            )

            fila.pack(

                fill="x",

                pady=2

            )

            altitud = ""

            if getattr(ubicacion, "altitud", None) is not None:

                altitud = f"{ubicacion.altitud} m"

            columnas = [

                ubicacion.sitio,
                ubicacion.distrito,
                ubicacion.canton,
                ubicacion.provincia,
                altitud

            ]

            anchos = [

                220,
                170,
                170,
                170,
                110

            ]

            for texto, ancho in zip(columnas, anchos):

                ctk.CTkLabel(

                    fila,

                    text=str(texto),

                    width=ancho,

                    anchor="w",

                    font=("Segoe UI", 13)

                ).pack(

                    side="left",

                    padx=6

                )

            boton = ctk.CTkButton(

                fila,

                text="⋮",

                width=35,

                fg_color="transparent",

                hover_color="#EEEEEE",

                text_color="black",

                command=lambda u=ubicacion: self.menu_ubicacion(u)

            )

            boton.pack(

                side="right",

                padx=10

            )

    # =====================================================
    # NUEVA UBICACION
    # =====================================================

    def nueva_ubicacion(self):

        if hasattr(self.master, "mostrar_nueva_ubicacion"):

            self.master.mostrar_nueva_ubicacion()

    # =====================================================
    # MENU
    # =====================================================

    def menu_ubicacion(self, ubicacion):

        print(

            f"Ubicación seleccionada: {ubicacion.sitio}"

        )

    # =====================================================
    # ACTUALIZAR
    # =====================================================

    def actualizar(self):

        self.cargar_ubicaciones()