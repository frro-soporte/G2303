from flask import Flask,render_template,jsonify,redirect,request
# from db.todos import get_todos
from business import NegocioSocio
from model import Socio
app = Flask(__name__)


@app.route('/')
def index():
    socios = NegocioSocio().todos()
    
    print(len(socios))
    print('TOTAL :: ',)
    return render_template('index.html', socios=socios)


# create a route to create a socio with a form
@app.route('/socios/create', methods=['GET'])
def createSocio():
    return render_template('/socios/create.html')

# create a route to edit a socio with a form
@app.route('/socios/<id>/edit', methods=['GET'])
def editSocio(id):
    print('hello :: ', id)
    socio = NegocioSocio().buscar(id)
    print(socio.dni)
    return render_template('/socios/edit.html',socio=socio)

# create a route to save a socio with a form
@app.route('/socio/save', methods=['POST'])
def saveSocio():
    data = request.form # send data with post method in the form
    # validate the dni,apellido y nombre 
    socio = Socio(dni=data['dni'], nombre=data['nombre'], apellido=data['apellido'])  
    try:
        res = NegocioSocio().alta(socio)
        if res == True :
            return redirect('/')
        else:
            return render_template('/socios/create.html',error=res)
    except Exception as e:
        print('ERROR :: ',e)
        return render_template('/socios/create.html',error=e,oldData=data)
    
    return jsonify(data)
    #return render_template('/socios/create.html')

# create a route to save a socio with a form
@app.route('/socio/modify', methods=['POST'])
def saveModify():
    data = request.form # send data with post method in the form
    # validate the dni,apellido y nombre 
    print('DATA :: ',data)
    socio = Socio(dni=data['dni'], nombre=data['nombre'], apellido=data['apellido'],id=data['id'])

    res = NegocioSocio().modificacion(socio)
   
    if res != None :
        return redirect('/')
    else:
        return render_template('/socios/edit.html',error=res)
# create a route to delete a socio with a form
@app.route('/socios/<id>/delete')
def deleteSocio(id):
    try : 
        res = NegocioSocio().baja(id)    
        if res == True :
            return redirect('/')
        else:
            return render_template('/socios/delete.html',error=res,id=id)
    except Exception as e:
        print('ERROR :: ',e)
        return render_template('/socios/delete.html',error=e,id=id)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
