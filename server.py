from flask import Flask

app = Flask(__name__)

@app.route("/")
async def route():
    return "VysakhTG"

if __name__ == "__main__":     
   app.run()
