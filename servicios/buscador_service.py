from servicios.observacion_service import ObservacionService


class BuscadorService:

    @staticmethod
    def buscar(
        especie="",
        ubicacion="",
        sexo="",
        fecha=None
    ):

        observaciones = ObservacionService.listar()

        resultado = []

        for obs in observaciones:

            # -------------------------
            # especie
            # -------------------------

            if especie:

                nombre = ""

                try:
                    nombre = obs.especie.nombre_comun.lower()
                except:
                    pass

                cientifico = ""

                try:
                    cientifico = obs.especie.nombre_cientifico.lower()
                except:
                    pass

                if especie.lower() not in nombre and especie.lower() not in cientifico:
                    continue

            # -------------------------
            # ubicación
            # -------------------------

            if ubicacion:

                lugar = ""

                try:
                    lugar = obs.ubicacion.nombre.lower()
                except:
                    pass

                if ubicacion.lower() not in lugar:
                    continue

            # -------------------------
            # sexo
            # -------------------------

            if sexo:

                try:

                    if obs.sexo.lower() != sexo.lower():
                        continue

                except:

                    continue

            # -------------------------
            # fecha
            # -------------------------

            if fecha is not None:

                try:

                    if obs.fecha != fecha:
                        continue

                except:

                    continue

            resultado.append(obs)

        return resultado