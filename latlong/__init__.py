from flask import Flask, request, render_template
from .helpers import process_locations, process_one_location

app = Flask(__name__)

@app.route('/process_text', methods=['POST'])
def process_text():
    uploaded_text = request.form['uploaded_text']
    # Process the uploaded_text here (e.g., perform some operations)
    processed_output = f"Processed text: {uploaded_text.upper()}"
    return render_template('output.html', output=processed_output)

@app.route('/latlong', methods=['GET', 'POST'])
def get_latlong():
    if request.method == 'POST':
        raw_locations = request.form.get('raw_locations_text').split("\n")
    else:
        raw_locations = [request.args.get('location')]
    locations = process_locations(raw_locations)
    return render_template(
        'index.html', 
        content_page="results.html", 
        locations=locations
        )

@app.route('/test')
def test_location():
    location = process_one_location("melbourne")
    try:
        assert str(location.latitude).startswith("-37")
        assert str(location.longitude).startswith('144')
        print(location.latitude, location.longitude)
        test_result = "True"
    except AssertionError:
        test_result = "False"
    return render_template('index.html', content_page="test_results.html", test_result=test_result)

@app.route('/')
def home():
    content_page = "search.html"
    return render_template('index.html', content_page=content_page)