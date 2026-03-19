'''
runs flask server
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_detector():
    """This function performs emotion analysis on given text"""
    # get text from req
    txt = request.args.get("textToAnalyze")
    # pass text to emotion_detector -- get resp
    resp = emotion_detector(txt)
    if resp['anger'] is None:
        return "Invalid text! Please try again!"
    # save dom emotion
    dom = resp.pop("dominant_emotion")
    # trim out {}
    str_resp = str(resp)
    str_resp = str_resp[1:-2]
    # format output
    return f"""For the given statement, the system response is {str_resp}. The dominant emotion is
     <strong>{dom}</strong>"""

@app.route("/")
def render_index():
    """This function renders the home page of app"""
    return render_template('index.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000)
