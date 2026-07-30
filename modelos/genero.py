class Genero:

    def __init__(

        self,

        id_genero=None,

        familia=None,

        nombre=""

    ):

        self.id_genero = id_genero

        self.familia = familia

        self.nombre = nombre

    def __str__(self):

        return self.nombre