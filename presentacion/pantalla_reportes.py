import customtkinter as ctk

from dao.observacion_dao import ObservacionDAO
from dao.especie_dao import EspecieDAO
from dao.ubicacion_dao import UbicacionDAO


class PantallaReportes(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="#EEF2F6"
        )

        self.master = master

        self.observacionDAO = ObservacionDAO()
        self.especieDAO = EspecieDAO()
        self.ubicacionDAO = UbicacionDAO()

        self.grid_columnconfigure((0, 1), weight=1)
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
            columnspan=2,
            sticky="ew",
            padx=20,
            pady=(20, 10)
        )

        cabecera.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(

            cabecera,

            text="Reportes",

            font=("Segoe UI", 28, "bold")

        ).grid(

            row=0,

            column=0,

            sticky="w"

        )

        # =====================================================
        # TARJETAS
        # =====================================================

        self.panel = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.panel.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="nsew",
            padx=20,
            pady=(0, 20)
        )

        self.panel.grid_columnconfigure((0, 1), weight=1)

        self.tarjetaObservaciones = self.crear_tarjeta(
            "Observaciones",
            "0",
            0,
            0
        )

        self.tarjetaEspecies = self.crear_tarjeta(
            "Especies",
            "0",
            0,
            1
        )

        self.tarjetaUbicaciones = self.crear_tarjeta(
            "Ubicaciones",
            "0",
            1,
            0
        )

        self.tarjetaArchivos = self.crear_tarjeta(
            "Archivos",
            "0",
            1,
            1
        )

        self.actualizar()
    
    # =====================================================
    # CREAR TARJETA
    # =====================================================

    def crear_tarjeta(self, titulo, valor, fila, columna):

        tarjeta = ctk.CTkFrame(

            self.panel,

            fg_color="white",

            corner_radius=12

        )

        tarjeta.grid(

            row=fila,

            column=columna,

            padx=10,

            pady=10,

            sticky="nsew"

        )

        ctk.CTkLabel(

            tarjeta,

            text=titulo,

            font=("Segoe UI", 18, "bold")

        ).pack(

            pady=(25, 5)

        )

        lblValor = ctk.CTkLabel(

            tarjeta,

            text=valor,

            font=("Segoe UI", 42, "bold"),

            text_color="#16A34A"

        )

        lblValor.pack(

            pady=(0, 25)

        )

        return lblValor

    # =====================================================
    # ACTUALIZAR
    # =====================================================

    def actualizar(self):

        try:

            observaciones = self.observacionDAO.listar()

        except Exception as e:

            print(e)

            observaciones = []

        try:

            especies = self.especieDAO.listar()

        except Exception as e:

            print(e)

            especies = []

        try:

            ubicaciones = self.ubicacionDAO.listar()

        except Exception as e:

            print(e)

            ubicaciones = []

        totalArchivos = 0

        for observacion in observaciones:

            if getattr(observacion, "archivos", None):

                totalArchivos += len(observacion.archivos)

        self.tarjetaObservaciones.configure(

            text=str(len(observaciones))

        )

        self.tarjetaEspecies.configure(

            text=str(len(especies))

        )

        self.tarjetaUbicaciones.configure(

            text=str(len(ubicaciones))

        )

        self.tarjetaArchivos.configure(

            text=str(totalArchivos)

        )