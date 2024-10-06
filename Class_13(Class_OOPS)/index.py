class Teacher():
    def __init__(self,teacher_id:int,teacher_name:str) -> None:   # method
        self.name : str = teacher_name
        self.teacher_id : int = teacher_id 
        self.organization : str = "PIAIC"
    def speak(self,words:str)-> None:
        print(f"{self.name} is speaking the words {words}")
    
    def teaching(self,subject:str)-> None:
        print(f"{self.name} is teaching the subject {subject}")
        
obj1 : Teacher = Teacher(1,"muhammad")
obj2 : Teacher = Teacher(2,"ahmad")
print(obj1.name)
print(obj2.name)

obj1.teaching("gen AI")
obj2.teaching("AI")