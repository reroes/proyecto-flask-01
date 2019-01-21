# -*- coding: utf-8 -*-

from flask import Flask, render_template, flash, request
from flask import jsonify

from aplicacion.forms import MyForm
from aplicacion import app
from aplicacion.models import Country 


@app.route('/')
@app.route('/index')
def index():
    """
    """
    user = {'username': u'René Elizalde'}
    return render_template('index.html', user=user)


@app.route('/ejemplo')
def ejemplo():
    """
        Ejemplo de bucle
    """
    autores = [
        {
            'identificacion': {'username': 'John', 'apellido': 'Elizalde'},
            'titulo': 'Estudiante'
        },
        {
            'identificacion': {'username': 'Daniel', 'apellido': u'Pérez'},
            'titulo': 'Estudiante'
        }
    ]
    
    form = MyForm()
    return render_template('ejemplo.html', autores = autores, form = form)

@app.route('/countries')
def countrydic():
    paises = Country.query.all()
    list_paises = [r.as_dict() for r in paises]
    return jsonify(list_paises)

@app.route('/process', methods=['POST'])
def process():
    country = request.form['country']
    print(country)
    pais = [p for p in Country.query.all() if p.name==country]
    if len(pais)>0:
        return jsonify({'country':country})
    return jsonify({'error': 'missing data..'})
