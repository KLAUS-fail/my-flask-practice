from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        if user_name:
            session['user_name'] = user_name
            
    name = session.get('user_name')
    return render_template('index.html', name=name)

@app.route('/clear')
def clear_session():
    """Та самая очистка для отчета ПМ.04"""
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
