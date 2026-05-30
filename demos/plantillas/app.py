import web

# 1. Definición de rutas: la raíz '/' será atendida por la clase 'Index'
urls = (
    '/', 'Index'
)

# 2. Inicialización de la aplicación web
app = web.application(urls, globals())

# 3. Configuración del motor de plantillas apuntando a la carpeta 'templates'
render = web.template.render('templates')

# 4. Clase encargada de manejar las peticiones GET en la raíz
class Index:
    def GET(self):
        # Llama y renderiza el archivo index.html
        return render.index()

# 5. Punto de entrada para arrancar el servidor local
if __name__ == "__main__":
    app.run()