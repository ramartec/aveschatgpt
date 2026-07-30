import customtkinter as ctk


class PantallaAyuda(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="#EEF2F6"
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # ==========================================
        # CABECERA
        # ==========================================

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

        ctk.CTkLabel(

            cabecera,

            text="Ayuda",

            font=("Segoe UI", 28, "bold")

        ).pack(

            anchor="w"

        )

        # ==========================================
        # CONTENIDO
        # ==========================================

        panel = ctk.CTkScrollableFrame(

            self,

            fg_color="white",

            corner_radius=12

        )

        panel.grid(

            row=1,

            column=0,

            sticky="nsew",

            padx=20,

            pady=(0, 20)

        )

        self.crear_seccion(

            panel,

            "Registro de aves",

            "Permite registrar cada observación indicando especie, ubicación, fecha, sexo, comportamiento y notas."

        )

        self.crear_seccion(

            panel,

            "Fotografías",

            "Cada observación puede contener varias fotografías, videos y audios."

        )

        self.crear_seccion(

            panel,

            "Búsquedas",

            "Puede buscar por nombre común, nombre científico, ubicación y otros datos."

        )

        self.crear_seccion(

            panel,

            "Reportes",

            "Genera estadísticas del número de observaciones, especies y ubicaciones."

        )

        self.crear_seccion(

            panel,

            "Versión",

            "Registro de Aves de Ronald\nVersión 1.0"
        )
    
    # =====================================================
    # CREAR SECCION
    # =====================================================

    def crear_seccion(self, parent, titulo, descripcion):

        tarjeta = ctk.CTkFrame(

            parent,

            fg_color="#F8FAFC",

            corner_radius=10,

            border_width=1,

            border_color="#E5E7EB"

        )

        tarjeta.pack(

            fill="x",

            padx=15,

            pady=10

        )

        ctk.CTkLabel(

            tarjeta,

            text=titulo,

            font=("Segoe UI", 18, "bold"),

            anchor="w"

        ).pack(

            anchor="w",

            padx=15,

            pady=(15, 5)

        )

        ctk.CTkLabel(

            tarjeta,

            text=descripcion,

            justify="left",

            wraplength=850,

            anchor="w",

            font=("Segoe UI", 13)

        ).pack(

            anchor="w",

            padx=15,

            pady=(0, 15)

        )