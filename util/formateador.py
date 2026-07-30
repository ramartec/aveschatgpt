from datetime import datetime


class Formateador:

    # =====================================================

    @staticmethod
    def fecha(fecha):

        if fecha is None:

            return ""

        if isinstance(fecha, datetime):

            return fecha.strftime("%d/%m/%Y")

        return str(fecha)

    # =====================================================

    @staticmethod
    def hora(hora):

        if hora is None:

            return ""

        if isinstance(hora, datetime):

            return hora.strftime("%H:%M")

        return str(hora)

    # =====================================================

    @staticmethod
    def fecha_hora(fecha):

        if fecha is None:

            return ""

        if isinstance(fecha, datetime):

            return fecha.strftime("%d/%m/%Y %H:%M")

        return str(fecha)

    # =====================================================

    @staticmethod
    def tamano(bytes_archivo):

        if bytes_archivo is None:

            return ""

        kb = 1024
        mb = kb * 1024
        gb = mb * 1024

        if bytes_archivo >= gb:

            return f"{bytes_archivo/gb:.2f} GB"

        if bytes_archivo >= mb:

            return f"{bytes_archivo/mb:.2f} MB"

        if bytes_archivo >= kb:

            return f"{bytes_archivo/kb:.2f} KB"

        return f"{bytes_archivo} B"

    # =====================================================

    @staticmethod
    def si_no(valor):

        return "Sí" if valor else "No"

    # =====================================================

    @staticmethod
    def coordenada(valor):

        if valor is None:

            return ""

        return f"{valor:.6f}"