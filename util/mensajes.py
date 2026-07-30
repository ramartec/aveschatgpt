import customtkinter as ctk


class Mensajes:

    @staticmethod
    def informacion(titulo, mensaje):

        ventana = ctk.CTkToplevel()

        ventana.withdraw()

        ctk.CTkMessagebox(

            title=titulo,

            message=mensaje,

            icon="info"

        )

    @staticmethod
    def error(titulo, mensaje):

        ventana = ctk.CTkToplevel()

        ventana.withdraw()

        ctk.CTkMessagebox(

            title=titulo,

            message=mensaje,

            icon="cancel"

        )