import customtkinter as ctk

from presentacion.detalle_observacion import DetalleObservacion


class PantallaDetalleObservacion(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="#EEF2F6"
        )

        self.master = master

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

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

        self.btnVolver = ctk.CTkButton(
            cabecera,
            text="← Volver",
            width=120,
            command=self.volver
        )

        self.btnVolver.pack(
            side="left"
        )

        self.lblTitulo = ctk.CTkLabel(
            cabecera,
            text="Detalle de la observación",
            font=("Segoe UI", 28, "bold")
        )

        self.lblTitulo.pack(
            side="left",
            padx=20
        )

        self.detalle = DetalleObservacion(self)

        self.detalle.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(0,20)
        )

    # =====================================================

    def mostrar(self, observacion):

        self.detalle.cargar(observacion)
    
    # =====================================================

    def volver(self):

        if hasattr(self.master, "mostrar_inicio"):

            self.master.mostrar_inicio()

    # =====================================================

    def actualizar(self, observacion):

        self.mostrar(observacion)