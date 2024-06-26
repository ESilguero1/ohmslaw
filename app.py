from flask import Flask, redirect, url_for, render_template
app = Flask(__name__, static_folder='static')

@app.route("/", methods=["POST", "GET"])
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)