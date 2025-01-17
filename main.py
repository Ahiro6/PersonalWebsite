from flask import Flask, render_template
# import portfolio.Mapping.map
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/portfolio/")
def portfolio():
    return render_template("Portfolio.html")


@app.route("/guess/")
def guess():
    return render_template("guess.html")


@app.route("/map/")
def map():
    return render_template("Map.html")

@app.route("/pokemon/")
def pokemon():
    return render_template("pokemon.html")

@app.route("/scorekeeper/")
def scorekeeper():
    return render_template("Score.html")


# if __name__ == "__main__":
app.run(debug=True)
