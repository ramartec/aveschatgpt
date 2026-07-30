# servicios/ubicacion_service.py

from dao.ubicacion_dao import UbicacionDAO
from modelos.ubicacion import Ubicacion
from servicios.base_service import BaseService


class UbicacionService(BaseService):

    dao = UbicacionDAO()

    @staticmethod
    def listar():

        return UbicacionService.dao.listar()

    @staticmethod
    def buscar(id_ubicacion):

        return UbicacionService.dao.obtener(id_ubicacion)

    @staticmethod
    def guardar(ubicacion: Ubicacion):

        if BaseService.es_nuevo(ubicacion):

            return UbicacionService.dao.insertar(ubicacion)

        UbicacionService.dao.actualizar(ubicacion)

        return ubicacion.id_ubicacion

    @staticmethod
    def eliminar(id_ubicacion):

        UbicacionService.dao.eliminar(id_ubicacion)