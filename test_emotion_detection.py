import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_emotion_not_none(self):
        result = emotion_detector("I am happy")
        self.assertIsNotNone(result['dominant_emotion'])

    def test_keys_exist(self):
        result = emotion_detector("I am happy")
        self.assertIn('anger', result)
        self.assertIn('joy', result)
        self.assertIn('sadness', result)
        self.assertIn('fear', result)
        self.assertIn('disgust', result)
        self.assertIn('dominant_emotion', result)

    def test_output_type(self):
        result = emotion_detector("I am happy")
        self.assertIsInstance(result, dict)

if __name__ == "__main__":
    unittest.main()
