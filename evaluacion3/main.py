from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])
        promedio = (nota1 + nota2 + nota3)/3
        if promedio >= 40 and  asistencia >= 75 :
            resultado = "Aprobado"
        else :
            resultado = "Reprobado"
            
        return render_template('ejercicio1.html', promedio=promedio, resultado = resultado)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = str(request.form['nombre1'])
        nombre2 = str(request.form['nombre2'])
        nombre3 = str(request.form['nombre3'])
        if len(nombre1)> len(nombre2):
            if(nombre1)>len(nombre3):
                resulNombre = nombre1
                cantNombre = len(nombre1)
            else:
                resulNombre = nombre3
                cantNombre = len(nombre3)
        else :
            if len(nombre2)>len(nombre3):
                resulNombre = nombre2
                cantNombre = len(nombre2)
            else :
                resulNombre = nombre3
                cantNombre = len(nombre3)
            
        return render_template('ejercicio2.html', nombre=resulNombre, cant = cantNombre)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run()