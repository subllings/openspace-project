"""
Main Flask application to handle file uploads, process seating assignment,
and render results to the user.
"""

from flask import Flask, request, render_template, redirect, url_for, send_file
import os
from utils.file_utils import load_colleagues_from_excel
from utils.openspace import Openspace

app = Flask(__name__)

# Folder where uploaded files will be stored
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET'])
def index():
    """
    Render the upload page.
    """
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    """
    Receive the uploaded Excel file, save it, process the seating,
    and display the seating arrangement.
    """
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No file selected", 400

    if file and file.filename.endswith('.xlsx'):
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # Load names from Excel
        names = load_colleagues_from_excel(filepath)

        # Initialize Openspace with default 6 tables of 4 seats (configurable)
        room = Openspace(6, 4)
        room.organize(names)

        # Handle lonely persons if any
        if room.is_there_lonely_person():
            room.eliminate_lonely_tables()

        # Prepare data for template rendering
        tables_data = []
        for i, table in enumerate(room.tables, start=1):
            seats = [(idx+1, seat.occupant if not seat.free else "Free") for idx, seat in enumerate(table.seats)]
            tables_data.append({"table_num": i, "seats": seats})

        return render_template('result.html', tables=tables_data)

    return "Invalid file format. Please upload an .xlsx file.", 400

@app.route('/download')
def download():
    """
    Allow downloading the output CSV file if implemented.
    """
    output_path = 'data/output.csv'
    if os.path.exists(output_path):
        return send_file(output_path, as_attachment=True)
    else:
        return "No output file available.", 404

if __name__ == '__main__':
    # Run Flask app in debug mode for development
    app.run(debug=True)
