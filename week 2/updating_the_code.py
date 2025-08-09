class StringManipulation:
    def find_lenght(self):
        return  len(self.text)
    
    def find_character(self, char):
        return self.text.find(char)
    
    def Convert_upper(self):
        return self.text.upper()
    
name = StringManipulation()
name.text = "example"

result = name.find_character('x')
result1 = name.Convert_upper()
result2 = name.find_lenght()
print(result)
print(result1)
print(result2)