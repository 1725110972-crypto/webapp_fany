import web

urls = (
    '/', 'Index',
    '/calculadora', 'Calculadora'
)

app = web.application(urls, globals())
render = web.template.render('views')

class Index:
    def GET(self):
        return render.index()

class Calculadora:
    def GET(self):
        return render.calculadora()
    
    def POST(self):
        formulario = web.input()
        #valores usando sus llaves y los conviertes a números al mismo tiempo
        numero_uno = float(formulario.numero_1)
        numero_dos = float(formulario.numero_2)
        
        resultado = numero_uno + numero_dos
        
        # 4. Retornamos el texto original que ya tenías junto con el resultado de la suma
        return f"Formulario: {formulario} | resultado: {resultado}"

if __name__ == "__main__":
    app.run()




    