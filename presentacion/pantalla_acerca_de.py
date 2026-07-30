import customtkinter as ctk


class PantallaAcercaDe(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="#EEF2F6"
        )

        self.grid_columnconfigure(0, weight=1)

        cabecera = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        cabecera.pack(
            fill="x",
            padx=20,
            pady=(20,10)
        )

        ctk.CTkLabel(
            cabecera,
            text="Acerca de",
            font=("Segoe UI",28,"bold")
        ).pack(anchor="w")

        panel = ctk.CTkFrame(
            self,
            fg_color="white",
            corner_radius=12
        )

        panel.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0,20)
        )

        ctk.CTkLabel(
            panel,
            text="Registro de Aves de Ronald",
            font=("Segoe UI",24,"bold")
        ).pack(
            pady=(30,10)
        )

        ctk.CTkLabel(
            panel,
            text="Versión 1.0",
            font=("Segoe UI",16)
        ).pack()

        ctk.CTkLabel(
            panel,
            text="Aplicación para registrar observaciones de aves\ncon fotografías, videos, audios y ubicaciones.",
            justify="center",
            font=("Segoe UI",14)
        ).pack(
            pady=20
        )

        ctk.CTkLabel(
            panel,
            text="Desarrollado por Ronald Arias",
            font=("Segoe UI",16,"bold")
        ).pack(
            pady=(20,5)
        )

        ctk.CTkLabel(
            panel,
            text="Universidad de Costa Rica",
            font=("Segoe UI",14)
        ).pack()

        ctk.CTkLabel(
            panel,
            text="2026",
            font=("Segoe UI",14)
        ).pack(
            pady=(0,30)
        )
    
    # =====================================================
    # INFORMACIÓN
    # =====================================================

        separador = ctk.CTkFrame(
            panel,
            fg_color="#E5E7EB",
            height=2
        )

        separador.pack(
            fill="x",
            padx=40,
            pady=15
        )

        informacion = [

            ("Python", "3.14"),
            ("CustomTkinter", "Interfaz gráfica"),
            ("MySQL", "Base de datos"),
            ("Pillow", "Procesamiento de imágenes"),
            ("Licencia", "Uso personal"),
            ("Repositorio", "Registro de Aves de Ronald")

        ]

        for titulo, valor in informacion:

            fila = ctk.CTkFrame(
                panel,
                fg_color="transparent"
            )

            fila.pack(
                fill="x",
                padx=35,
                pady=5
            )

            ctk.CTkLabel(
                fila,
                text=titulo,
                width=170,
                anchor="w",
                font=("Segoe UI", 14, "bold")
            ).pack(
                side="left"
            )

            ctk.CTkLabel(
                fila,
                text=valor,
                anchor="w",
                font=("Segoe UI", 14)
            ).pack(
                side="left"
            )

        ctk.CTkButton(
            panel,
            text="Cerrar",
            width=170,
            fg_color="#16A34A",
            hover_color="#15803D",
            command=self.cerrar
        ).pack(
            pady=30
        )

    # =====================================================
    # CERRAR
    # =====================================================

    def cerrar(self):

        if hasattr(self.master, "mostrar_inicio"):

            self.master.mostrar_inicio()