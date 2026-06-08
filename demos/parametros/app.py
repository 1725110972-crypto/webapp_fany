import web

urls = (
    '/', 'Index',
    '/parametros', 'Parametros'
)
app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
        return render.index()
    

class Parametros:
    def GET(self):
        titulo = "Título desde Python"
        descripcion = """Lorem ipsum dolor sit amet consectetur adipiscing elit fusce quis, cras pellentesque hac nisl in aptent leo dictum curae, euismod posuere vestibulum facilisis ridiculus varius neque nisi. Pellentesque fames laoreet gravida mattis at duis, interdum sodales sagittis aliquet urna dui netus, ultrices augue suscipit metus curae. Massa facilisi morbi non felis bibendum nam ultrices, varius ornare metus duis velit pretium, senectus tellus aenean elementum vulputate habitasse.
                    Feugiat dictum mattis commodo eros mollis posuere, semper urna ante aliquet quisque lectus ullamcorper, neque cubilia mi condimentum mus. Nisl convallis enim velit litora praesent gravida inceptos potenti primis, condimentum fringilla venenatis ac dictumst luctus a maecenas porttitor, cras platea fames vulputate curabitur nisi tincidunt viverra. Nunc per duis sodales nostra orci a placerat, viverra pharetra scelerisque in himenaeos torquent."""
        return render.parametros(titulo,descripcion)

if __name__ == "__main__":
    app.run()