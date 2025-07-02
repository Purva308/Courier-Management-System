class InvalidEmployeeIdException(Exception):
    def __init__(self,message="Invalid Employee ID ."):
        super().__init__(message)