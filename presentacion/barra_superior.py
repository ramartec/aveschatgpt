import customtkinter as ctk


class BarraSuperior(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            height=70,
            fg_color="white",
            corner_radius=0
        )

        self.grid_columnconfigure(0, weight=1)

        self.lblTitulo = ctk.CTkLabel(
            self,
            text="Registro de Aves de Ronald",
            font=("Segoe UI", 20, "bold")
        )

        self.lblTitulo.grid(
            row=0,
            column=0,
            sticky="w",
            padx=20,
            pady=15
        )

        self.lblUsuario = ctk.CTkLabel(
            self,
            text="Bienvenido, Ronald",
            font=("Segoe UI", 14)
        )

        self.lblUsuario.grid(
            row=0,
            column=1,
            padx=(0, 20)
        )