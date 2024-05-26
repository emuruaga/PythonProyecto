from django.http import HttpResponse
from django.template import Template, Context, loader

def saludo(req):
    return HttpResponse('Holaaaa Mundillooo!!!')

def saludoCopado(req):
    return HttpResponse('''
    <h1>Bienvenidos a mi página web cabrón!!!</h1>
    <br>
    <p>Esto está muy copadoooo</p>
                        ''')

def saludo_con_nombre(req, nombre, apellido):
    documentoTexto = f'Mi nombre es: <br> {nombre} {apellido}'
    return HttpResponse(documentoTexto)

def probando_template(req):
    template = loader.get_template('template1.html')
    documento = template.render({
        'name': 'Henry',
        'apellido': 'Muruaga',
        'notas': [8, 5, 7, 9, 4]
    })
    return HttpResponse(documento)





    # miHtml=open('C:/Users/COMPAQ/Desktop/Coder/Python/PythonProyecto/Proyecto1/template/template1.html')
    # plantilla= Template(miHtml.read())
    # miHtml.close()
    # miContexto= Context({
    #     'name':'Henry',
    #     'apellido':'Muruaga',
    #     'notas':[8,5,7,9,4]
    # })
    # documento=plantilla.render(miContexto)
    # return HttpResponse(documento)
    plantilla=loader.get_template('template1.html')
    documento=plantilla.render({
         'name':'Henry',
         'apellido':'Muruaga',
         'notas':[8,5,7,9,4]
     })
    return HttpResponse(documento)
