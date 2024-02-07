from flask import Flask,render_template, request
from flask_wtf import CSRFProtect

# In Flask, we are having generally 2 ways to create a form one by using FlaskForm and another by creating forms manually. FlaskForm processes the request that already getting CSRF Protection. Csrf requires a secret key by default, it uses the Flask app’s Secret Key.

#  If you like to set up a separate token then you can use WTF_CSRF_SECRET_KEY instead of using a flask app’s secret key. While using FlaskForm, you will have to render the forms CSRF field.n You can disable the CSRF Protection in all views by default, then set WTF_CSRF_CHECK_DEFAULT to False in the app.py file.

app = Flask(__name__)
app.secret_key = b'_53oi3uriq9pifpff;apl'
csrf = CSRFProtect(app)

@app.route("/protected_form", methods=['GET', 'POST'])
def protected_form():
    if request.method == "POST":
        name = request.form['Name']
        return (f'Hello {name}')
    return render_template('index.html')

@app.route("/unprotected_form", methods = ['GET', 'POST'])
def unprotected_form():
    if request.method == "POST":
        name = request.form['Name']
        return (f'Hello {name}')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)