import customtkinter as ctk

from dao.observacion_dao import ObservacionDAO
from dao.especie_dao import EspecieDAO
from dao.ubicacion_dao import UbicacionDAO


class PantallaEstadisticas(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="#EEF2F6"
        )

        self.observacionDAO = ObservacionDAO()
        self.especieDAO = EspecieDAO()
        self.ubicacionDAO = UbicacionDAO()

        self.grid_columnconfigure((0, 1), weight=1)

        titulo = ctk.CTkLabel(
            self,
            text="Estadísticas",
            font=("Segoe UI", 28, "bold")
        )

        titulo.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="w",
            padx=20,
            pady=(20, 15)
        )

        self.lblObservaciones = self.crear_tarjeta(
            1,
            0,
            "Observaciones"
        )

        self.lblEspecies = self.crear_tarjeta(
            1,
            1,
            "Especies"
        )

        self.lblUbicaciones = self.crear_tarjeta(
            2,
            0,
            "Ubicaciones"
        )

        self.lblArchivos = self.crear_tarjeta(
            2,
            1,
            "Archivos"
        )

        self.actualizar()

    # =====================================================

    def crear_tarjeta(self, fila, columna, titulo):

        tarjeta = ctk.CTkFrame(
            self,
            fg_color="white",
            corner_radius=12
        )

        tarjeta.grid(
            row=fila,
            column=columna,
            sticky="nsew",
            padx=10,
            pady=10
        )

        ctk.CTkLabel(
            tarjeta,
            text=titulo,
            font=("Segoe UI", 18, "bold")
        ).pack(
            pady=(20, 5)
        )

        valor = ctk.CTkLabel(
            tarjeta,
            text="0",
            font=("Segoe UI", 42, "bold"),
            text_color="#16A34A"
        )

        valor.pack(
            pady=(0, 20)
        )

        return valor
    
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

        total_archivos = 0

        for observacion in observaciones:

            if getattr(observacion, "archivos", None):

                total_archivos += len(observacion.archivos)

        self.lblObservaciones.configure(
            text=str(len(observaciones))
        )

        self.lblEspecies.configure(
            text=str(len(especies))
        )

        self.lblUbicaciones.configure(
            text=str(len(ubicaciones))
        )

        self.lblArchivos.configure(
            text=str(total_archivos)
        )
    # =====================================================
    # REFRESCAR
    # =====================================================

    def refrescar(self):

        self.actualizar()