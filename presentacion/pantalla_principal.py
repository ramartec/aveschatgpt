import customtkinter as ctk

from presentacion.menu_lateral import MenuLateral
from presentacion.barra_superior import BarraSuperior
from presentacion.barra_estado import BarraEstado

from presentacion.panel_inicio import PanelInicio
from presentacion.tabla_observaciones import TablaObservaciones
from presentacion.pantalla_nueva_observacion import PantallaNuevaObservacion
from presentacion.pantalla_detalle_observacion import PantallaDetalleObservacion
from presentacion.pantalla_especies import PantallaEspecies
from presentacion.pantalla_ubicaciones import PantallaUbicaciones
from presentacion.pantalla_buscar import PantallaBuscar
from presentacion.pantalla_reportes import PantallaReportes
from presentacion.pantalla_estadisticas import PantallaEstadisticas
from presentacion.pantalla_configuracion import PantallaConfiguracion
from presentacion.pantalla_ayuda import PantallaAyuda
from presentacion.pantalla_acerca_de import PantallaAcercaDe


class VentanaPrincipal(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.title("Registro de Aves de Ronald")

        # =====================================================
        # TAMAÑO AUTOMÁTICO DE LA VENTANA
        # =====================================================

        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()

        ancho = int(ancho_pantalla * 0.85)
        alto = int(alto_pantalla * 0.85)

        x = (ancho_pantalla - ancho) // 2
        y = (alto_pantalla - alto) // 2

        self.geometry(f"{ancho}x{alto}+{x}+{y}")

        # Tamaño mínimo para evitar que se deforme demasiado
        self.minsize(1100, 700)


        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # =====================================================
        # MENÚ
        # =====================================================

        self.menu = MenuLateral(self)

        self.menu.grid(
            row=0,
            column=0,
            rowspan=3,
            sticky="ns"
        )

        # =====================================================
        # BARRA SUPERIOR
        # =====================================================

        self.barraSuperior = BarraSuperior(self)

        self.barraSuperior.grid(
            row=0,
            column=1,
            sticky="ew"
        )

        # =====================================================
        # CONTENEDOR
        # =====================================================

        self.contenedor = ctk.CTkFrame(
            self,
            fg_color="#EEF2F6"
        )

        self.contenedor.grid(
            row=1,
            column=1,
            sticky="nsew"
        )

        self.contenedor.grid_rowconfigure(0, weight=1)
        self.contenedor.grid_columnconfigure(0, weight=1)

        # =====================================================
        # BARRA DE ESTADO
        # =====================================================

        self.barraEstado = BarraEstado(self)

        self.barraEstado.grid(
            row=2,
            column=1,
            sticky="ew"
        )

        # =====================================================
        # PANTALLAS
        # =====================================================

        self.panelInicio = PanelInicio(self.contenedor)

        self.panelNuevaObservacion = PantallaNuevaObservacion(
            self.contenedor
        )

        self.panelObservaciones = TablaObservaciones(
            self.contenedor
        )

        self.panelDetalle = PantallaDetalleObservacion(
            self.contenedor
        )

        self.panelEspecies = PantallaEspecies(
            self.contenedor
        )

        self.panelUbicaciones = PantallaUbicaciones(
            self.contenedor
        )

        self.panelBusqueda = PantallaBuscar(
            self.contenedor
        )

        self.panelReportes = PantallaReportes(
            self.contenedor
        )

        self.panelEstadisticas = PantallaEstadisticas(
            self.contenedor
        )

        self.panelConfiguracion = PantallaConfiguracion(
            self.contenedor
        )

        self.panelAyuda = PantallaAyuda(
            self.contenedor
        )

        self.panelAcerca = PantallaAcercaDe(
            self.contenedor
        )

        self.pantallas = [

            self.panelInicio,

            self.panelNuevaObservacion,

            self.panelObservaciones,

            self.panelDetalle,

            self.panelEspecies,

            self.panelUbicaciones,

            self.panelBusqueda,

            self.panelReportes,

            self.panelEstadisticas,

            self.panelConfiguracion,

            self.panelAyuda,

            self.panelAcerca

        ]

        for pantalla in self.pantallas:

            pantalla.grid(
                row=0,
                column=0,
                sticky="nsew"
            )

        self.mostrar_inicio()

    # =====================================================

    def ocultar_todo(self):

        for pantalla in self.pantallas:

            pantalla.grid_remove()

    # =====================================================

    def mostrar_inicio(self):

        self.ocultar_todo()

        self.panelInicio.grid()

    # =====================================================

    def mostrar_nueva_observacion(self):

        self.ocultar_todo()

        self.panelNuevaObservacion.grid()

    # =====================================================

    def mostrar_observaciones(self):

        self.ocultar_todo()

        if hasattr(self.panelObservaciones, "actualizar"):

            self.panelObservaciones.actualizar()

        self.panelObservaciones.grid()

    # =====================================================

    def mostrar_detalle_observacion(self, observacion):

        self.ocultar_todo()

        self.panelDetalle.mostrar(observacion)

        self.panelDetalle.grid()

    # =====================================================

    def mostrar_especies(self):

        self.ocultar_todo()

        self.panelEspecies.actualizar()

        self.panelEspecies.grid()

    # =====================================================

    def mostrar_ubicaciones(self):

        self.ocultar_todo()

        self.panelUbicaciones.actualizar()

        self.panelUbicaciones.grid()

    # =====================================================

    def mostrar_busqueda(self):

        self.ocultar_todo()

        self.panelBusqueda.buscar()

        self.panelBusqueda.grid()

    # =====================================================

    def mostrar_reportes(self):

        self.ocultar_todo()

        self.panelReportes.actualizar()

        self.panelReportes.grid()

    # =====================================================

    def mostrar_estadisticas(self):

        self.ocultar_todo()

        self.panelEstadisticas.actualizar()

        self.panelEstadisticas.grid()

    # =====================================================

    def mostrar_configuracion(self):

        self.ocultar_todo()

        self.panelConfiguracion.grid()

    # =====================================================

    def mostrar_ayuda(self):

        self.ocultar_todo()

        self.panelAyuda.grid()

    # =====================================================

    def mostrar_acerca(self):

        self.ocultar_todo()

        self.panelAcerca.grid()