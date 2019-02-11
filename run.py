from app import create_app

config_name = "development"
app = create_app(config_name)


@app.route("/")
def home():
    return "hello world"

if (__name__ == "__main__"):
    app.run()