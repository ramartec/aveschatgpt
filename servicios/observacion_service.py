# servicios/observacion_service.py

from dao.observacion_dao import ObservacionDAO
from modelos.observacion import Observacion
from servicios.base_service import BaseService


class ObservacionService(BaseService):

    dao = ObservacionDAO()

    @staticmethod
    def listar():

        return ObservacionService.dao.listar()

    @staticmethod
    def buscar(id_observacion):

        return ObservacionService.dao.obtener(id_observacion)

    @staticmethod
    def guardar(observacion: Observacion):

        if BaseService.es_nuevo(observacion):

            return ObservacionService.dao.insertar(observacion)

        ObservacionService.dao.actualizar(observacion)

        return observacion.id_observacion

    @staticmethod
    def eliminar(id_observacion):

        ObservacionService.dao.eliminar(id_observacion)