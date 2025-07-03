import unittest
from survey import AnonyomousSurvey

class TestAnonyoumousSurvey(unittest.TestCase):
    """Tests for the class Anonyomous survey"""
    def test_store_single_response(self):
        question = "What language did you first learn to speak? "
        my_survey = AnonyomousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_response(self):
        """Test that three individual responses are stored properly"""
        question = "What language did you learn first? "
        my_survey = AnonyomousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()