import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_joy(self):
        self.assertEqual(emotion_detector("I am happy")['dominant_emotion'], 'joy')

    def test_anger(self):
        self.assertEqual(emotion_detector("I am angry")['dominant_emotion'], 'anger')

if __name__ == "__main__":
    unittest.main()