import customtkinter as ctk

from database.database import Database


class BarraEstado(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            height=32,
            fg_color="#E5E7EB",
            corner_radius=0
        )

        self.grid_columnconfigure(0, weight=1)

        self.lblEstado = ctk.CTkLabel(
            self,
            text="",
            anchor="w",
            font=("Segoe UI", 12)
        )

        self.lblEstado.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=15,
            pady=5
        )

        self.actualizar()

    # =====================================================

    def actualizar(self):

        if Database.probar_conexion():

            texto = "🟢 Base de datos conectada"

        else:

            texto = "🔴 Base de datos desconectada"

        self.lblEstado.configure(

            text=texto

        )