from flask import Flask, render_template, request
from logging import debug
import utlils

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        Open = request.form.get('Open')
        High = request.form.get('High')
        Low = request.form.get('Low')
        Volume = request.form.get('Volume')
        prediction = utlils.preprocess(Open, High, Low, Volume)
        return render_template('prediction.html', prediction=prediction)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)