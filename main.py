import customtkinter as ctk

from presentacion.pantalla_principal import VentanaPrincipal


def configurar_aplicacion():

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")


def main():

    configurar_aplicacion()

    app = VentanaPrincipal()

    def cerrar():

        app.quit()

    app.protocol("WM_DELETE_WINDOW", cerrar)

    app.mainloop()


if __name__ == "__main__":

    main()