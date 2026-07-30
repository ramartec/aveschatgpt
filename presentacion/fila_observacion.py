# presentacion/fila_observacion.py

import os
import customtkinter as ctk
from PIL import Image


class FilaObservacion(ctk.CTkFrame):

    ALTO = 72

    def __init__(
        self,
        master,
        imagen,
        fecha,
        especie,
        cientifico,
        ubicacion,
        sexo,
        fotos,
        videos,
        audios,
        notas,
        comando=None
    ):

        super().__init__(
            master,
            fg_color="white",
            corner_radius=8,
            height=self.ALTO
        )

        self.comando = comando

        self.grid_columnconfigure(2, weight=1)
        self.configure(cursor="hand2")

        # ==========================================
        # MINIATURA
        # ==========================================

        self.imagen = self.cargar_imagen(imagen)

        lblImagen = ctk.CTkLabel(
            self,
            image=self.imagen,
            text=""
        )

        lblImagen.grid(
            row=0,
            column=0,
            padx=(10, 15),
            pady=8
        )

        # ==========================================

        ctk.CTkLabel(
            self,
            text=fecha,
            width=95,
            anchor="w",
            font=("Segoe UI", 12)
        ).grid(
            row=0,
            column=1,
            sticky="w"
        )

        # ==========================================

        cont = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        cont.grid(
            row=0,
            column=2,
            sticky="ew",
            padx=(15, 10)
        )

        ctk.CTkLabel(
            cont,
            text=especie,
            font=("Segoe UI", 14, "bold"),
            anchor="w"
        ).pack(anchor="w")

        ctk.CTkLabel(
            cont,
            text=cientifico,
            font=("Segoe UI", 11, "italic"),
            text_color="#6B7280",
            anchor="w"
        ).pack(anchor="w")

        # ==========================================

        ctk.CTkLabel(
            self,
            text=ubicacion,
            width=180,
            anchor="w",
            font=("Segoe UI", 12)
        ).grid(
            row=0,
            column=3,
            sticky="w"
        )

        # ==========================================

        color = "#2E8B57"

        if sexo == "Hembra":
            color = "#D63384"

        elif sexo == "Indeterminado":
            color = "#6C757D"

        ctk.CTkLabel(
            self,
            text=sexo,
            width=90,
            height=28,
            corner_radius=14,
            fg_color=color,
            text_color="white",
            font=("Segoe UI", 11, "bold")
        ).grid(
            row=0,
            column=4,
            padx=10
        )

        # ==========================================

        ctk.CTkLabel(
            self,
            text=str(fotos),
            width=55
        ).grid(
            row=0,
            column=5
        )

        ctk.CTkLabel(
            self,
            text=str(videos),
            width=55
        ).grid(
            row=0,
            column=6
        )

        ctk.CTkLabel(
            self,
            text=str(audios),
            width=55
        ).grid(
            row=0,
            column=7
        )

        # ==========================================

        ctk.CTkLabel(
            self,
            text=notas,
            width=240,
            anchor="w",
            font=("Segoe UI", 12)
        ).grid(
            row=0,
            column=8,
            sticky="w",
            padx=(10, 0)
        )

        # ==========================================

        ctk.CTkButton(
            self,
            text="⋮",
            width=32,
            height=32,
            fg_color="transparent",
            hover_color="#EAEAEA",
            text_color="black",
            font=("Segoe UI", 18)
        ).grid(
            row=0,
            column=9,
            padx=10
        )

        # ==========================================
        # HOVER
        # ==========================================

        self.bind("<Enter>", self.mouse_entra)
        self.bind("<Leave>", self.mouse_sale)
        self.bind("<Button-1>", self.click)

        for w in self.winfo_children():

            w.bind("<Enter>", self.mouse_entra)
            w.bind("<Leave>", self.mouse_sale)
            w.bind("<Button-1>", self.click)

    # ==================================================

    def cargar_imagen(self, ruta):

        if not os.path.exists(ruta):

            ruta = "recursos/iconos/sin_imagen.png"

        img = Image.open(ruta)

        return ctk.CTkImage(

            light_image=img,

            dark_image=img,

            size=(54, 54)

        )

    # ==================================================

    def mouse_entra(self, event):

        self.configure(
            fg_color="#F7FAFC"
        )

    # ==================================================

    def mouse_sale(self, event):

        self.configure(
            fg_color="white"
        )

    # ==================================================

    def click(self, event):

        if self.comando:

            self.comando()