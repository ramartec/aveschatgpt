import customtkinter as ctk

from presentacion.lista_observaciones import ListaObservaciones


class PanelInicio(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="#EEF2F6"
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

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

        ctk.CTkLabel(
            cabecera,
            text="Inicio",
            font=("Segoe UI", 30, "bold")
        ).grid(
            row=0,
            column=0,
            sticky="w"
        )

        self.btnNueva = ctk.CTkButton(
            cabecera,
            text="+ Nueva observación",
            width=190,
            height=40,
            fg_color="#16A34A",
            hover_color="#15803D",
            command=self.nueva_observacion
        )

        self.btnNueva.grid(
            row=0,
            column=1
        )

        # =====================================================
        # RESUMEN
        # =====================================================

        resumen = ctk.CTkFrame(
            self,
            fg_color="white",
            corner_radius=12
        )

        resumen.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20,
            pady=(0, 15)
        )

        ctk.CTkLabel(
            resumen,
            text="Observaciones recientes",
            font=("Segoe UI", 18, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        ctk.CTkLabel(
            resumen,
            text="Seleccione una observación para ver todos sus detalles.",
            font=("Segoe UI", 13)
        ).pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

        # =====================================================
        # LISTA
        # =====================================================

        self.lista = ListaObservaciones(self)

        self.lista.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(0, 20)
        )

    # =====================================================
    # ACTUALIZAR
    # =====================================================

    def actualizar(self):

        self.lista.actualizar()

    # =====================================================
    # NUEVA OBSERVACIÓN
    # =====================================================

    def nueva_observacion(self):

        if hasattr(self.master.master, "mostrar_nueva_observacion"):

            self.master.master.mostrar_nueva_observacion()