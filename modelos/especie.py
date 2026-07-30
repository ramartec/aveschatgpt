class Especie:

    def __init__(

        self,

        id_especie=None,

        genero=None,

        nombre_comun="",

        nombre_cientifico="",

        nombre_ingles="",

        estado_conservacion="",

        migratoria=False,

        endemica=False,

        descripcion=""

    ):

        self.id_especie = id_especie

        self.genero = genero

        self.nombre_comun = nombre_comun

        self.nombre_cientifico = nombre_cientifico

        self.nombre_ingles = nombre_ingles

        self.estado_conservacion = estado_conservacion

        self.migratoria = migratoria

        self.endemica = endemica

        self.descripcion = descripcion

    def __str__(self):

        return self.nombre_comun