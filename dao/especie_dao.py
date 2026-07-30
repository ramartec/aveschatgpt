from database.database import Database

from modelos.especie import Especie
from dao.genero_dao import GeneroDAO


class EspecieDAO:

    def __init__(self):

        self.db = Database()

        self.generoDAO = GeneroDAO()

    # =====================================================

    def listar(self):

        conexion = self.db.conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""

            SELECT *

            FROM especies

            ORDER BY nombre_comun

        """)

        datos = cursor.fetchall()

        cursor.close()

        conexion.close()

        especies = []

        for fila in datos:

            especies.append(

                self._crear_objeto(fila)

            )

        return especies

    # =====================================================

    def obtener(self, id_especie):

        conexion = self.db.conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute(

            """

            SELECT *

            FROM especies

            WHERE id_especie=%s

            """,

            (id_especie,)

        )

        fila = cursor.fetchone()

        cursor.close()

        conexion.close()

        if fila is None:

            return None

        return self._crear_objeto(fila)
    
    # =====================================================

    def _crear_objeto(self, fila):

        genero = self.generoDAO.obtener(

            fila["id_genero"]

        )

        especie = Especie(

            id_especie=fila["id_especie"],

            genero=genero,

            nombre_comun=fila["nombre_comun"],

            nombre_cientifico=fila["nombre_cientifico"],

            nombre_ingles=fila["nombre_ingles"],

            estado_conservacion=fila["estado_conservacion"],

            migratoria=bool(fila["migratoria"]),

            endemica=bool(fila["endemica"]),

            descripcion=fila["descripcion"]

        )

        return especie

    # =====================================================

    def insertar(self, especie):

        conexion = self.db.conectar()

        cursor = conexion.cursor()

        cursor.execute(

            """

            INSERT INTO especies(

                id_genero,

                nombre_comun,

                nombre_cientifico,

                nombre_ingles,

                estado_conservacion,

                migratoria,

                endemica,

                descripcion

            )

            VALUES(

                %s,%s,%s,%s,%s,%s,%s,%s

            )

            """,

            (

                especie.genero.id_genero,

                especie.nombre_comun,

                especie.nombre_cientifico,

                especie.nombre_ingles,

                especie.estado_conservacion,

                especie.migratoria,

                especie.endemica,

                especie.descripcion

            )

        )

        conexion.commit()

        id_especie = cursor.lastrowid

        cursor.close()

        conexion.close()

        return id_especie    
    
    # =====================================================

    def actualizar(self, especie):

        conexion = self.db.conectar()

        cursor = conexion.cursor()

        cursor.execute(

            """

            UPDATE especies

            SET

                id_genero=%s,

                nombre_comun=%s,

                nombre_cientifico=%s,

                nombre_ingles=%s,

                estado_conservacion=%s,

                migratoria=%s,

                endemica=%s,

                descripcion=%s

            WHERE id_especie=%s

            """,

            (

                especie.genero.id_genero,

                especie.nombre_comun,

                especie.nombre_cientifico,

                especie.nombre_ingles,

                especie.estado_conservacion,

                especie.migratoria,

                especie.endemica,

                especie.descripcion,

                especie.id_especie

            )

        )

        conexion.commit()

        cursor.close()

        conexion.close()
    
        # =====================================================

    def eliminar(self, id_especie):

        conexion = self.db.conectar()

        cursor = conexion.cursor()

        cursor.execute(

            """

            DELETE FROM especies

            WHERE id_especie=%s

            """,

            (id_especie,)

        )

        conexion.commit()

        cursor.close()

        conexion.close()

    # =====================================================

    def buscar(self, texto):

        texto = texto.lower()

        return [

            especie

            for especie in self.listar()

            if texto in especie.nombre_comun.lower()

            or texto in especie.nombre_cientifico.lower()

        ]