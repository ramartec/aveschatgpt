import customtkinter as ctk


class MenuLateral(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            width=230,
            fg_color="#1F2937",
            corner_radius=0
        )

        self.master = master

        self.grid_propagate(False)

        ctk.CTkLabel(
            self,
            text="Registro de\nAves",
            font=("Segoe UI", 24, "bold"),
            text_color="white"
        ).pack(
            pady=(30, 35)
        )

        botones = [

            ("🏠 Inicio", self.master.mostrar_inicio),

            ("➕ Nueva observación", self.master.mostrar_nueva_observacion),

            ("🦜 Observaciones", self.master.mostrar_observaciones),

            ("🐦 Especies", self.master.mostrar_especies),

            ("📍 Ubicaciones", self.master.mostrar_ubicaciones),

            ("🔎 Buscar", self.master.mostrar_busqueda),

            ("📊 Estadísticas", self.master.mostrar_estadisticas),

            ("📄 Reportes", self.master.mostrar_reportes),

            ("⚙ Configuración", self.master.mostrar_configuracion),

            ("❓ Ayuda", self.master.mostrar_ayuda),

            ("ℹ Acerca de", self.master.mostrar_acerca)

        ]

        for texto, comando in botones:

            ctk.CTkButton(

                self,

                text=texto,

                command=comando,

                height=42,

                anchor="w",

                fg_color="transparent",

                hover_color="#374151",

                corner_radius=8,

                font=("Segoe UI", 15)

            ).pack(

                fill="x",

                padx=12,

                pady=3

            )

        ctk.CTkButton(

            self,

            text="Salir",

            height=42,

            fg_color="#DC2626",

            hover_color="#B91C1C",

            command=self.salir

        ).pack(

            side="bottom",

            fill="x",

            padx=12,

            pady=15

        )

    # =====================================================
    
    def salir(self):
        self.master.destroy()