#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs:
                if key != __class__:
                    setattr(self, key, value)
            if created_at and updated_at in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
                self.updated_at = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid4())


    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        """A function to collect the needed data and put them into dic
        by making a copy of __dict__ using {**self}"""
        
        temp = {**self.__dict__}
        temp["created_at"] = self.created_at.isoformat()
        temp["updated_at"] = self.updated_at.isoformat()
        temp["__class__"] = type(self).__name__
        return temp
    def __str__(self):
        """overriding the __str__ method to print specific format"""
        return "[{}] ({}) {}".format(type(self).__name__,self.id, self.__dict__)

my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)