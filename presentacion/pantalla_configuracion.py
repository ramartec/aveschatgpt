import customtkinter as ctk


class PantallaConfiguracion(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(
            master,
            fg_color="#EEF2F6"
        )

        self.master = master

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # =====================================================
        # CABECERA
        # =====================================================

        cabecera = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        cabecera.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=20,
            pady=(20, 10)
        )

        ctk.CTkLabel(

            cabecera,

            text="Configuración",

            font=("Segoe UI", 28, "bold")

        ).pack(

            anchor="w"

        )

        # =====================================================
        # PANEL
        # =====================================================

        panel = ctk.CTkScrollableFrame(

            self,

            fg_color="white",

            corner_radius=12

        )

        panel.grid(

            row=1,

            column=0,

            sticky="nsew",

            padx=20,

            pady=(0,20)

        )

        # =====================================================
        # GENERAL
        # =====================================================

        ctk.CTkLabel(

            panel,

            text="General",

            font=("Segoe UI",20,"bold")

        ).pack(

            anchor="w",

            padx=20,

            pady=(20,10)

        )

        self.chkMiniaturas = ctk.CTkCheckBox(

            panel,

            text="Mostrar miniaturas"

        )

        self.chkMiniaturas.pack(

            anchor="w",

            padx=25,

            pady=5

        )

        self.chkAnimaciones = ctk.CTkCheckBox(

            panel,

            text="Activar animaciones"

        )

        self.chkAnimaciones.pack(

            anchor="w",

            padx=25,

            pady=5

        )

        self.chkRecordar = ctk.CTkCheckBox(

            panel,

            text="Recordar ventana al iniciar"

        )

        self.chkRecordar.pack(

            anchor="w",

            padx=25,

            pady=5

        )

        # =====================================================
        # APARIENCIA
        # =====================================================

        ctk.CTkLabel(

            panel,

            text="Apariencia",

            font=("Segoe UI",20,"bold")

        ).pack(

            anchor="w",

            padx=20,

            pady=(30,10)

        )

        self.cmbTema = ctk.CTkComboBox(

            panel,

            values=[

                "Claro",

                "Oscuro",

                "Sistema"

            ]

        )

        self.cmbTema.pack(

            fill="x",

            padx=25

        )
    
    # =====================================================
    # BASE DE DATOS
    # =====================================================

        ctk.CTkLabel(

            panel,

            text="Base de datos",

            font=("Segoe UI", 20, "bold")

        ).pack(

            anchor="w",

            padx=20,

            pady=(30, 10)

        )

        self.lblEstado = ctk.CTkLabel(

            panel,

            text="Estado: Conectado",

            anchor="w"

        )

        self.lblEstado.pack(

            anchor="w",

            padx=25,

            pady=5

        )

        self.btnProbar = ctk.CTkButton(

            panel,

            text="Probar conexión",

            command=self.probar_conexion

        )

        self.btnProbar.pack(

            anchor="w",

            padx=25,

            pady=10

        )

        # =====================================================
        # BOTONES
        # =====================================================

        botones = ctk.CTkFrame(

            panel,

            fg_color="transparent"

        )

        botones.pack(

            fill="x",

            padx=20,

            pady=30

        )

        ctk.CTkButton(

            botones,

            text="Guardar",

            width=150,

            command=self.guardar

        ).pack(

            side="left"

        )

        ctk.CTkButton(

            botones,

            text="Restablecer",

            width=150,

            fg_color="#6B7280",

            hover_color="#4B5563",

            command=self.restablecer

        ).pack(

            side="left",

            padx=10

        )

    # =====================================================
    # PROBAR CONEXION
    # =====================================================

    def probar_conexion(self):

        try:

            self.lblEstado.configure(

                text="Estado: Conectado",

                text_color="#16A34A"

            )

        except Exception:

            self.lblEstado.configure(

                text="Estado: Desconectado",

                text_color="red"

            )

    # =====================================================
    # GUARDAR
    # =====================================================

    def guardar(self):

        print("Configuración guardada.")

    # =====================================================
    # RESTABLECER
    # =====================================================

    def restablecer(self):

        self.chkMiniaturas.select()

        self.chkAnimaciones.select()

        self.chkRecordar.select()

        self.cmbTema.set("Sistema")

        print("Configuración restablecida.")