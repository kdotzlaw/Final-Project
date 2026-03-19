from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_detector():
    # get text from req
    txt = request.args.get("textToAnalyze")

    # pass text to emotion_detector -- get resp
    resp = emotion_detector(txt)

    # save dom emotion
    dom = resp.pop("dominant_emotion")

    # trim out {}
    str_resp = str(resp)
    str_resp = str_resp[1:-2]

    # format output
    return f"For the given statement, the system response is {str_resp}. The dominant emotion is <strong>{dom}</strong>"

# render base template
@app.route("/")
def render_index():
    return render_template('index.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)