from flask import Flask, request, render_template, send_file, Response
import os
from wordcloud_generator import generate_word_cloud
from io import BytesIO

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text_data = request.form.get('text_data')
        
        if not text_data:
            return "Please enter some text data."

        wordcloud = generate_word_cloud(text_data)
        
        # Create a downloadable response
        img_bytes_io = BytesIO()
        wordcloud.to_image().save(img_bytes_io, 'PNG')
        img_bytes = img_bytes_io.getvalue()
        img_bytes_io.close()
        
        return Response(img_bytes, mimetype='image/png', headers={
            'Content-Disposition': 'attachment; filename=wordcloud.png'
        })

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
