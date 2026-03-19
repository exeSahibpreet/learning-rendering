from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    percentage = None

    if request.method == 'POST':
        try:
            maths = float(request.form['maths'])
            chemistry = float(request.form['chemistry'])
            physics = float(request.form['physics'])
            english = float(request.form['english'])

            total = maths + chemistry + physics + english
            percentage = (total / 400) * 100

        except:
            percentage = "Invalid input. Please enter numbers only."

    return render_template('index.html', percentage=percentage)

if __name__ == '__main__':
    app.run(debug=False)
