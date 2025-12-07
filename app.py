from flask import Flask, request, render_template, redirect, url_for
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def create_meme(image_path, top_text, bottom_text, out_path):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_PATH, 50)

    # Top text
    top_bbox = draw.textbbox((0, 0), top_text, font=font)
    top_w = top_bbox[2] - top_bbox[0]
    top_h = top_bbox[3] - top_bbox[1]

    # Bottom text
    bottom_bbox = draw.textbbox((0, 0), bottom_text, font=font)
    bottom_w = bottom_bbox[2] - bottom_bbox[0]
    bottom_h = bottom_bbox[3] - bottom_bbox[1]

    # Positions
    draw.text(((img.width - top_w) / 2, 10), top_text, font=font, fill="white")
    draw.text(((img.width - bottom_w) / 2, img.height - bottom_h - 10), bottom_text, font=font, fill="white")

    img.save(out_path)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    file = request.files.get('image')
    top_text = request.form.get('top_text', '')
    bottom_text = request.form.get('bottom_text', '')

    if not file:
        return "No file uploaded", 400

    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded.png')
    out_path = os.path.join(app.config['UPLOAD_FOLDER'], 'generated.png')
    file.save(input_path)

    create_meme(input_path, top_text, bottom_text, out_path)

    return render_template('result.html', meme_url=url_for('static', filename='generated.png'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
