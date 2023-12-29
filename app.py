from flask import Flask, request, render_template 
 
app = Flask(__name__, static_folder='static') 
 
@app.route('/') 
def index(): 
    return render_template('index.html') 
 
@app.route('/process', methods=['POST']) 
def process(): 
    # This function will be called when the button is clicked 
    # You can write your Python code here 
    return 'Function called successfully' 

@app.route('/test', methods=["GET", "POST"])
def file_upload():
    return render_template("sup.html")

 
if __name__ == '__main__': 
    app.run(debug=True) 