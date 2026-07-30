# servicios/especie_service.py

from dao.especie_dao import EspecieDAO
from modelos.especie import Especie
from servicios.base_service import BaseService


class EspecieService(BaseService):

    dao = EspecieDAO()

    @staticmethod
    def listar():

        return EspecieService.dao.listar()

    @staticmethod
    def buscar(id_especie):

        return EspecieService.dao.obtener(id_especie)

    @staticmethod
    def guardar(especie: Especie):

        if BaseService.es_nuevo(especie):

            return EspecieService.dao.insertar(especie)

        EspecieService.dao.actualizar(especie)

        return especie.id_especie

    @staticmethod
    def eliminar(id_especie):

        EspecieService.dao.eliminar(id_especie)