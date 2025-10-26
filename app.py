from flask import Flask, render_template, request, send_file, url_for
from PIL import Image
import io, os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/encoded"

# ----------------- ENCODE -----------------
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

# ----------------- DECODE -----------------
def decode_message(img):
    binary_data = ""
    width, height = img.size

    for x in range(width):
        for y in range(height):
            pixel = img.getpixel((x, y))
            for n in range(3):
                binary_data += str(pixel[n] & 1)

    # Split into bytes (8 bits each)
    message = ""
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        char = chr(int(byte, 2))
        message += char
        if message[-2:] == "%%":  # end marker
            return message[:-2]
    return message

# ----------------- ROUTES -----------------
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
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
    output_path = os.path.join(app.config["UPLOAD_FOLDER"], "encoded.png")
    encoded_img.save(output_path)

    whatsapp_link = f"https://api.whatsapp.com/send?text=Check+this+secret+image:+{request.url_root}{output_path}"

    return render_template("index.html", encoded_image=output_path, whatsapp_link=whatsapp_link)

@app.route('/decode', methods=['POST'])
def decode():
    if 'image' not in request.files:
        return "No image uploaded", 400

    image = Image.open(request.files['image'])
    message = decode_message(image)

    return render_template('index.html', decoded_message=message)

# ----------------- RUN -----------------
if __name__ == '__main__':
    app.run(debug=True)
