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
        team_name = request.form.get('team_name')
        team_size = int(request.form.get('team_size', 1))
        members = []
        for i in range(1, team_size + 1):
            members.append({
                'name': request.form.get(f'member_name_{i}'),
                'email': request.form.get(f'member_email_{i}'),
                'institute': request.form.get(f'member_institute_{i}'),
                'branch': request.form.get(f'member_branch_{i}'),
                'year': request.form.get(f'member_year_{i}')
            })
        data = {
            'team_name': team_name,
            'team_size': team_size,
            'members': members,
            'problem': request.form.get('problem')
        }
        return render_template('display.html', data=data)
    return render_template('register.html', problems=PROBLEM_STATEMENTS)

if __name__ == '__main__':
    app.run(debug=True)
