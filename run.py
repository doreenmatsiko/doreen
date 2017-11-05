from app import app

@app.route("/")
def index():
    return "Edgar is awesome"


@app.route("/a")
def index_i():
    return "dgar is awesome"
if __name__=="__main__":
    app.run(debug=True)
