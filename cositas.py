# from rich.console import Console
# from rich.panel import Panel
# from rich.align import Align

# consola = Console()

# # Tu arte ASCII (el estilo Arch Linux)
# ascii_art = """
#        /\\
#       /  \\
#      /    \\
#     /      \\
#    /   ,,   \\
#   /   |  |   \\
#  /_-''    ''-_\\
# """

# # Tu menú de opciones
# opciones = """
# [1] Actualizar sistema
# [2] Configurar red
# [3] Entrar a la Matrix
# [4] Salir
# """

# # Armamos el cuadro (Panel)
# panel_menu = Panel(
#     Align.center(opciones), 
#     title="[bold cyan]⚡ PANEL DE CONTROL ⚡[/bold cyan]", 
#     border_style="green",
#     padding=(1, 2)
# )

# consola.print(f"[bold blue]{ascii_art}[/bold blue]")
# consola.print(panel_menu)


# import questionary

# # Esto te frena la terminal y te deja elegir con las flechas
# respuesta = questionary.select(
#     "¿Qué querés hacer, brother?",
#     choices=[
#         "🚀 Iniciar servidor",
#         "📂 Ver base de datos",
#         "⚙️ Configuraciones",
#         "❌ Salir"
#     ],
#     # Este es el puntero que querías
#     pointer="=>" 
# ).ask()

# print(f"Elegiste: {respuesta}")

# from textual.app import App, ComposeResult
# from textual.widgets import Header, Footer, Static, Button
# from textual.containers import Container, Vertical

# class MiDashboard(App):
#     # Título que aparece en la parte de arriba
#     TITLE = "Terminal Admin Center"
    
#     # Acá le damos estilo a los marcos usando algo casi idéntico a CSS web
#     CSS = """
#     Screen {
#         layout: grid;
#         grid-size: 2;
#         grid-columns: 1fr 3fr; /* La barra lateral ocupa 1 parte, el main 3 partes */
#     }

#     #barra-lateral {
#         border: solid cyan; /* Marco azul brillante */
#         height: 100%;
#         padding: 1;
#     }

#     #area-principal {
#         height: 100%;
#         padding: 1;
#     }

#     .caja-info {
#         border: round green; /* Marco verde con bordes redondeados */
#         height: 1fr;
#         padding: 1;
#         margin-bottom: 1;
#     }

#     Button {
#         width: 100%;
#         margin-bottom: 1;
#     }
#     """

#     def compose(self) -> ComposeResult:
#         # Header (arriba) y Footer (abajo para atajos)
#         yield Header()
        
#         # Barra lateral izquierda con los botones
#         with Container(id="barra-lateral"):
#             yield Static("[b]⚡ MÓDULOS[/b]\n")
#             yield Button("🖥️ Ubuntu Server", id="btn_server", variant="primary")
#             yield Button("🗄️ Samba NAS", id="btn_nas", variant="warning")
#             yield Button("🖨️ Klipper 3D", id="btn_klipper", variant="success")
#             yield Button("❌ Salir", id="btn_salir", variant="error")

#         # Área principal a la derecha con los paneles
#         with Vertical(id="area-principal"):
#             yield Static(
#                 "[b]ESTADO DEL SERVIDOR:[/b] Óptimo\n"
#                 "[b]CARGA CPU:[/b] 12%\n"
#                 "[b]CONEXIONES ACTIVAS:[/b] 4", 
#                 classes="caja-info"
#             )
#             yield Static(
#                 "[b]ESTADO IMPRESORA 3D:[/b] En espera\n"
#                 "[b]TEMP CAMA:[/b] 22°C\n"
#                 "[b]TEMP NOZZLE:[/b] 21°C", 
#                 classes="caja-info"
#             )

#         yield Footer()

#     # Esto captura los clics del mouse o el Enter sobre los botones
#     def on_button_pressed(self, event: Button.Pressed) -> None:
#         if event.button.id == "btn_salir":
#             self.exit()
#         else:
#             # Tira una notificación flotante estilo Windows abajo a la derecha
#             self.notify(f"Solicitud enviada al módulo: {event.button.id}")

# if __name__ == "__main__":
#     app = MiDashboard()
#     app.run()





# from textual.app import App, ComposeResult
# from textual.widgets import Static

# # Usamos los emojis para que sea súper limpio y compacto
# FRAMES_MUNDO = ["🌍", "🌎", "🌏"]

# class MiApp(App):
#     CSS = """
#     Screen {
#         /* 1. Creamos las capas: el fondo y el frente */
#         layers: fondo frente; 
#         background: black;
#     }

#     #panel-principal {
#         /* 2. Mandamos la interfaz a la capa del fondo */
#         layer: fondo;         
#         height: 100%;
#         border: solid green;
#         padding: 1;
#         color: lime;
#     }

#     #esquinita-animada {
#         /* 3. Mandamos la animación a la capa del frente (flota) */
#         layer: frente;        
        
#         /* 4. Lo anclamos al piso de la terminal */
#         dock: bottom;         
        
#         height: 1;            
        
#         /* 5. Lo despegamos 1 renglón desde abajo */
#         margin-bottom: 1;     
        
#         /* 6. Alinear el emoji completamente a la derecha */
#         content-align: right middle; 
        
#         /* 7. Lo despegamos 2 espacios desde la derecha */
#         padding-right: 2;     
        
#         background: transparent;
#     }
#     """

#     def __init__(self):
#         super().__init__()
#         self.frame_actual = 0

#     def compose(self) -> ComposeResult:
#         yield Static(
#             "⚡ INICIANDO INTERFAZ...\n"
#             "   Cargando módulos...\n"
#             "   Todo listo.", 
#             id="panel-principal"
#         )
#         yield Static(FRAMES_MUNDO[0], id="esquinita-animada")

#     def on_mount(self) -> None:
#         self.set_interval(0.5, self.avanzar_frame)

#     def avanzar_frame(self) -> None:
#         self.frame_actual = (self.frame_actual + 1) % len(FRAMES_MUNDO)
#         caja_animacion = self.query_one("#esquinita-animada", Static)
#         caja_animacion.update(FRAMES_MUNDO[self.frame_actual])

# if __name__ == "__main__":
#     app = MiApp()
#     app.run()