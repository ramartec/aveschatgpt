import customtkinter as ctk

from dao.observacion_dao import ObservacionDAO
from presentacion.tarjeta_observacion import TarjetaObservacion


class ListaObservaciones(ctk.CTkScrollableFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="transparent"
        )

        self.master = master

        self.dao = ObservacionDAO()

        self.grid_columnconfigure(0, weight=1)

        self.actualizar()

    # =====================================================

    def actualizar(self):

        for widget in self.winfo_children():

            widget.destroy()

        observaciones = self.dao.listar()

        if len(observaciones) == 0:

            ctk.CTkLabel(

                self,

                text="No hay observaciones registradas.",

                font=("Segoe UI", 18),

                text_color="gray"

            ).pack(

                pady=40

            )

            return

        for observacion in observaciones:

            ruta_imagen = None

            cantidad_archivos = 0

            if hasattr(observacion, "archivos"):

                cantidad_archivos = len(observacion.archivos)

                for archivo in observacion.archivos:

                    if archivo.tipo == "Fotografia":

                        ruta_imagen = archivo.ruta

                        break

            nombre_comun = ""

            nombre_cientifico = ""

            if getattr(observacion, "especie", None):

                nombre_comun = observacion.especie.nombre_comun

                nombre_cientifico = observacion.especie.nombre_cientifico

            lugar = ""

            if getattr(observacion, "ubicacion", None):

                lugar = observacion.ubicacion.sitio
    
            fecha = ""

            if getattr(observacion, "fecha", None):

                fecha = str(observacion.fecha)

            tarjeta = TarjetaObservacion(

                self,

                ruta_imagen=ruta_imagen,

                nombre_comun=nombre_comun,

                nombre_cientifico=nombre_cientifico,

                lugar=lugar,

                fecha=fecha,

                cantidad_archivos=f"{cantidad_archivos} archivo(s)",

                comando=lambda o=observacion: self.abrir_observacion(o)

            )

            tarjeta.pack(

                fill="x",

                padx=10,

                pady=8

            )

    # =====================================================

    def abrir_observacion(self, observacion):

        if hasattr(self.master, "mostrar_detalle_observacion"):

            self.master.mostrar_detalle_observacion(observacion)