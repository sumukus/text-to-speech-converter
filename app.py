from flask import Flask, render_template, request
from gtts import gTTS

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
	status = 0
	if request.method == "POST":
		if request.form.get('mp3') == "Convert":
			text_data = request.form.get('text')
			language = request.form.get('lang')
			audio = gTTS(text_data, lang=language)
			audio.save("static/your_audio.mp3")
			status = 1
			return render_template("index.html", status=status)

	return render_template("index.html", status=status)


if "_name__" == "__main__":
	app.run(debug=True)
