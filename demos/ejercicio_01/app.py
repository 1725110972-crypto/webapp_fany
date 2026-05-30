import web

# Definición de rutas: vincula una URL con su respectiva clase encargada de responder
urls = (
    '/', 'Index',
    '/clientes', 'Clientes',
    '/usuarios', 'Usuarios'
)

# Inicializa la aplicación web
app = web.application(urls, globals())

# Configura el motor para buscar los archivos HTML dentro de la carpeta 'templates'
render = web.template.render('templates')

# Clase para la página de inicio (/)
class Index:
    def GET(self):
        return render.index()

# Clase para la página de clientes (/clientes)
class Clientes:
    def GET(self):
        return render.clientes()

# Clase para la página de usuarios (/usuarios)
class Usuarios:
    def GET(self):
        return render.usuarios()

# Arranca el servidor local
if __name__ == "__main__":
    app.run()