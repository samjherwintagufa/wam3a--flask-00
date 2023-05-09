from flask import Flask


app = Flask(__name__)

@app.route("/")
def index():
    return "<center><a href='/goodmorning'><button>goodmorning</button></a><a href='/breakfast'><button>breakfast</button></a><a href='/galit'><button>galit</button></a><a href='/suyo'><button>suyo</button></a><a href='/sorry'><button>sorry</button></a></center>"

@app.route("/goodmorning")
def goodmorning():
    return "<center><strong><p>GOODMORNING MY LOVE</p></strong><a href='/'><button>back</button></a></center>"
@app.route("/breakfast")
def breakfast():
    return "<center><strong><p>Nag breakfast ka na?</p></strong><a href='/'><button>back</button></a></center>"
@app.route("/suyo")
def suyo():
    return "<center><strong><p>Suyuin mo naman ako uwu</p></strong><a href='/'><button>back</button></a></center>"
@app.route("/galit")
def galit():
    return "<center><strong><p>Di ako galit bahala ka K!</p></strong><a href='/'><button>back</button></a></center>"

@app.route("/sorry")
def sorry():
    return "<center><strong><p>Sorry na</p></strong><a href='/'><button>back</button></a></center>"