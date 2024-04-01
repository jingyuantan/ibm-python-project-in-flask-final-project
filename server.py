"""
Emotion Detection Server

This script defines a Flask-based server for performing emotion detection on user-input text.

Author: Jing Yuan Tan
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_predictor

app = Flask("Emotion Detection")


@app.route("/")
def render_index_page():
    """
    This function renders the main page of the application.
    """
    return render_template('index.html')


@app.route("/emotionDetector", methods=['GET'])
def call_emotion_detector():
    """
    This function receives GET requests from client,
    predicting the emotion of the user input,
    by returning the score for each emotion of the sentence and
    the final prediction of the dominant emotion of the user input.
    """
    user_input_text = request.args.get('textToAnalyze')
    result = emotion_predictor(user_input_text)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
