class Question:
    def __init__(self,q_text,a_text):
        self.text=q_text
        self.answer=a_text

question1=Question("2+3=5 ??", "True")        

print(question1.answer)