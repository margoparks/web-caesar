from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True
form = ''' <!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540 px;
                height: 120px;
            }}
        </style>
    </head>
    </body>
        <form action="/" method="POST">
            <label for="rot"> Rotate by: </label>
            <input type="text" name="rot" value="0" > 
            <br>
            <textarea name="text" rows=3 cols=50> {message} </textarea>
            <input type="submit" value="Submit" >
        </form>
    </body>
</html> '''

@app.route("/")
def index():
    return form.format(message="")

@app.route("/" , methods=['POST'])
def encrypt():
    text = request.form["text"]
    rot = int(request.form["rot"])
    encrypted_text = rotate_string(text,rot)
    content = form.format(message=encrypted_text)
    return content 


app.run()
