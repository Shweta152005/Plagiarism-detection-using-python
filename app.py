from flask import Flask, render_template, request
import difflib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = "Upload two files to check plagiarism."
    
    if request.method == 'POST':
        # Ensure both files are provided
        if 'file1' in request.files and 'file2' in request.files:
            file1 = request.files['file1']
            file2 = request.files['file2']
            
            # Read the contents of both files
            file1_content = file1.read().decode('utf-8', errors='ignore')
            file2_content = file2.read().decode('utf-8', errors='ignore')

            # Check for plagiarism using difflib (this is a simple example)
            similarity_ratio = difflib.SequenceMatcher(None, file1_content, file2_content).ratio()
            
            # Display similarity percentage as the result
            result = f"Plagiarism Similarity: {similarity_ratio * 100:.2f}%"
        else:
            result = "Both files are required."

    return render_template("index.html", result=result)

if __name__ == "_main_":
    app.run(debug=True, use_reloader=False, port=5001)  # Change port to 5001