class Orden:

    def __init__(

        self,

        id_orden=None,

        nombre=""

    ):

        self.id_orden = id_orden

        self.nombre = nombre

    def __str__(self):

        return self.nombre