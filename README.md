# 🕵️‍♂️ Flask Steganography App

A simple Flask-based web application that allows users to **hide (encode)** and **retrieve (decode)** secret text messages inside images using **steganography** techniques.

---

## 🚀 Features

- Upload an image and embed a secret message inside it.
- Decode a hidden message from an encoded image.
- Simple and intuitive Flask web interface.
- Stores encoded images for download (`/static/encoded/` folder).
- Lightweight and easy to run locally.

---

## 📁 Project Structure

flask_steganography_app/
├── app.py # Main Flask application

├── requirements.txt # Dependencies list

├── templates/ # HTML templates for the app

│ ├── encode.html

│ └── decode.html

├── static/

│ └── encoded/ # Folder for generated encoded images

├── .gitignore

└── README.md # Project documentation

---

## ⚙️ Installation and Setup

Follow the steps below to get the app running locally on your computer 👇

### 🧩 Prerequisites

- **Python 3.6+**
- **pip** (Python package manager)
- *(Optional)* Virtual environment for isolation

### 🪜 Steps to Run

```bash
# 1. Clone the repository
git clone https://github.com/anshumancodes/flask_steganography_app.git

# 2. Navigate into the project directory
cd flask_steganography_app

# 3. (Optional) Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate       # On macOS/Linux
venv\Scripts\activate          # On Windows

# 4. Install all dependencies
pip install -r requirements.txt

# 5. Run the Flask application
python app.py
```

---

## 🧭 How to Use the Application

### 🔒 Encode (Hide a Message)

1. Click on the Encode page in the app.
2. Upload a normal image file (e.g., .png or .jpg).
3. Enter your secret text message in the input field.
4. Click Submit — the app will process the image.
5. The new encoded image (with hidden text) will be saved in static/encoded/.
6. You can download or share this encoded image safely.

### 🔓 Decode (Reveal a Message)

1. Go to the Decode page.
2. Upload an encoded image (one created through this app).
3. Click Submit.
4. The app will extract and display the hidden message instantly.

---

## 🧰 Example Workflow

Here’s what a typical workflow looks like:

1. **User uploads an image** → chooses a message → app encodes and saves it.
2. **Another user uploads that encoded image** → app extracts and displays the hidden message.

🖼️ The actual image looks unchanged to the eye — but your secret message is hidden in its pixels!

---

## 💡 Use Cases

- 🎓 Educational Projects — Learn Flask, Python file handling, and image manipulation.
- 🧑‍💻 Cybersecurity Demos — Demonstrate data hiding techniques.
- 🔍 Privacy Applications — Prototype message-hiding tools.
- 🪄 Fun Experiments — Hide secret notes or easter eggs in your images.

---

## 👨‍💻 Author
**Developed by:** [anshumancodes](https://github.com/anshumancodes), [sahil nayak](https://github.com/sahilnyk), [Rohan Bandha](https://github.com/rohanbandha), [Manishi Marjeet](https://github.com/DABOZE), [Subhrakant Singh](https://github.com/subhrakant1299)

💡 Built with ❤️ using **Python** and **Flask**

---

## ✍️ Documentation Contributor

**README created and formatted by:** [Rohan Bandha](https://github.com/rohanbandha)  
📚 *For academic and educational purposes — Birla Global University project.*
