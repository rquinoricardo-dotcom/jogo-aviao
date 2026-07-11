from flask import Flask, render_template, request
import random

app = Flask(__name__)

saldo = 100.0

@app.route('/', methods=['GET', 'POST'])
def home():
    global saldo
    mensagem = ""
    multiplicador = None
    
    if request.method == 'POST':
        try:
            aposta = float(request.form.get('aposta', 0))
            if aposta > 0 and aposta <= saldo:
                multiplicador = round(random.uniform(1.0, 5.0), 2)
                ganho = aposta * multiplicador
                saldo = saldo - aposta + ganho
                mensagem = f"Você ganhou {ganho:.2f} MZN!"
            else:
                mensagem = "Aposta inválida!"
        except ValueError:
            mensagem = "Por favor, digite um número válido."
            
    return render_template('index.html', saldo=round(saldo, 2), multiplicador=multiplicador, mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True)
