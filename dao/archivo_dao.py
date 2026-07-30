from database.database import Database

from modelos.archivo import Archivo


class ArchivoDAO:

    def __init__(self):

        self.db = Database()

    # =====================================================

    def listar(self):

        conexion = self.db.conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""

            SELECT *

            FROM archivos

            ORDER BY fecha_archivo DESC

        """)

        datos = cursor.fetchall()

        cursor.close()

        conexion.close()

        return [self._crear_objeto(fila) for fila in datos]

    # =====================================================

    def listar_por_observacion(self, id_observacion):

        conexion = self.db.conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute(

            """

            SELECT *

            FROM archivos

            WHERE id_observacion=%s

            ORDER BY favorita DESC,
                     fecha_archivo

            """,

            (id_observacion,)

        )

        datos = cursor.fetchall()

        cursor.close()

        conexion.close()

        return [self._crear_objeto(fila) for fila in datos]

    # =====================================================

    def obtener(self, id_archivo):

        conexion = self.db.conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute(

            """

            SELECT *

            FROM archivos

            WHERE id_archivo=%s

            """,

            (id_archivo,)

        )

        fila = cursor.fetchone()

        cursor.close()

        conexion.close()

        if fila is None:

            return None

        return self._crear_objeto(fila)

    # =====================================================

    def _crear_objeto(self, fila):

        return Archivo(

            id_archivo=fila["id_archivo"],

            id_observacion=fila["id_observacion"],

            tipo=fila["tipo"],

            archivo=fila["archivo"],

            carpeta=fila["carpeta"],

            extension=fila["extension"],

            tamano=fila["tamano"],

            fecha_archivo=fila["fecha_archivo"],

            latitud=fila["latitud"],

            longitud=fila["longitud"],

            gps=fila["GPS"],

            duracion=fila["duracion"],

            favorita=bool(fila["favorita"]),

            editada=bool(fila["editada"]),

            notas=fila["notas"]

        )

    # =====================================================

    def insertar(self, archivo):

        conexion = self.db.conectar()

        cursor = conexion.cursor()

        cursor.execute(

            """

            INSERT INTO archivos(

                id_observacion,

                tipo,

                archivo,

                carpeta,

                extension,

                tamano,

                fecha_archivo,

                latitud,

                longitud,

                GPS,

                duracion,

                favorita,

                editada,

                notas

            )

            VALUES(

                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s

            )

            """,

            (

                archivo.id_observacion,

                archivo.tipo,

                archivo.archivo,

                archivo.carpeta,

                archivo.extension,

                archivo.tamano,

                archivo.fecha_archivo,

                archivo.latitud,

                archivo.longitud,

                archivo.gps,

                archivo.duracion,

                archivo.favorita,

                archivo.editada,

                archivo.notas

            )

        )

        conexion.commit()

        cursor.close()

        conexion.close()

    # =====================================================

    def actualizar(self, archivo):

        conexion = self.db.conectar()

        cursor = conexion.cursor()

        cursor.execute(

            """

            UPDATE archivos

            SET

                tipo=%s,

                archivo=%s,

                carpeta=%s,

                extension=%s,

                tamano=%s,

                fecha_archivo=%s,

                latitud=%s,

                longitud=%s,

                GPS=%s,

                duracion=%s,

                favorita=%s,

                editada=%s,

                notas=%s

            WHERE id_archivo=%s

            """,

            (

                archivo.tipo,

                archivo.archivo,

                archivo.carpeta,

                archivo.extension,

                archivo.tamano,

                archivo.fecha_archivo,

                archivo.latitud,

                archivo.longitud,

                archivo.gps,

                archivo.duracion,

                archivo.favorita,

                archivo.editada,

                archivo.notas,

                archivo.id_archivo

            )

        )

        conexion.commit()

        cursor.close()

        conexion.close()

    # =====================================================

    def eliminar(self, id_archivo):

        conexion = self.db.conectar()

        cursor = conexion.cursor()

        cursor.execute(

            """

            DELETE FROM archivos

            WHERE id_archivo=%s

            """,

            (id_archivo,)

        )

        conexion.commit()

        cursor.close()

        conexion.close()