class Familia:

    def __init__(

        self,

        id_familia=None,

        orden=None,

        nombre=""

    ):

        self.id_familia = id_familia

        self.orden = orden

        self.nombre = nombre

    def __str__(self):

        return self.nombre