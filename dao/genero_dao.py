from database.database import Database

from modelos.genero import Genero
from dao.familia_dao import FamiliaDAO


class GeneroDAO:

    def __init__(self):

        self.db = Database()

        self.familiaDAO = FamiliaDAO()

    # =====================================================

    def listar(self):

        conexion = self.db.conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""

            SELECT *

            FROM generos

            ORDER BY nombre

        """)

        datos = cursor.fetchall()

        cursor.close()

        conexion.close()

        generos = []

        for fila in datos:

            generos.append(

                self._crear_objeto(fila)

            )

        return generos

    # =====================================================

    def obtener(self, id_genero):

        conexion = self.db.conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute(

            """

            SELECT *

            FROM generos

            WHERE id_genero=%s

            """,

            (id_genero,)

        )

        fila = cursor.fetchone()

        cursor.close()

        conexion.close()

        if fila is None:

            return None

        return self._crear_objeto(fila)
    
    # =====================================================

    def _crear_objeto(self, fila):

        familia = self.familiaDAO.obtener(

            fila["id_familia"]

        )

        genero = Genero(

            id_genero=fila["id_genero"],

            familia=familia,

            nombre=fila["nombre"]

        )

        return genero

    # =====================================================

    def insertar(self, genero):

        conexion = self.db.conectar()

        cursor = conexion.cursor()

        cursor.execute(

            """

            INSERT INTO generos(

                id_familia,

                nombre

            )

            VALUES(

                %s,%s

            )

            """,

            (

                genero.familia.id_familia,

                genero.nombre

            )

        )

        conexion.commit()

        id_genero = cursor.lastrowid

        cursor.close()

        conexion.close()

        return id_genero
    
        # =====================================================

    def actualizar(self, genero):

        conexion = self.db.conectar()

        cursor = conexion.cursor()

        cursor.execute(

            """

            UPDATE generos

            SET

                id_familia=%s,

                nombre=%s

            WHERE id_genero=%s

            """,

            (

                genero.familia.id_familia,

                genero.nombre,

                genero.id_genero

            )

        )

        conexion.commit()

        cursor.close()

        conexion.close()
    
        # =====================================================

    def eliminar(self, id_genero):

        conexion = self.db.conectar()

        cursor = conexion.cursor()

        cursor.execute(

            """

            DELETE FROM generos

            WHERE id_genero=%s

            """,

            (id_genero,)

        )

        conexion.commit()

        cursor.close()

        conexion.close()

    # =====================================================

    def buscar(self, texto):

        texto = texto.lower()

        return [

            genero

            for genero in self.listar()

            if texto in genero.nombre.lower()

        ]