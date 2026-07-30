class Observacion:

    def __init__(

        self,

        id_observacion=None,

        especie=None,

        ubicacion=None,

        fecha=None,

        hora=None,

        cantidad=1,

        sexo="Indeterminado",

        edad="",

        comportamiento="",

        notas="",

        archivos=None

    ):

        self.id_observacion = id_observacion

        self.especie = especie

        self.ubicacion = ubicacion

        self.fecha = fecha

        self.hora = hora

        self.cantidad = cantidad

        self.sexo = sexo

        self.edad = edad

        self.comportamiento = comportamiento

        self.notas = notas

        self.archivos = archivos if archivos is not None else []

    def __str__(self):

        if self.especie:

            return self.especie.nombre_comun

        return f"Observación {self.id_observacion}"

    @property
    def id_especie(self):

        if self.especie is None:

            return None

        return self.especie.id_especie

    # =====================================================

    @property
    def id_ubicacion(self):

        if self.ubicacion is None:

            return None

        return self.ubicacion.id_ubicacion