from flask import Flask, render_template, jsonify, request
import os
from werkzeug.utils import secure_filename
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'AI_Service')))
from gemini_response_image import  process_image_with_gemini
from gemini_response_text import get_gemini_response

app = Flask(__name__, template_folder="../Frontend/templates", static_folder="../Frontend/static")



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/text',methods=['POST'])
def simplData():
    data = request.get_json()
    user_message = data.get('msg')
    bot_msg  = get_gemini_response(user_message)
    return jsonify({'msg':bot_msg})

@app.route('/api/image', methods=['POST'])
def image_save():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        uploads_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../uploads')

        if not os.path.exists(uploads_folder):
            os.makedirs(uploads_folder)

        filename = secure_filename(file.filename)
        file_path = os.path.join(uploads_folder, filename)

        file.save(file_path)
        
        response = process_image_with_gemini(file_path)
        print(response)

        return jsonify({"botImgResTxt": response, "file_path": file_path})

    return jsonify({"error": "File not saved"}), 500
    

if __name__ == "__main__":
       app.run(host='0.0.0.0', port=3000, debug=True)