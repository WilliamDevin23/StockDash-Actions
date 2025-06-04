from flask import Flask
from update_news import update_news
from update_price import update_price
from update_volume import update_volume

app = Flask(__name__)

@app.route("/")
def index() :
    try :
        return "Halo!"
    except Exception as e:
        return f"Error happened : {e}"

@app.route("/update_price")
def api_update_price() :
    try :
        update_price()
        return "Successfully update price"
    except Exception as e:
        return f"Error happened : {e}"

@app.route("/update_news")
def api_update_news() :
    try :
        update_news()
        return "Successfully update news"
    except Exception as e:
        return f"Error happened : {e}"
        
@app.route("/update_volume")
def api_update_volume() :
    try :
        update_volume()
        return "Successfully update trade volume"
    except Exception as e:
        return f"Error happened : {e}"
        
if __name__ == "__main__" :
    app.run()
