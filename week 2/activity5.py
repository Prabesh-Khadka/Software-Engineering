class StringSentence:
    def __init__(self, word):
        self.word = word
    
    def find_length(self):
        return len(self.word)
    
    def word_count(self):
        word = self.word.split()
        return len(word)
    
    def main():        
        user_input = input("Enter the sentence: ")
        sentence = StringSentence(user_input)
        print("You have Entered: ", user_input)
#        round_sentence = round(sentence)
        print(user_input)
        print("The letter of the word is:", sentence.find_length())
        print("The no of words typed is:", sentence.word_count())

if __name__ == "__main__":
    StringSentence.main()
