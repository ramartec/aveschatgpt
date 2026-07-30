import customtkinter as ctk

from presentacion.lista_observaciones import ListaObservaciones


class PantallaInicio(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="#EEF2F6"
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # =====================================================
        # TITULO
        # =====================================================

        titulo = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        titulo.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=20,
            pady=(20, 10)
        )

        ctk.CTkLabel(

            titulo,

            text="Observaciones",

            font=("Segoe UI", 30, "bold")

        ).pack(

            side="left"

        )

        # =====================================================
        # ESTADISTICAS
        # =====================================================

        estadisticas = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        estadisticas.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=20
        )

        estadisticas.grid_columnconfigure((0,1,2), weight=1)

        self.lblObservaciones = self.crear_tarjeta(
            estadisticas,
            0,
            "Observaciones",
            "0"
        )

        self.lblEspecies = self.crear_tarjeta(
            estadisticas,
            1,
            "Especies",
            "0"
        )

        self.lblUbicaciones = self.crear_tarjeta(
            estadisticas,
            2,
            "Ubicaciones",
            "0"
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
            pady=(20,20)
        )
    
    # =====================================================
    # CREAR TARJETA
    # =====================================================

    def crear_tarjeta(self, parent, columna, titulo, valor):

        tarjeta = ctk.CTkFrame(
            parent,
            fg_color="white",
            corner_radius=12
        )

        tarjeta.grid(
            row=0,
            column=columna,
            padx=8,
            pady=5,
            sticky="ew"
        )

        ctk.CTkLabel(
            tarjeta,
            text=titulo,
            font=("Segoe UI", 16, "bold")
        ).pack(
            pady=(18, 5)
        )

        lblValor = ctk.CTkLabel(
            tarjeta,
            text=valor,
            font=("Segoe UI", 34, "bold"),
            text_color="#16A34A"
        )

        lblValor.pack(
            pady=(0, 18)
        )

        return lblValor

    # =====================================================
    # ACTUALIZAR
    # =====================================================

    def actualizar(self):

        if hasattr(self.lista, "actualizar"):

            self.lista.actualizar()

        try:

            observaciones = self.lista.dao.listar()

            self.lblObservaciones.configure(
                text=str(len(observaciones))
            )

            especies = set()
            ubicaciones = set()

            for observacion in observaciones:

                if getattr(observacion, "especie", None):

                    especies.add(observacion.especie.id_especie)

                if getattr(observacion, "ubicacion", None):

                    ubicaciones.add(observacion.ubicacion.id_ubicacion)

            self.lblEspecies.configure(
                text=str(len(especies))
            )

            self.lblUbicaciones.configure(
                text=str(len(ubicaciones))
            )

        except Exception as error:

            print(error)