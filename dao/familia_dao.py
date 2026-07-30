from database.database import Database

from modelos.familia import Familia
from dao.orden_dao import OrdenDAO


class FamiliaDAO:

    def __init__(self):

        self.db = Database()

        self.ordenDAO = OrdenDAO()

    # =====================================================

    def listar(self):

        conexion = self.db.conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""

            SELECT *

            FROM familias

            ORDER BY nombre

        """)

        datos = cursor.fetchall()

        cursor.close()

        conexion.close()

        familias = []

        for fila in datos:

            familias.append(

                self._crear_objeto(fila)

            )

        return familias

    # =====================================================

    def obtener(self, id_familia):

        conexion = self.db.conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute(

            """

            SELECT *

            FROM familias

            WHERE id_familia=%s

            """,

            (id_familia,)

        )

        fila = cursor.fetchone()

        cursor.close()

        conexion.close()

        if fila is None:

            return None

        return self._crear_objeto(fila)
    
    # =====================================================

    def _crear_objeto(self, fila):

        orden = self.ordenDAO.obtener(

            fila["id_orden"]

        )

        familia = Familia(

            id_familia=fila["id_familia"],

            orden=orden,

            nombre=fila["nombre"]

        )

        return familia

    # =====================================================

    def insertar(self, familia):

        conexion = self.db.conectar()

        cursor = conexion.cursor()

        cursor.execute(

            """

            INSERT INTO familias(

                id_orden,

                nombre

            )

            VALUES(

                %s,%s

            )

            """,

            (

                familia.orden.id_orden,

                familia.nombre

            )

        )

        conexion.commit()

        id_familia = cursor.lastrowid

        cursor.close()

        conexion.close()

        return id_familia
    
        # =====================================================

    def actualizar(self, familia):

        conexion = self.db.conectar()

        cursor = conexion.cursor()

        cursor.execute(

            """

            UPDATE familias

            SET

                id_orden=%s,

                nombre=%s

            WHERE id_familia=%s

            """,

            (

                familia.orden.id_orden,

                familia.nombre,

                familia.id_familia

            )

        )

        conexion.commit()

        cursor.close()

        conexion.close()
    
        # =====================================================

    def eliminar(self, id_familia):

        conexion = self.db.conectar()

        cursor = conexion.cursor()

        cursor.execute(

            """

            DELETE FROM familias

            WHERE id_familia=%s

            """,

            (id_familia,)

        )

        conexion.commit()

        cursor.close()

        conexion.close()

    # =====================================================

    def buscar(self, texto):

        texto = texto.lower()

        return [

            familia

            for familia in self.listar()

            if texto in familia.nombre.lower()

        ]