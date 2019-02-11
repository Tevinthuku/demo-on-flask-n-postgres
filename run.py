from app import createApp

config_name = "development"
app = createApp(config_name)


@app.route("/")
def home():
    return "hello world"

if (__name__ == "__main__"):
    app.run()