#pantalla_nueva_observacion.py

import customtkinter as ctk
from tkinter import filedialog
from datetime import datetime
import os

from modelos.observacion import Observacion
from modelos.archivo import Archivo

from servicios.observacion_service import ObservacionService
from servicios.especie_service import EspecieService
from servicios.ubicacion_service import UbicacionService
from servicios.archivo_service import ArchivoService

from util.imagenes import Imagenes
from util.validadores import Validadores

from presentacion.pantalla_base import PantallaBase


class PantallaNuevaObservacion(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="#EEF2F6"
        )

        self.master = master

        self.archivos = []

        self.especies = []

        self.ubicaciones = []

        self.grid_columnconfigure(0, weight=3)

        self.grid_columnconfigure(1, weight=2)

        self.grid_rowconfigure(1, weight=1)

        self.crear_cabecera()

        self.crear_panel_izquierdo()

        self.crear_panel_derecho()

        self.cargar_especies()

        self.cargar_ubicaciones()

    # =====================================================

    def crear_cabecera(self):

        cabecera = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        cabecera.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=25,
            pady=(20, 15)
        )

        cabecera.grid_columnconfigure(0, weight=1)

        self.lblTitulo = ctk.CTkLabel(
            cabecera,
            text="Nueva observación",
            font=("Segoe UI", 30, "bold")
        )

        self.lblTitulo.grid(
            row=0,
            column=0,
            sticky="w"
        )

        self.btnGuardar = ctk.CTkButton(
            cabecera,
            text="💾 Guardar",
            width=150,
            fg_color="#16A34A",
            hover_color="#15803D",
            command=self.guardar
        )

        self.btnGuardar.grid(
            row=0,
            column=1,
            padx=5
        )

        self.btnCancelar = ctk.CTkButton(
            cabecera,
            text="Cancelar",
            width=120,
            fg_color="#9CA3AF",
            command=self.master.master.mostrar_inicio
        )

        self.btnCancelar.grid(
            row=0,
            column=2
        )

    # =====================================================

    def crear_panel_izquierdo(self):

        izquierda = ctk.CTkScrollableFrame(
            self,
            fg_color="white",
            corner_radius=12
        )

        izquierda.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=(20, 10),
            pady=(0, 20)
        )

        ctk.CTkLabel(
            izquierda,
            text="Especie",
            font=("Segoe UI", 16, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 5)
        )

        self.cmbEspecie = ctk.CTkComboBox(
            izquierda,
            values=[]
        )

        self.cmbEspecie.pack(
            fill="x",
            padx=20
        )

        ctk.CTkLabel(
            izquierda,
            text="Ubicación",
            font=("Segoe UI", 16, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 5)
        )

        self.cmbUbicacion = ctk.CTkComboBox(
            izquierda,
            values=[]
        )

        self.cmbUbicacion.pack(
            fill="x",
            padx=20
        )

        self.txtFecha = self.crear_fila_entry(
            izquierda,
            "Fecha",
            datetime.now().strftime("%d/%m/%Y")
        )

        self.txtHora = self.crear_fila_entry(
            izquierda,
            "Hora",
            datetime.now().strftime("%H:%M")
        )

        fila = ctk.CTkFrame(
            izquierda,
            fg_color="transparent"
        )

        fila.pack(
            fill="x",
            padx=20,
            pady=(15, 0)
        )

        ctk.CTkLabel(
            fila,
            text="Sexo",
            width=120,
            anchor="w"
        ).pack(side="left")

        self.cmbSexo = ctk.CTkComboBox(
            fila,
            values=[
                "",
                "Macho",
                "Hembra",
                "Indeterminado"
            ]
        )

        self.cmbSexo.set("Indeterminado")

        self.cmbSexo.pack(
            side="left",
            fill="x",
            expand=True
        )

        self.txtCantidad = self.crear_fila_entry(
            izquierda,
            "Cantidad",
            "1"
        )

        ctk.CTkLabel(
            izquierda,
            text="Notas",
            font=("Segoe UI", 16, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 5)
        )

        self.txtNotas = ctk.CTkTextbox(
            izquierda,
            height=180
        )

        self.txtNotas.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

    # =====================================================

    def crear_panel_derecho(self):

        derecha = ctk.CTkFrame(
            self,
            fg_color="white",
            corner_radius=12
        )

        derecha.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=(10, 20),
            pady=(0, 20)
        )

        self.lblImagen = ctk.CTkLabel(
            derecha,
            text="Sin fotografía",
            width=420,
            height=320,
            fg_color="#F3F4F6",
            corner_radius=12
        )

        self.lblImagen.pack(
            padx=20,
            pady=(20, 15)
        )

        self.btnAgregar = ctk.CTkButton(
            derecha,
            text="📷 Agregar fotografías / videos / audios",
            command=self.agregar_archivos
        )

        self.btnAgregar.pack(
            fill="x",
            padx=20
        )

        self.lblCantidadArchivos = ctk.CTkLabel(
            derecha,
            text="0 archivos seleccionados"
        )

        self.lblCantidadArchivos.pack(
            pady=(12, 8)
        )

        self.galeria = ctk.CTkScrollableFrame(
            derecha,
            orientation="horizontal",
            height=110,
            fg_color="transparent"
        )

        self.galeria.pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

    # =====================================================

    def crear_fila_entry(self, parent, texto, valor):

        fila = ctk.CTkFrame(
            parent,
            fg_color="transparent"
        )

        fila.pack(
            fill="x",
            padx=20,
            pady=(15, 0)
        )

        ctk.CTkLabel(
            fila,
            text=texto,
            width=120,
            anchor="w"
        ).pack(side="left")

        entry = ctk.CTkEntry(fila)

        entry.pack(
            side="left",
            fill="x",
            expand=True
        )

        entry.insert(0, valor)

        return entry

    # =====================================================

    def cargar_especies(self):

        try:

            self.especies = EspecieService.listar()

            nombres = [
                especie.nombre_comun
                for especie in self.especies
            ]

            self.cmbEspecie.configure(
                values=nombres
            )

            if nombres:
                self.cmbEspecie.set(nombres[0])

        except Exception as e:

            print(e)

            self.especies = []

    # =====================================================

    def cargar_ubicaciones(self):

        try:

            self.ubicaciones = UbicacionService.listar()

            nombres = [
                ubicacion.sitio
                for ubicacion in self.ubicaciones
            ]

            self.cmbUbicacion.configure(
                values=nombres
            )

            if nombres:
                self.cmbUbicacion.set(nombres[0])

        except Exception as e:

            print(e)

            self.ubicaciones = []

    # =====================================================

    def agregar_archivos(self):

        rutas = filedialog.askopenfilenames(

            title="Seleccionar archivos",

            filetypes=[(
                "Archivos",
                "*.jpg *.jpeg *.png *.bmp *.gif *.mp4 *.avi *.mov *.mp3 *.wav"
            )]

        )

        if not rutas:
            return

        self.archivos.extend(rutas)

        self.actualizar_galeria()

    # =====================================================

    def actualizar_galeria(self):

        for widget in self.galeria.winfo_children():

            widget.destroy()

        self.lblCantidadArchivos.configure(

            text=f"{len(self.archivos)} archivos seleccionados"

        )

        if len(self.archivos) == 0:

            self.lblImagen.configure(
                image=None,
                text="Sin fotografía"
            )

            return

        try:

            imagen = Imagenes.grande(
                self.archivos[0]
            )

            self.lblImagen.configure(
                image=imagen,
                text=""
            )

            self.lblImagen.image = imagen

        except Exception:

            pass

        for ruta in self.archivos:

            try:

                mini = Imagenes.galeria(ruta)

                lbl = ctk.CTkLabel(
                    self.galeria,
                    image=mini,
                    text=""
                )

                lbl.image = mini

                lbl.pack(
                    side="left",
                    padx=5,
                    pady=5
                )

            except Exception:

                pass

    # =====================================================

    def guardar(self):

        try:

            if not Validadores.texto_requerido(
                self.cmbEspecie.get()
            ):
                print("Debe seleccionar una especie.")
                return

            if not Validadores.texto_requerido(
                self.cmbUbicacion.get()
            ):
                print("Debe seleccionar una ubicación.")
                return

            observacion = Observacion()

            observacion.fecha = self.txtFecha.get()
            observacion.hora = self.txtHora.get()
            observacion.sexo = self.cmbSexo.get()
            observacion.cantidad = int(self.txtCantidad.get())
            observacion.notas = self.txtNotas.get(
                "1.0",
                "end"
            ).strip()

            observacion.edad = ""
            observacion.comportamiento = ""

            for especie in self.especies:

                if especie.nombre_comun == self.cmbEspecie.get():

                    observacion.especie = especie
                    break

            for ubicacion in self.ubicaciones:

                if ubicacion.sitio == self.cmbUbicacion.get():

                    observacion.ubicacion = ubicacion
                    break

            id_observacion = ObservacionService.guardar(
                observacion
            )

            for indice, ruta in enumerate(self.archivos):

                archivo = Archivo()

                archivo.id_observacion = id_observacion
                archivo.tipo = "Fotografia"
                archivo.archivo = ruta
                archivo.carpeta = ""
                archivo.extension = ruta.split(".")[-1].lower()
                archivo.tamano = 0
                archivo.fecha_archivo = datetime.now()
                archivo.latitud = None
                archivo.longitud = None
                archivo.gps = ""
                archivo.duracion = None
                archivo.favorita = (indice == 0)
                archivo.editada = False
                archivo.notas = ""

                ArchivoService.guardar(
                    archivo
                )

            self.master.master.mostrar_inicio()

        except Exception as e:

            print(e)