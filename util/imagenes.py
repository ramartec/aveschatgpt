import os

import customtkinter as ctk

from PIL import Image


class Imagenes:

    @staticmethod
    def miniatura(

        ruta,

        ancho=220,

        alto=170

    ):

        try:

            if ruta and os.path.exists(ruta):

                imagen = Image.open(ruta)

            else:

                imagen = Image.new(

                    "RGB",

                    (ancho, alto),

                    "#D1D5DB"

                )

            imagen.thumbnail(

                (ancho, alto)

            )

            return ctk.CTkImage(

                light_image=imagen,

                dark_image=imagen,

                size=imagen.size

            )

        except Exception:

            imagen = Image.new(

                "RGB",

                (ancho, alto),

                "#D1D5DB"

            )

            return ctk.CTkImage(

                light_image=imagen,

                dark_image=imagen,

                size=(ancho, alto)

            )

    # =====================================================

    @staticmethod

    def icono(

        ruta,

        tamano=(32, 32)

    ):

        try:

            imagen = Image.open(ruta)

            return ctk.CTkImage(

                light_image=imagen,

                dark_image=imagen,

                size=tamano

            )

        except Exception:

            return None