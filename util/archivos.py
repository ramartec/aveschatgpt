import os
import shutil
from pathlib import Path


class Archivos:

    # =====================================================

    @staticmethod
    def existe(ruta):

        return os.path.exists(ruta)

    # =====================================================

    @staticmethod
    def crear_carpeta(ruta):

        Path(ruta).mkdir(

            parents=True,

            exist_ok=True

        )

    # =====================================================

    @staticmethod
    def copiar(origen, destino):

        Archivos.crear_carpeta(

            os.path.dirname(destino)

        )

        shutil.copy2(

            origen,

            destino

        )

    # =====================================================

    @staticmethod
    def mover(origen, destino):

        Archivos.crear_carpeta(

            os.path.dirname(destino)

        )

        shutil.move(

            origen,

            destino

        )

    # =====================================================

    @staticmethod
    def eliminar(ruta):

        if Archivos.existe(ruta):

            os.remove(ruta)

    # =====================================================

    @staticmethod
    def nombre(ruta):

        return os.path.basename(ruta)

    # =====================================================

    @staticmethod
    def extension(ruta):

        return os.path.splitext(ruta)[1].lower()

    # =====================================================

    @staticmethod
    def tamano(ruta):

        if not Archivos.existe(ruta):

            return 0

        return os.path.getsize(ruta)