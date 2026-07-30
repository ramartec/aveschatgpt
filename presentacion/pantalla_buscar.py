import customtkinter as ctk

from dao.observacion_dao import ObservacionDAO


class PantallaBuscar(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="#EEF2F6"
        )

        self.master = master

        self.dao = ObservacionDAO()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

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

        self.lblTitulo = ctk.CTkLabel(
            cabecera,
            text="Buscar observaciones",
            font=("Segoe UI", 28, "bold")
        )

        self.lblTitulo.grid(
            row=0,
            column=0,
            sticky="w"
        )

        self.txtBuscar = ctk.CTkEntry(
            cabecera,
            placeholder_text="Nombre común, científico o lugar..."
        )

        self.txtBuscar.grid(
            row=0,
            column=1,
            padx=10,
            sticky="ew"
        )

        self.txtBuscar.bind(
            "<KeyRelease>",
            self.buscar
        )

        self.resultados = ctk.CTkScrollableFrame(
            self,
            fg_color="white",
            corner_radius=12
        )

        self.resultados.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(0, 20)
        )

        self.buscar()
    
        # =====================================================
    # BUSCAR
    # =====================================================

    def buscar(self, event=None):

        for widget in self.resultados.winfo_children():

            widget.destroy()

        texto = self.txtBuscar.get().strip().lower()

        try:

            observaciones = self.dao.listar()

        except Exception as e:

            print(e)

            observaciones = []

        encontrados = 0

        for observacion in observaciones:

            nombre_comun = ""
            nombre_cientifico = ""
            lugar = ""

            if getattr(observacion, "especie", None):

                nombre_comun = observacion.especie.nombre_comun or ""
                nombre_cientifico = observacion.especie.nombre_cientifico or ""

            if getattr(observacion, "ubicacion", None):

                lugar = observacion.ubicacion.sitio or ""

            if texto:

                contenido = " ".join([

                    nombre_comun.lower(),
                    nombre_cientifico.lower(),
                    lugar.lower()

                ])

                if texto not in contenido:

                    continue

            encontrados += 1

            tarjeta = ctk.CTkFrame(

                self.resultados,

                fg_color="white",

                corner_radius=10,

                border_width=1,

                border_color="#E5E7EB"

            )

            tarjeta.pack(

                fill="x",

                padx=10,

                pady=5

            )

            ctk.CTkLabel(

                tarjeta,

                text=nombre_comun,

                font=("Segoe UI", 18, "bold"),

                anchor="w"

            ).pack(

                anchor="w",

                padx=15,

                pady=(10, 0)

            )

            ctk.CTkLabel(

                tarjeta,

                text=nombre_cientifico,

                font=("Segoe UI", 13, "italic"),

                text_color="#6B7280",

                anchor="w"

            ).pack(

                anchor="w",

                padx=15

            )

            ctk.CTkLabel(

                tarjeta,

                text=f"📍 {lugar}",

                anchor="w"

            ).pack(

                anchor="w",

                padx=15,

                pady=(0, 10)

            )

            tarjeta.bind(

                "<Button-1>",

                lambda e, o=observacion: self.abrir_observacion(o)

            )

        if encontrados == 0:

            ctk.CTkLabel(

                self.resultados,

                text="No se encontraron observaciones.",

                font=("Segoe UI", 16),

                text_color="gray"

            ).pack(

                pady=30

            )
    # =====================================================
    # ABRIR
    # =====================================================

    def abrir_observacion(self, observacion):

        if hasattr(self.master, "mostrar_detalle_observacion"):

            self.master.mostrar_detalle_observacion(observacion)