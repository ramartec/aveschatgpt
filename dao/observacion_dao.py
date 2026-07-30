from database.database import Database

from modelos.observacion import Observacion
from dao.especie_dao import EspecieDAO
from dao.ubicacion_dao import UbicacionDAO
from dao.archivo_dao import ArchivoDAO


class ObservacionDAO:

    def __init__(self):

        self.db = Database()

        self.especieDAO = EspecieDAO()

        self.ubicacionDAO = UbicacionDAO()

        self.archivoDAO = ArchivoDAO()

    # =====================================================

    def listar(self):

        conexion = self.db.conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""

            SELECT *

            FROM observaciones

            ORDER BY fecha DESC, hora DESC

        """)

        datos = cursor.fetchall()

        cursor.close()

        conexion.close()

        observaciones = []

        for fila in datos:

            observaciones.append(

                self._crear_objeto(fila)

            )

        return observaciones
    
        # =====================================================

    def obtener(self, id_observacion):

        conexion = self.db.conectar()

        cursor = conexion.cursor(dictionary=True)

        cursor.execute(

            """

            SELECT *

            FROM observaciones

            WHERE id_observacion = %s

            """,

            (id_observacion,)

        )

        fila = cursor.fetchone()

        cursor.close()

        conexion.close()

        if fila is None:

            return None

        return self._crear_objeto(fila)

    # =====================================================

    def _crear_objeto(self, fila):

        especie = self.especieDAO.obtener(

            fila["id_especie"]

        )

        ubicacion = self.ubicacionDAO.obtener(

            fila["id_ubicacion"]

        )

        archivos = self.archivoDAO.listar_por_observacion(

            fila["id_observacion"]

        )
    
        # =====================================================

        observacion = Observacion(

            id_observacion=fila["id_observacion"],

            especie=especie,

            ubicacion=ubicacion,

            fecha=fila["fecha"],

            hora=fila["hora"],

            cantidad=fila["cantidad"],

            sexo=fila["sexo"],

            edad=fila["edad"],

            comportamiento=fila["comportamiento"],

            notas=fila["notas"],

            archivos=archivos

        )

        return observacion
    
        # =====================================================

    def listar_por_especie(self, id_especie):

        return [

            observacion

            for observacion in self.listar()

            if observacion.especie
            and observacion.especie.id_especie == id_especie

        ]

    # =====================================================

    def listar_por_ubicacion(self, id_ubicacion):

        return [

            observacion

            for observacion in self.listar()

            if observacion.ubicacion
            and observacion.ubicacion.id_ubicacion == id_ubicacion

        ]
    
        # =====================================================

    def insertar(self, observacion):

        conexion = self.db.conectar()

        cursor = conexion.cursor()

        cursor.execute(

            """
            INSERT INTO observaciones
            (
                id_especie,
                id_ubicacion,
                fecha,
                hora,
                cantidad,
                sexo,
                edad,
                comportamiento,
                notas
            )
            VALUES
            (%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """,

            (

                observacion.id_especie,

                observacion.id_ubicacion,

                observacion.fecha,

                observacion.hora,

                observacion.cantidad,

                observacion.sexo,

                observacion.edad,

                observacion.comportamiento,

                observacion.notas

            )

        )

        conexion.commit()

        id_observacion = cursor.lastrowid

        cursor.close()

        conexion.close()

        return id_observacion

    # =====================================================

    def actualizar(self, observacion):

        conexion = self.db.conectar()

        cursor = conexion.cursor()

        cursor.execute(

            """
            UPDATE observaciones
            SET
                id_especie=%s,
                id_ubicacion=%s,
                fecha=%s,
                hora=%s,
                cantidad=%s,
                sexo=%s,
                edad=%s,
                comportamiento=%s,
                notas=%s
            WHERE id_observacion=%s
            """,

            (

                observacion.id_especie,

                observacion.id_ubicacion,

                observacion.fecha,

                observacion.hora,

                observacion.cantidad,

                observacion.sexo,

                observacion.edad,

                observacion.comportamiento,

                observacion.notas,

                observacion.id_observacion

            )

        )

        conexion.commit()

        cursor.close()

        conexion.close()

    # =====================================================

    def eliminar(self, id_observacion):

        conexion = self.db.conectar()

        cursor = conexion.cursor()

        cursor.execute(

            """
            DELETE FROM observaciones
            WHERE id_observacion=%s
            """,

            (id_observacion,)

        )

        conexion.commit()

        cursor.close()

        conexion.close()