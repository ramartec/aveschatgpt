class Ubicacion:

    def __init__(

        self,

        id_ubicacion=None,

        sitio="",

        pais="",

        provincia="",

        canton="",

        distrito="",

        latitud=None,

        longitud=None,

        altitud=None,

        habitat=""

    ):

        self.id_ubicacion = id_ubicacion

        self.sitio = sitio

        self.pais = pais

        self.provincia = provincia

        self.canton = canton

        self.distrito = distrito

        self.latitud = latitud

        self.longitud = longitud

        self.altitud = altitud

        self.habitat = habitat

    def __str__(self):

        return self.sitio