# presentacion/tabla_observaciones.py

import customtkinter as ctk


class TablaObservaciones(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="white",
            corner_radius=12
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # ==========================================
        # ENCABEZADOS
        # ==========================================

        encabezado = ctk.CTkFrame(
            self,
            fg_color="#F5F7FA",
            corner_radius=10,
            height=42
        )

        encabezado.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=10,
            pady=(10, 0)
        )

        columnas = [

            ("",70),

            ("Fecha",110),

            ("Especie",280),

            ("Ubicación",220),

            ("Sexo",90),

            ("Fotos",70),

            ("Videos",70),

            ("Audios",70),

            ("Notas",260),

            ("",40)

        ]

        for i, (texto, ancho) in enumerate(columnas):

            encabezado.grid_columnconfigure(i, weight=0)

            lbl = ctk.CTkLabel(

                encabezado,

                text=texto,

                width=ancho,

                font=("Segoe UI",13,"bold"),

                anchor="w"

            )

            lbl.grid(

                row=0,

                column=i,

                padx=6,

                pady=10,

                sticky="w"

            )

        # ==========================================

        self.scroll = ctk.CTkScrollableFrame(

            self,

            fg_color="white"

        )

        self.scroll.grid(

            row=1,

            column=0,

            sticky="nsew",

            padx=8,

            pady=(5,10)

        )

        self.scroll.grid_columnconfigure(
            0,
            weight=1
        )

    # ==============================================

    def limpiar(self):

        for widget in self.scroll.winfo_children():

            widget.destroy()

    # ==============================================

    def agregar_fila(self, fila):

        fila.pack(

            fill="x",

            padx=2,

            pady=2

        )