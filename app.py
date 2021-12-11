from flask import Flask, request, render_template
import pickle
import pandas as pd
import json
import plotly
import plotly.express as px
from datetime import datetime


app = Flask(__name__)

model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Prediksi tamu dan menampilkannya ke html
    
    df = pd.read_csv('notebook/data/JakartaHotel.csv', index_col=['dt'], parse_dates=True)
    
    first, last = [x for x in request.form.values()]
    first = datetime.strptime(first, '%Y-%m')
    last = datetime.strptime(last, '%Y-%m')
    selisih = (last.year - first.year) * 12 + (last.month - first.month)
    
    pred = model.predict(start=len(df)-1, end=len(df-1)+selisih, typ='levels')
    
    # melakukan shift data -1
    idx = pred.index.values

    x = df.value
    pred_tamu = []
    lag = 1
    for i, diff in enumerate(pred):
        prev_value = x[-(lag)+i:][0]
        pred_tamu.append(prev_value+diff)
    
    data = pd.DataFrame({'Datetime': idx, 'Jumlah Tamu': pred_tamu})
    print(data)
    
    figure = px.line(data, x='Datetime', y='Jumlah Tamu')
    graphJson = json.dumps(figure, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', graphJson = graphJson)


if __name__ == '__main__':
    app.run(debug=True)