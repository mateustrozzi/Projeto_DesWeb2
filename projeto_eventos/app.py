from flask import Flask
from controllers.evento_controller import evento_bp

app = Flask(__name__)
app.register_blueprint(evento_bp)

if __name__ == "__main__":
    app.run(debug=True)


#versão antiga, apagar depois ou adaptar

#from flask import Flask, render_template
#app = Flask(__name__)

#@app.route("/teste")
#def teste():
#    return render_template('index.html')

#@app.route("/")
#def inicio():
#    return "Olá mundo! - DSM - SEMII"

#@app.route("/sobre")
#def sobre():
#    return """
#    <head>
#        <link rel='stylesheet' href='/static/style.css'>
#    </head>
#    <body>
#        <h1>Gestão de Eventos - DW2</h1>
#    </body>
#    """


#@app.route("/eventos")

#def eventos():
    #return "<h1 style='color: red; text-align: center; font-size: 48pt'>Lista de eventos aqui..</h1>"
    #""
#    lista_eventos = []          # cria uma lista vazia
#    x = {
#    "nome": "Semana da Computação",
#    "data": "10-09-2026",
#    "local": "Auditório"
#}
#    lista_eventos.append(x)     # adiciona o item x ao final da lista
    #return lista_eventos RETORNA JSON
    #retornaa html

#    html = "<div style='font-family: sans-serif;'>"
#    for ev in lista_eventos:
#        html += f"<h2>{ev['nome']}</h2>"
#        html += f"<p><b>Data:</b> {ev['data']} - <b>Local:</b> {ev['local']}</p>"
#        html += f"<span style='color: red; font-size: xx-large;font-family: 'Arial Narrow Bold';'><strong>NÃO PERCA!!</strong></span>"
#    html += "</div>"
    
#    return html


#if __name__ == "__main__":
#    app.run(debug=True)


