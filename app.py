from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        try:
            x = float(request.form['num1'])
            y = float(request.form['num2'])
            op = request.form['operation']
            if op == '+':
                result = x + y
            elif op == '-':
                result = x - y
            elif op == '*':
                result = x * y
            elif op == '/':
                result = "Error: div by zero" if y == 0 else x / y
            else:
                flash("Invalid operation selected", 'error')
        except ValueError:
            flash("Please enter valid numbers", 'error')
    return render_template('index.html', result=result)
    
if __name__ == '__main__':
    app.run(debug=True)
