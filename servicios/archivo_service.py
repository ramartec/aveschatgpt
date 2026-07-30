# servicios/archivo_service.py

from dao.archivo_dao import ArchivoDAO
from modelos.archivo import Archivo
from servicios.base_service import BaseService


class ArchivoService(BaseService):

    dao = ArchivoDAO()

    @staticmethod
    def listar():

        return ArchivoService.dao.listar()

    @staticmethod
    def listar_por_observacion(id_observacion):

        return ArchivoService.dao.listar_por_observacion(id_observacion)

    @staticmethod
    def buscar(id_archivo):

        return ArchivoService.dao.obtener(id_archivo)

    @staticmethod
    def guardar(archivo: Archivo):

        if BaseService.es_nuevo(archivo):

            return ArchivoService.dao.insertar(archivo)

        ArchivoService.dao.actualizar(archivo)

        return archivo.id_archivo

    @staticmethod
    def eliminar(id_archivo):

        ArchivoService.dao.eliminar(id_archivo)