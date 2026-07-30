#tabla_observacion.py

import customtkinter as ctk
from util.imagenes import Imagenes



class TarjetaObservacion(ctk.CTkFrame):

    ANCHO_MINIATURA = 115
    ALTO_MINIATURA = 115
    

    def __init__(
        self,
        master,
        ruta_imagen,
        nombre_comun,
        nombre_cientifico,
        lugar,
        fecha,
        cantidad_archivos,
        comando=None
    ):

        super().__init__(
            master,
            fg_color="white",
            corner_radius=12,
            border_width=1,
            border_color="#E5E7EB",
            height=145
        )

        self.comando = comando

        self.grid_columnconfigure(1, weight=1)

        self.imagen = Imagenes.miniatura(ruta_imagen)

        # =============================================
        # MINIATURA
        # =============================================

        self.lblImagen = ctk.CTkLabel(
            self,
            image=self.imagen,
            text=""
        )

        self.lblImagen.grid(
            row=0,
            column=0,
            rowspan=5,
            padx=18,
            pady=15
        )

        # =============================================
        # NOMBRE COMÚN
        # =============================================

        self.lblNombre = ctk.CTkLabel(
            self,
            text=nombre_comun,
            font=("Segoe UI", 21, "bold"),
            anchor="w"
        )

        self.lblNombre.grid(
            row=0,
            column=1,
            sticky="w",
            pady=(15, 0)
        )

        # =============================================

        self.lblCientifico = ctk.CTkLabel(
            self,
            text=nombre_cientifico,
            font=("Segoe UI", 14, "italic"),
            text_color="#6B7280"
        )

        self.lblCientifico.grid(
            row=1,
            column=1,
            sticky="w"
        )

        # =============================================

        self.lblLugar = ctk.CTkLabel(
            self,
            text=f"📍 {lugar}",
            font=("Segoe UI", 13)
        )

        self.lblLugar.grid(
            row=2,
            column=1,
            sticky="w",
            pady=(5, 0)
        )

        # =============================================

        self.lblFecha = ctk.CTkLabel(
            self,
            text=f"📅 {fecha}",
            font=("Segoe UI", 13)
        )

        self.lblFecha.grid(
            row=3,
            column=1,
            sticky="w"
        )

        # =============================================

        self.lblArchivos = ctk.CTkLabel(
            self,
            text=cantidad_archivos,
            font=("Segoe UI", 13),
            text_color="#256D47"
        )

        self.lblArchivos.grid(
            row=4,
            column=1,
            sticky="w",
            pady=(0, 15)
        )

        # =============================================
        # FLECHA
        # =============================================

        self.lblFlecha = ctk.CTkLabel(
            self,
            text="❯",
            font=("Segoe UI", 28),
            text_color="#B0B0B0"
        )

        self.lblFlecha.grid(
            row=0,
            column=2,
            rowspan=5,
            padx=20
        )

        # =============================================
        # HOVER
        # =============================================

        self.widgets = [self]

        self.widgets.extend(self.winfo_children())

        for widget in self.widgets:

            widget.bind("<Enter>", self.mouse_entra)

            widget.bind("<Leave>", self.mouse_sale)

            widget.bind("<Button-1>", self.click)

    # ==================================================

    # ==================================================

    def mouse_entra(self, event):

        self.configure(

            fg_color="#F8FAFC",

            border_color="#2E8B57"

        )

    # ==================================================

    def mouse_sale(self, event):

        self.configure(

            fg_color="white",

            border_color="#E5E7EB"

        )

    # ==================================================

    def click(self, event):

        if self.comando:

            self.comando()