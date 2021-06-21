from flask import Flask

app10 = Flask(__name__)

@app10.route('/',methods=['Get','Post'])
def index():
    return "<H1>This is the practise code!!! Sucessfully Done..</H1>"

if __name__ == "__main__":
    app10.run(debug=True)
