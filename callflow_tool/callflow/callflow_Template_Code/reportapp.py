from flask import render_template, Flask, request, jsonify
app = Flask(__name__, static_folder="/home/pgokhe/venv/callflow/callflow_Template_Code")
import pandas
import sys
import datetime
#import config
import importlib.util
spec = importlib.util.spec_from_file_location("config", sys.argv[1])
foo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(foo)
config = foo

@app.route('/', methods=["GET", "POST"])
def button():
    filename = '/home/pgokhe/venv/callflow/callflow_Template_Code/testreporting.csv'
    data = pandas.read_csv(filename, header=0)
    myData = data.values
    date = datetime.date.today()
    print(myData)
    return render_template("help.html", myData= myData, date = date)

if __name__ == '__main__':
	app.run(host=config.CONTROLLERIP, port=9000)