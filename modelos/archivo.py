class Archivo:

    def __init__(

        self,

        id_archivo=None,

        id_observacion=None,

        tipo="Fotografia",

        archivo="",

        carpeta="",

        extension="",

        tamano=0,

        fecha_archivo=None,

        latitud=None,

        longitud=None,

        gps="",

        duracion=None,

        favorita=False,

        editada=False,

        notas=""

    ):

        self.id_archivo = id_archivo

        self.id_observacion = id_observacion

        self.tipo = tipo

        self.archivo = archivo

        self.carpeta = carpeta

        self.extension = extension

        self.tamano = tamano

        self.fecha_archivo = fecha_archivo

        self.latitud = latitud

        self.longitud = longitud

        self.gps = gps

        self.duracion = duracion

        self.favorita = favorita

        self.editada = editada

        self.notas = notas

    # =====================================================

    @property
    def ruta(self):

        if self.carpeta:

            import os

            return os.path.join(

                self.carpeta,

                self.archivo

            )

        return self.archivo

    # =====================================================

    def __str__(self):

        return self.archivo