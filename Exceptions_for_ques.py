class InvalidChoice(Exception):
    def __init__(self,value):
                super().__init__(f"Invalid choice {value}.Choice must be number")

class InvalidAnsError(Exception):
    def __init__(self, ans):
        super().__init__(f"Invalid ans: {ans}.Ans must be a number.")
