class MyString(object):

    def __init__(self, object=""):
        self.data = object
        
    def __str__(self):
        print(self.data)

    def append(self, text):
        self.data.extend(text)



s = MyString("hi there")
print(s.data)
