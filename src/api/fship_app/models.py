from django.db import models

# Create your models here.
## Models made specifically for Neo4J
class FShipUser:

    ## Initialize this object
    def __init__(self, id:int, name:str, gitHandle:str, email:str):
        self.id = id
        self.name = name
        self.gitHandle = gitHandle
        self.email = email
            
    ## Return a dict version of the object for easy serialization
    def toJSON(self):
        return self.__dict__

## Model to store a hobby
class Hobby:
    
    ## Initialize a user's hobby
    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name
            
    ## Return a dict version of the object for easy serialization
    def toJSON(self):
        return self.__dict__

## Model to store a tech skill
class TechSkill:
    
    ## Initialize a user's hobby
    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name
            
    ## Return a dict version of the object for easy serialization
    def toJSON(self):
        return self.__dict__

## Model to store a user's bio
class Bio:
    
    ## Initialize a user's hobby
    def __init__(self, id:int, description:str):
        self.id = id
        self.description = description
            
    ## Return a dict version of the object for easy serialization
    def toJSON(self):
        return self.__dict__

## Model to store a user's country and timezone
class Location:
    
    ## Initialize a user's hobby
    def __init__(self, timezoneID:int, timezone:str, countryID:int, country:str):
        self.timezoneID = timezoneID
        self.timezone = timezone
        self.countryID = countryID
        self.country = country
            
    ## Return a dict version of the object for easy serialization
    def toJSON(self):
        return self.__dict__


## Model to store a user's dislikes
class Dislike:
    
    ## Initialize a user's hobby
    def __init__(self, id:int, description:str):
        self.id = id
        self.description = description
            
    ## Return a dict version of the object for easy serialization
    def toJSON(self):
        return self.__dict__


## TechSkill with frequency
## Inherit properties from TechSkill
class TechSkillWithFrequency(TechSkill):    

    def __init__(self, frequency: int, **kwargs):
        super(TechSkillWithFrequency, self).__init__(**kwargs)
        self.frequency = frequency
    
    def toJSON(self):
        skillDict = {}
        skillDict.update(self.__dict__)
        skillDict.update(super().toJSON())
        return skillDict


## Hobbies with frequency
## Inherit properties from Hobby
class HobbyWithFrequency(Hobby):

    def __init__(self, frequency: int, **kwargs):
        super(HobbyWithFrequency, self).__init__(**kwargs)
        self.frequency = frequency

    def toJSON(self):
        hobbyDict = {}
        hobbyDict.update(self.__dict__)
        hobbyDict.update(super().toJSON())
        return hobbyDict


## A user who's had connections with other users
## Inherit from FShipUser
class UserWithConnections(FShipUser):

    def __init__(self, date: str, **kwargs):
        super(UserWithConnections, self).__init__(**kwargs)
        self.date = date

    def toJSON(self):
        hobbyDict = {}
        hobbyDict.update(self.__dict__)
        hobbyDict.update(super().toJSON())
        return hobbyDict


