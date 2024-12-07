"""
Emotion Detector Flask Application

This Flask application provides an interface for users to submit text for emotion detection. 
It uses the `emotion_detector` function from the `EmotionDetection.emotion_detection` module 
to analyze the emotions in the provided text. The app is accessible at the root endpoint, 
and it returns the results of emotion detection, including the dominant emotion, 
in a formatted string.

Routes:
- /: The homepage where users can input text to analyze.
- /emotionDetector: The route that performs emotion detection on the input text.

Dependencies:
- Flask: A micro web framework used to create the web application.
- EmotionDetection: A module for performing emotion detection on text.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/')
def index():
    """
    Render the index page where users can input text to analyze.
    
    Returns:
        str: HTML page rendered from 'index.html' template.
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def detector():
    """
    Handle the request for emotion detection on the input text.
    
    This route extracts the input text from the query string, calls the 
    emotion_detector function to analyze it, and formats the results to 
    display the emotion values and the dominant emotion.
    
    Returns:
        str: Formatted response with emotion values and dominant emotion.
        If no dominant emotion is found, returns an error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    emotion_values = ', '.join(
        [f"'{key}': {value}" for key, value in response.items()
         if key != 'dominant_emotion'])
    dominant_emotion = response['dominant_emotion']
    if dominant_emotion is not None:
        formatted_response = (
            f"For the given statement, the system response is {emotion_values}. "
            f"The dominant emotion is {dominant_emotion}."
        )
        return formatted_response

    return "Invalid text! Please try again!"

if __name__ == '__main__':
    app.run(debug=True, port=5001)
