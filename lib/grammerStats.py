class GrammarStats:
    def __init__(self):
        self.correct = []
        self.incorrect = []

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if text == "":
            raise Exception ("No text")
        
        punc_char = '.!?'

    
        if text[0] == text[0].upper() and text[-1] in punc_char:
            self.correct.append(text)
            return True
        else:
            self.incorrect.append(text)
            return False
        

    def percentage_good(self, text_list):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        for text in text_list:
            self.check(text)

        total_texts = len(self.correct) + len(self.incorrect)
        if total_texts == 0:
            return 0

        correct_percentage = len(self.correct)/total_texts * 100
        return f"{int(correct_percentage)}%"
        