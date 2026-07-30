# presentacion/pantalla_nueva_observacion.py

import customtkinter as ctk


class PantallaNuevaObservacion(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="#EEF2F6"
        )

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # =====================================================
        # IZQUIERDA
        # =====================================================

        izquierda = ctk.CTkFrame(
            self,
            fg_color="white",
            corner_radius=12
        )

        izquierda.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(20, 10),
            pady=20
        )

        izquierda.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(

            izquierda,

            text="Nueva observación",

            font=("Segoe UI", 28, "bold")

        ).pack(
            anchor="w",
            padx=25,
            pady=(20, 5)
        )

        ctk.CTkLabel(

            izquierda,

            text="Complete la información de la observación.",

            text_color="gray"

        ).pack(
            anchor="w",
            padx=25
        )

        # ---------------------------------------

        foto = ctk.CTkFrame(

            izquierda,

            fg_color="#ECECEC",

            height=340,

            corner_radius=10

        )

        foto.pack(

            fill="x",

            padx=25,

            pady=25

        )

        ctk.CTkLabel(

            foto,

            text="Arrastre fotografías aquí\n\n📷",

            font=("Segoe UI", 22)

        ).place(

            relx=0.5,

            rely=0.5,

            anchor="center"

        )

        # ---------------------------------------

        botones = ctk.CTkFrame(

            izquierda,

            fg_color="transparent"

        )

        botones.pack(

            fill="x",

            padx=25,

            pady=5

        )

        ctk.CTkButton(

            botones,

            text="Agregar fotografías",

            width=180

        ).pack(

            side="left",

            padx=5

        )

        ctk.CTkButton(

            botones,

            text="Agregar videos",

            width=180

        ).pack(

            side="left",

            padx=5

        )

        ctk.CTkButton(

            botones,

            text="Agregar audios",

            width=180

        ).pack(

            side="left",

            padx=5

        )

        # =====================================================
        # DERECHA
        # =====================================================

        derecha = ctk.CTkFrame(
            self,
            fg_color="white",
            corner_radius=12
        )

        derecha.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(10, 20),
            pady=20
        )

        campos = [

            "Nombre común",

            "Nombre científico",

            "Provincia",

            "Cantón",

            "Distrito",

            "Lugar",

            "Fecha",

            "Hora",

            "Sexo"

        ]

        self.entradas = {}

        for campo in campos:

            ctk.CTkLabel(

                derecha,

                text=campo,

                font=("Segoe UI", 13, "bold")

            ).pack(

                anchor="w",

                padx=20,

                pady=(12, 3)

            )

            entrada = ctk.CTkEntry(

                derecha,

                height=38

            )

            entrada.pack(

                fill="x",

                padx=20

            )

            self.entradas[campo] = entrada

        # ---------------------------------------

        ctk.CTkLabel(

            derecha,

            text="Notas",

            font=("Segoe UI", 13, "bold")

        ).pack(

            anchor="w",

            padx=20,

            pady=(12, 3)

        )

        self.txtNotas = ctk.CTkTextbox(

            derecha,

            height=120

        )

        self.txtNotas.pack(

            fill="x",

            padx=20

        )

        # ---------------------------------------

        inferior = ctk.CTkFrame(

            derecha,

            fg_color="transparent"

        )

        inferior.pack(

            fill="x",

            padx=20,

            pady=20

        )

        ctk.CTkButton(

            inferior,

            text="Cancelar",

            width=140,

            fg_color="#9CA3AF"

        ).pack(

            side="left"

        )

        ctk.CTkButton(

            inferior,

            text="Guardar observación",

            width=180,

            fg_color="#16A34A",

            hover_color="#15803D"

        ).pack(

            side="right"

        )