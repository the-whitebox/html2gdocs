from flask import Flask, render_template
import json

app = Flask(__name__ , template_folder='templates')

@app.route('/')
def display_json_data():
    # Read and parse the JSON file
    with open('example.json', 'r') as json_file:
        data = json.load(json_file)

    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
