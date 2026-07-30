import customtkinter as ctk

from util.imagenes import Imagenes


class DetalleObservacion(ctk.CTkScrollableFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="white",
            corner_radius=12
        )

        self.grid_columnconfigure(1, weight=1)

        self.imagen = ctk.CTkLabel(
            self,
            text="",
            width=320,
            height=320
        )

        self.imagen.grid(
            row=0,
            column=0,
            rowspan=10,
            padx=20,
            pady=20,
            sticky="n"
        )

        self.lblComun = self.crear_fila(
            0,
            "Nombre común"
        )

        self.lblCientifico = self.crear_fila(
            1,
            "Nombre científico"
        )

        self.lblLugar = self.crear_fila(
            2,
            "Ubicación"
        )

        self.lblFecha = self.crear_fila(
            3,
            "Fecha"
        )

        self.lblSexo = self.crear_fila(
            4,
            "Sexo"
        )

        self.lblEdad = self.crear_fila(
            5,
            "Edad"
        )

        self.lblComportamiento = self.crear_fila(
            6,
            "Comportamiento"
        )

        self.lblCantidad = self.crear_fila(
            7,
            "Cantidad"
        )

        self.lblArchivos = self.crear_fila(
            8,
            "Archivos"
        )

        self.txtNotas = ctk.CTkTextbox(
            self,
            height=180
        )

        self.txtNotas.grid(
            row=9,
            column=1,
            sticky="nsew",
            padx=(10,20),
            pady=(10,20)
        )

    # =====================================================

    def crear_fila(self, fila, titulo):

        ctk.CTkLabel(

            self,

            text=titulo + ":",

            font=("Segoe UI",15,"bold")

        ).grid(

            row=fila,

            column=1,

            sticky="w",

            padx=(10,20),

            pady=(10,0)

        )

        valor = ctk.CTkLabel(

            self,

            text="",

            anchor="w",

            justify="left",

            font=("Segoe UI",14)

        )

        valor.grid(

            row=fila,

            column=1,

            sticky="w",

            padx=(170,20),

            pady=(10,0)

        )

        return valor
    
        # =====================================================

    def cargar(self, observacion):

        ruta = None
        cantidad = 0

        if getattr(observacion, "archivos", None):

            cantidad = len(observacion.archivos)

            for archivo in observacion.archivos:

                if getattr(archivo, "tipo", "") == "Fotografia":

                    ruta = getattr(archivo, "ruta", None)

                    break

        try:

            imagen = Imagenes.miniatura(ruta)

            self.imagen.configure(
                image=imagen,
                text=""
            )

            self.imagen.image = imagen

        except Exception:

            self.imagen.configure(
                image=None,
                text="Sin fotografía"
            )

            self.imagen.image = None

        especie = getattr(observacion, "especie", None)

        if especie:

            self.lblComun.configure(
                text=especie.nombre_comun or ""
            )

            self.lblCientifico.configure(
                text=especie.nombre_cientifico or ""
            )

        else:

            self.lblComun.configure(text="")
            self.lblCientifico.configure(text="")

        ubicacion = getattr(observacion, "ubicacion", None)

        if ubicacion:

            self.lblLugar.configure(
                text=ubicacion.sitio or ""
            )

        else:

            self.lblLugar.configure(text="")

        self.lblFecha.configure(
            text=str(getattr(observacion, "fecha", "") or "")
        )

        self.lblSexo.configure(
            text=getattr(observacion, "sexo", "") or ""
        )

        self.lblEdad.configure(
            text=getattr(observacion, "edad", "") or ""
        )

        self.lblComportamiento.configure(
            text=getattr(observacion, "comportamiento", "") or ""
        )

        self.lblCantidad.configure(
            text=str(getattr(observacion, "cantidad", 0))
        )

        self.lblArchivos.configure(
            text=f"{cantidad} archivo(s)"
        )

        self.txtNotas.delete(
            "1.0",
            "end"
        )

        self.txtNotas.insert(
            "1.0",
            getattr(observacion, "notas", "") or ""
        )