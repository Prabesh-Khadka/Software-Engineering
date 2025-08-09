class StringManipulator:
#defining to initialize the object and to store     
    def __init__(self, text): 
        self.text = text

#defining function to initialize to find character
    def find_characters(self, char):
        return self.text.find(char)

#defining funtion to find the length of the character
    def find_length(self):
        return  len(self.text)
    
    def convert_upper(self):
        return self.text.upper()

#create an instance of the stringManipulator class 
name = StringManipulator("example")
result1 = name.find_length()
result = name.find_characters('x')
result3 = name.convert_upper()
print(result)
print(result1)
print(result3)