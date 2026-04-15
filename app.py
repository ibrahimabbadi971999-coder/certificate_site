from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='.', static_folder='.')

VALID_CERT = "B00907099"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cert_number = request.form.get('cert_number')

        if cert_number == VALID_CERT:
            return redirect(url_for('result'))
        else:
            return "Invalid certificate number"

    return render_template('index.html')


@app.route('/result')
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run()