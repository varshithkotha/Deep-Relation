from flask import *
import os
from Family_detect import calculate_similarity_for_folders

app = Flask(__name__)

# Create the 'uploads' directory if it doesn't exist
uploads_dir = os.path.join(app.root_path, 'uploads')
if not os.path.exists(uploads_dir):
    os.makedirs(uploads_dir)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_file(os.path.join(uploads_dir, filename), as_attachment=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        
        if uploaded_file.filename != '':
            query_image_path = os.path.join(uploads_dir, uploaded_file.filename)
            uploaded_file.save(query_image_path)

            root_folder_path = r"C:\Users\Varshith\OneDrive\Desktop\deep relation project\Families"

            results, top_results = calculate_similarity_for_folders(root_folder_path, query_image_path)

            return render_template('index.html', query_image=query_image_path, results=results, top_results=top_results)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
