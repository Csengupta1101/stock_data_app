import os
import yfinance as yf
import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/fetch_stock_data', methods=['POST'])
def fetch_stock_data():
    data = request.json

    start_date = data['start_date']
    end_date = data['end_date']
    company_name = data['company_name']
    output_folder = data['output_folder']

    try:
        stock_data = yf.download(company_name, start=start_date, end=end_date)
        output_file_path = os.path.join(output_folder, f"{company_name}_stock_data.csv")
        stock_data.to_csv(output_file_path)
        response = {
            'status': 'success',
            'message': f"Stock data for {company_name} saved to {output_file_path}"
        }
        return jsonify(response), 200
    except Exception as e:
        response = {
            'status': 'error',
            'message': str(e)
        }
        return jsonify(response), 400

if __name__ == '__main__':
    app.run(debug=True)
