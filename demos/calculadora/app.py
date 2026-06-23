import web

urls = (
    '/', 'Index',
    '/calculadora', 'Calculadora'
)
app = web.application(urls, globals())
render = web.template.render('views')

class Index:
    def GET(self):
        return render.index
    

class Calculadora:
    def GET(self):
        numero_1=0.0
        numero_2=0.0
        resultado=0.0
        return render.calculadora(numero_1,numero_2, resultado)
    
    def POST(self):
        formulario = web.input()
        
        # 1. Directo y sin enredos, tal como lo tenías tú
        numero_1 = float(formulario['numero_1'])
        numero_2 = float(formulario['numero_2'])   

        # 2. Atrapamos el valor del botón
        operacion = formulario['operacion']
        resultado = 0.0

        # 3. Solo los IF anidados para las operaciones
        if operacion == "sumar":
            resultado = numero_1 + numero_2
            
        elif operacion == "restar":
            resultado = numero_1 - numero_2
            
        elif operacion == "multiplicar":
            resultado = numero_1 * numero_2
            
        elif operacion == "dividir":
            resultado = numero_1 / numero_2
                
        elif operacion == "modulo":
            resultado = numero_1 % numero_2
            
        elif operacion == "potencia":
            resultado = numero_1 ** numero_2
            
        elif operacion == "raiz":
            resultado = numero_1 ** 0.5 
            
        elif operacion == "limpiar":
            numero_1 = 0.0
            numero_2 = 0.0
            resultado = 0.0

        print (f"Tipo de dato de numero_1 : {type(numero_1)}")
        print (f"Tipo de dato de numero_2 : {type(numero_2)}")
        return render.calculadora(numero_1,numero_2, resultado)
if __name__ == "__main__":
    app.run()

