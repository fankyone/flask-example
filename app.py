from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/personal')
def personal():
    return render_template('personal.html')

@app.route('/Devops')
def Devops():
    return render_template('Devops.html')

@app.route('/GameStreaming')
def GameStreaming():
    return render_template('GameStreaming.html')

@app.route('/MultiplayerGame')
def MultiplayerGame():
    return render_template('MultiplayerGame.html')

@app.route('/ImmersiveProjects')
def ImmersiveProjects():
    return render_template('ImmersiveProjects.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
