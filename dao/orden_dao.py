from database.database import Database

from modelos.orden import Orden


class OrdenDAO:

    def __init__(self):

        self.db = Database()

    # =====================================================

    def listar(self):

        conexion = self.db.conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""

            SELECT *

            FROM ordenes

            ORDER BY nombre

        """)

        datos = cursor.fetchall()

        cursor.close()

        conexion.close()

        return [self._crear_objeto(fila) for fila in datos]

    # =====================================================

    def obtener(self, id_orden):

        conexion = self.db.conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute(

            """

            SELECT *

            FROM ordenes

            WHERE id_orden=%s

            """,

            (id_orden,)

        )

        fila = cursor.fetchone()

        cursor.close()

        conexion.close()

        if fila is None:

            return None

        return self._crear_objeto(fila)

    # =====================================================

    def _crear_objeto(self, fila):

        return Orden(

            id_orden=fila["id_orden"],

            nombre=fila["nombre"]

        )

    # =====================================================

    def insertar(self, orden):

        conexion = self.db.conectar()

        cursor = conexion.cursor()

        cursor.execute(

            """

            INSERT INTO ordenes(

                nombre

            )

            VALUES(

                %s

            )

            """,

            (

                orden.nombre,

            )

        )

        conexion.commit()

        cursor.close()

        conexion.close()

    # =====================================================

    def actualizar(self, orden):

        conexion = self.db.conectar()

        cursor = conexion.cursor()

        cursor.execute(

            """

            UPDATE ordenes

            SET

                nombre=%s

            WHERE id_orden=%s

            """,

            (

                orden.nombre,

                orden.id_orden

            )

        )

        conexion.commit()

        cursor.close()

        conexion.close()
    # =====================================================

    def eliminar(self, id_orden):

        conexion = self.db.conectar()

        cursor = conexion.cursor()

        cursor.execute(

            """

            DELETE FROM ordenes

            WHERE id_orden=%s

            """,

            (id_orden,)

        )

        conexion.commit()

        cursor.close()

        conexion.close()

    # =====================================================

    def buscar(self, texto):

        texto = texto.lower()

        return [

            orden

            for orden in self.listar()

            if texto in orden.nombre.lower()

        ]