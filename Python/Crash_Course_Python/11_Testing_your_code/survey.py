class AnonyomousSurvey:
    """Collect anonymous answers to survey questions"""

    def __init__(self, question):
        self.question = question
        self.responses = []
    
    def show_question(self):
        """Show the survey question"""
        print(self.question)

    def store_response(self, new_response):
        self.responses.append(new_response)
    
    def show_results(self):
        """Show all the  responses that have been given"""
        print("survey results: ")
        for response in self.responses:
            print(f"-{response}")