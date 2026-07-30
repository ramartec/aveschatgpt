from database.database import Database

from modelos.ubicacion import Ubicacion


class UbicacionDAO:

    def __init__(self):

        self.db = Database()

    # =====================================================

    def listar(self):

        conexion = self.db.conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""

            SELECT *

            FROM ubicaciones

            ORDER BY pais,
                     provincia,
                     canton,
                     distrito,
                     sitio

        """)

        datos = cursor.fetchall()

        cursor.close()

        conexion.close()

        ubicaciones = []

        for fila in datos:

            ubicaciones.append(

                self._crear_objeto(fila)

            )

        return ubicaciones

    # =====================================================

    def obtener(self, id_ubicacion):

        conexion = self.db.conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute(

            """

            SELECT *

            FROM ubicaciones

            WHERE id_ubicacion=%s

            """,

            (id_ubicacion,)

        )

        fila = cursor.fetchone()

        cursor.close()

        conexion.close()

        if fila is None:

            return None

        return self._crear_objeto(fila)
    
        # =====================================================

    def _crear_objeto(self, fila):

        return Ubicacion(

            id_ubicacion=fila["id_ubicacion"],

            sitio=fila["sitio"],

            pais=fila["pais"],

            provincia=fila["provincia"],

            canton=fila["canton"],

            distrito=fila["distrito"],

            latitud=fila["latitud"],

            longitud=fila["longitud"],

            altitud=fila["altitud"],

            habitat=fila["habitat"]

        )

    # =====================================================

    def insertar(self, ubicacion):

        conexion = self.db.conectar()

        cursor = conexion.cursor()

        cursor.execute(

            """

            INSERT INTO ubicaciones(

                sitio,

                pais,

                provincia,

                canton,

                distrito,

                latitud,

                longitud,

                altitud,

                habitat

            )

            VALUES(

                %s,%s,%s,%s,%s,%s,%s,%s,%s

            )

            """,

            (

                ubicacion.sitio,

                ubicacion.pais,

                ubicacion.provincia,

                ubicacion.canton,

                ubicacion.distrito,

                ubicacion.latitud,

                ubicacion.longitud,

                ubicacion.altitud,

                ubicacion.habitat

            )

        )

        conexion.commit()

        id_ubicacion = cursor.lastrowid

        cursor.close()

        conexion.close()

        return id_ubicacion
    
        # =====================================================

    def actualizar(self, ubicacion):

        conexion = self.db.conectar()

        cursor = conexion.cursor()

        cursor.execute(

            """

            UPDATE ubicaciones

            SET

                sitio=%s,

                pais=%s,

                provincia=%s,

                canton=%s,

                distrito=%s,

                latitud=%s,

                longitud=%s,

                altitud=%s,

                habitat=%s

            WHERE id_ubicacion=%s

            """,

            (

                ubicacion.sitio,

                ubicacion.pais,

                ubicacion.provincia,

                ubicacion.canton,

                ubicacion.distrito,

                ubicacion.latitud,

                ubicacion.longitud,

                ubicacion.altitud,

                ubicacion.habitat,

                ubicacion.id_ubicacion

            )

        )

        conexion.commit()

        cursor.close()

        conexion.close()
    
        # =====================================================

    def eliminar(self, id_ubicacion):

        conexion = self.db.conectar()

        cursor = conexion.cursor()

        cursor.execute(

            """

            DELETE FROM ubicaciones

            WHERE id_ubicacion=%s

            """,

            (id_ubicacion,)

        )

        conexion.commit()

        cursor.close()

        conexion.close()

    # =====================================================

    def buscar(self, texto):

        texto = texto.lower()

        return [

            ubicacion

            for ubicacion in self.listar()

            if texto in ubicacion.sitio.lower()

            or texto in ubicacion.distrito.lower()

            or texto in ubicacion.canton.lower()

            or texto in ubicacion.provincia.lower()

            or texto in ubicacion.pais.lower()

        ]