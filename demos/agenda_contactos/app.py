import web

# Definición de las rutas (URLs)
urls = (
    '/', 'Index',
    '/lista_contactos', 'ListaContactos',
    '/ver_contacto', 'VerContacto',
    '/insertar_contacto', 'InsertarContacto',
    '/editar_contacto', 'EditarContacto',
    '/borrar_contacto', 'BorrarContacto'
)

# Configuración de la aplicación y la carpeta de templates
app = web.application(urls, globals())
render = web.template.render('templates/')

# Clases controladoras para cada pantalla
class Index:
    def GET(self):
        return render.index()

class ListaContactos:
    def GET(self):
        return render.lista_contactos()

class VerContacto:
    def GET(self):
        return render.ver_contacto()

class InsertarContacto:
    def GET(self):
        return render.insertar_contacto()

class EditarContacto:
    def GET(self):
        return render.editar_contacto()

class BorrarContacto:
    def GET(self):
        return render.borrar_contacto()

if __name__ == "__main__":
    app.run()