import PIL.Image
from flask import Flask, render_template, request
from find_similar_imgs import most_similar_images

app = Flask(__name__)


@app.route('/')
def main():
    # for testing purposes
    return render_template("upload.html")


@app.route('/similar-images', methods=['POST'])
def similar_images():
    f = request.files['image']
    img = PIL.Image.open(f.stream)
    return most_similar_images(img)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
