from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/projects")
@app.route("/projects/<docs>")
def projects(docs = None):
    if docs == None:
        return render_template("projects.html")
    else:
        return render_template("documents.html", docs = docs)

if __name__ == "__main__":
    app.run(debug = True)
