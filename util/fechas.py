from datetime import datetime


class Fechas:

    # =====================================================

    @staticmethod
    def ahora():

        return datetime.now()

    # =====================================================

    @staticmethod
    def hoy():

        return datetime.now().date()

    # =====================================================

    @staticmethod
    def fecha_mysql():

        return datetime.now().strftime(

            "%Y-%m-%d"

        )

    # =====================================================

    @staticmethod
    def hora_mysql():

        return datetime.now().strftime(

            "%H:%M:%S"

        )

    # =====================================================

    @staticmethod
    def fecha_hora_mysql():

        return datetime.now().strftime(

            "%Y-%m-%d %H:%M:%S"

        )