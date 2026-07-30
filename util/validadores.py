from datetime import datetime


class Validadores:

    # =====================================================

    @staticmethod
    def texto_requerido(texto):

        return texto is not None and texto.strip() != ""

    # =====================================================

    @staticmethod
    def entero(valor):

        try:

            int(valor)

            return True

        except:

            return False

    # =====================================================

    @staticmethod
    def decimal(valor):

        try:

            float(valor)

            return True

        except:

            return False

    # =====================================================

    @staticmethod
    def fecha(valor):

        try:

            datetime.strptime(valor, "%d/%m/%Y")

            return True

        except:

            return False

    # =====================================================

    @staticmethod
    def longitud(valor):

        if valor is None:

            return False

        return -180 <= valor <= 180

    # =====================================================

    @staticmethod
    def latitud(valor):

        if valor is None:

            return False

        return -90 <= valor <= 90

    # =====================================================

    @staticmethod
    def porcentaje(valor):

        if valor is None:

            return False

        return 0 <= valor <= 100

    # =====================================================

    @staticmethod
    def archivo(ruta):

        if ruta is None:

            return False

        return ruta.strip() != ""