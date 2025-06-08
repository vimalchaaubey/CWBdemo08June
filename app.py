from flask import Flask, render_template, request

app = Flask(__name__)

PROBLEM_STATEMENTS = [
    "AI for Healthcare",
    "Smart City Solutions",
    "Sustainable Energy",
    "EdTech Innovation",
    "FinTech for All"
]

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = {
            'name': request.form.get('name'),
            'email': request.form.get('email'),
            'institute': request.form.get('institute'),
            'branch': request.form.get('branch'),
            'year': request.form.get('year'),
            'problem': request.form.get('problem')
        }
        return render_template('display.html', data=data)
    return render_template('register.html', problems=PROBLEM_STATEMENTS)

if __name__ == '__main__':
    app.run(debug=True)
