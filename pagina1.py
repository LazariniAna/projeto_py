from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html', var_titulo = "My page")

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/services")
def services():
    return render_template('services.html')

#@app.route("/alunos")
#def rota_teste_alunos():
 #   return "texto/ ou tags em HTML"\
  #      "\n<br/>" \
   #     "<strong>Essa é uma mensagem em negrito.</strong>"\
    #    "\n<br/>" \
     #   "<p>Olha a tag HTML de paragrafo aqui </p>"\
      #  "<img src = 'https://picsum.photos/200/300'>" 
            

app.run(debug=True)