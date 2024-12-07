import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def tests(self):
        cases = {'I am glad this happened': 'joy', 'I am really mad about this': 'anger', 'I feel disgusted just hearing about this': 'disgust', 'I am so sad about this': 'sadness', 'I am really afraid that this will happen': 'fear'}

        for test_input, expected_output in cases.items():
            self.assertEqual(emotion_detector(test_input)['dominant_emotion'], expected_output)
    

unittest.main()