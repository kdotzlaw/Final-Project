from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        res = emotion_detector("I am glad this happened")
        self.assertEqual(res['dominant_emotion'],'joy')

        res = emotion_detector("I am really mad about this")
        self.assertEqual(res['dominant_emotion'],'anger')

        res = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(res['dominant_emotion'],'disgust')

        res = emotion_detector("I am so sad about this")
        self.assertEqual(res['dominant_emotion'],'sadness')

        res = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(res['dominant_emotion'],'fear')
    
unittest.main()