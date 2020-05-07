from flask import Flask, jsonify, render_template
import appfunctions

app = Flask(__name__)


@app.route('/', methods=['Get'])

def apphome():
    #return jsonify(appfunctions.getConfig(app))
    return render_template('page.html', title='AlphaDemoContainer', paras=appfunctions.getConfig(app))

   
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8010, debug=True)