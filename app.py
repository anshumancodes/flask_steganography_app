from flask import Flask, render_template, request, send_file, url_for
from PIL import Image
import io, os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/encoded"

def encode_message(img, message):
    encoded = img.copy()
    width, height = img.size
    message += "%%"  # end marker
    data_index = 0
    binary_message = ''.join([format(ord(i), '08b') for i in message])

    for x in range(width):
        for y in range(height):
            pixel = list(img.getpixel((x, y)))
            for n in range(3):
                if data_index < len(binary_message):
                    pixel[n] = pixel[n] & ~1 | int(binary_message[data_index])
                    data_index += 1
            encoded.putpixel((x, y), tuple(pixel))
            if data_index >= len(binary_message):
                return encoded
    return encoded

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    if 'image' not in request.files or 'message' not in request.form:
        return "Missing fields", 400

    image = Image.open(request.files['image'])
    message = request.form['message']

    encoded_img = encode_message(image, message)
    output_path = os.path.join(app.config["UPLOAD_FOLDER"], "encoded.png")
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)  # fixed

    encoded_img.save(output_path)

    whatsapp_link = f"https://api.whatsapp.com/send?text=Check+this+secret+image:+{request.url_root}{output_path}"

    return render_template("index.html", encoded_image=output_path, whatsapp_link=whatsapp_link)


if __name__ == '__main__':
    app.run(debug=True)
