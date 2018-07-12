from flask import Flask, flash, redirect, render_template, request, session, abort
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')



@app.route('/', methods=['POST'])
def input_text_post():
    inputText = request.form['inputText']
    # Put conversion methods here and use inputText as the parameter
    print(inputText) # Remove this
    return ('', 204)

if __name__ == "__main__":
    app.debug = True
    app.run()
