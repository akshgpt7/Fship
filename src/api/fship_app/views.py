from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from . import models
import json
from neo4j import GraphDatabase

driver = GraphDatabase.driver("bolt://34.224.62.229:32769", auth=("neo4j", "auditors-crust-topic"))

# Create your views here.
## This function basically retrieves all users
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def index(request):
    ## Start the session
    session = driver.session()
    # Define the query
    query = "MATCH (u:User) RETURN id(u) AS id, u.name AS name, u.github AS github, u.email AS email"
    # Execute the query
    result = session.run(query)
    ## Fetch users 
    people = [models.fshipUser(
                        id=record["id"], 
                        name=record["name"], 
                        gitHandle=record["github"], 
                        email=record["email"]).toJSON()
                for record in result
                ]
    # Close the session                
    session.close()
    return HttpResponse(json.dumps(people), content_type='application/json; charset=UTF-8')


## Function to get primary user details <id, name, github name and email address
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def getUserDetails(request, id):
    ## Start the session
    session = driver.session()
    # Define the query
    query = f"""
    MATCH (u:User) WHERE id(u) = {id}
    RETURN id(u) AS id, u.name AS name, u.github AS github, u.email AS email
    """

    result = session.run(query) ## Execute the function 
    ## The result is not subsciptible so we loop to get the single value 
    ## Get the user details
    ## The 
    for record in result:
        person = models.fshipUser(
            id=record["id"], 
            name=record["name"], 
            gitHandle=record["github"], 
            email=record["email"]
        )

    ## Close the session
    session.close()

    return HttpResponse(json.dumps(person.toJSON()), content_type='application/json; charset=UTF-8')

## Get a user's hobbies
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def getUserHobies(request, id):
    ## Start the session
    session = driver.session()
    # Define the query
    query = f"""
    MATCH (u:User) - [:hasHobbie] -> (h:Hobbie) WHERE id(u) = {id} 
    RETURN id(h) AS id, h.name AS hobby
    """

    result = session.run(query) ## Execute the function 
    ## The result is not subsciptible so we loop to get the single value 
    ## Get the user details
    hobbies = [
        models.Hobby(
            id=record["id"], 
            name=record["hobby"], 
        ).toJSON()
        for record in result
    ]
    ## Close the session
    session.close()

    ## Create a dict with id and hobbies
    response = {
        "user_id" : id,
        "hobbies" : hobbies,
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def getUserSkills(request, id):
    ## Start the session
    session = driver.session()
    # Define the query
    query = f"""
    MATCH (u:User) - [:isInterestedIn] -> (s:TechSkill) WHERE id(u) = {id} 
    RETURN id(s) AS id, s.name AS skill
    """ 

    result = session.run(query) ## Execute the function 
    ## The result is not subsciptible so we loop to get the single value 
    ## Get the user details
    skills = [
        models.TechSkill(
            id=record["id"], 
            name=record["skill"], 
        ).toJSON()
        for record in result
    ]
    ## Close the session
    session.close()

    ## Create a dict with id and hobbies
    response = {
        "user_id" : id,
        "skills" : skills,
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')


# Function to get a user's bio
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def getUserBio(request, id):
    ## Start the session
    session = driver.session()
    # Define the query
    query = f"""
    MATCH (u:User) - [:hasBio] -> (b:Bio) WHERE id(u) = {id} RETURN id(b) AS id, 
    b.description AS description
    """ 

    result = session.run(query) ## Execute the function 
    ## The result is not subsciptible so we loop to get the single value 
    ## Get the user details
    for record in result:
        bio = models.Bio(
            id=record["id"], 
            description=record["description"], 
        ).toJSON()

    ## Close the session
    session.close()

    ## Create a dict with id and hobbies
    response = {
        "user_id" : id,
        "bio" : bio,
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')


## Function to get a user's country and timeZone
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def getUserTimeZoneAndCountry(request, id):
    ## Start the session
    session = driver.session()
    # Define the query
    query = f"""
    MATCH (u:User) - [:followsTimeZone] -> (tz:Timezone), (u) - [:comesFrom] -> (c:Country)
    WHERE id(u) = {id}
    RETURN id(tz) AS timezoneID, tz.tz AS timezone,id(c) AS countryID, c.name AS country
    """ 

    result = session.run(query) ## Execute the function 
    ## The result is not subsciptible so we loop to get the single value 
    ## Get the user details
    for record in result:
        location = models.Location(
            timezoneID=record["timezoneID"], 
            timezone=record["timezone"], 
            countryID=record["countryID"], 
            country=record["country"], 
        ).toJSON()

    ## Close the session
    session.close()

    ## Create a dict with id and hobbies
    response = {
        "user_id" : id,
        "location" : location,
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')


## Get a user's dislikes
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def getUserDislikes(request, id):
    ## Start the session
    session = driver.session()
    # Define the query
    query = f"""
    MATCH (u:User) - [:dislikes] -> (d:Dislike) 
    WHERE id(u) = {id}
    RETURN id(d) AS id, d.description AS description
    """ 

    result = session.run(query) ## Execute the function 
    ## The result is not subsciptible so we loop to get the single value 
    ## Get the user details
    dislikes = [
        models.Dislike(
            id=record["id"], 
            description=record["description"], 
        ).toJSON()
        for record in result
    ]
    ## Close the session
    session.close()

    ## Create a dict with id and hobbies
    response = {
        "user_id" : id,
        "dislikes" : dislikes,
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')


## Return a list of all skills, together their frequencies available in the database
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def getAllSkills(request):
    ## Start the session
    session = driver.session()
    # Define the query
    query = f"""
    MATCH (t:TechSkill) WITH count(t) AS frequency, t 
    RETURN id(t) AS id, t.name AS skill, frequency ORDER BY frequency
    """ 

    result = session.run(query) ## Execute the function 
    ## The result is not subsciptible so we loop to get the single value 
    ## Get all skills
    skills:list = []
    skills = [
        models.TechSkillWithFrequency(
            id=record["id"], 
            name=record["skill"], 
            frequency=record["frequency"],
        ).toJSON()
        for record in result
    ]

    ## Close the session
    session.close()

    ## Create a dict with id and hobbies
    response = {
        "skills" : skills,
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')

## Return a list of all skills, together their frequencies available in the database
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def getAllHobbies(request):
    ## Start the session
    session = driver.session()
    # Define the query
    query = f"""
    MATCH (h:Hobbie) WITH COUNT(h) AS frequency, h
    RETURN id(h) AS id, h.name AS hobby, frequency ORDER BY frequency
    """ 

    result = session.run(query) ## Execute the function 
    ## The result is not subsciptible so we loop to get the single value 
    ## Get all skills
    hobbies:list = []
    hobbies = [
        models.HobbyWithFrequency(
            id=record["id"], 
            name=record["hobby"], 
            frequency=record["frequency"],
        ).toJSON()
        for record in result
    ]

    ## Close the session
    session.close()

    ## Create a dict with id and hobbies
    response = {
        "hobbies" : hobbies,
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')


## Get a list of users who have the selected hobby
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def getUsersWithSelectedHobby(request, id):
     ## Start the session
    session = driver.session()
    # Define the query
    query = f"""
    MATCH (u:User) - [:hasHobbie] -> (h:Hobbie) 
    WHERE id(h) = {id} 
    RETURN id(u) AS id, u.name AS name, u.email AS email, u.github AS github
    """ 

    result = session.run(query) ## Execute the function 
    ## The result is not subsciptible so we loop to get the single value 

    users = [
        models.fshipUser(
            id=record["id"], 
            name=record["name"], 
            gitHandle=record["github"], 
            email=record["email"]).toJSON()
            for record in result
    ]

    response = {
        "users" : users
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')

## Retrieve users linked to a particular skill
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def getUsersWithSelectedSkill(request, id):
    ## Start the session
    session = driver.session()
    # Define the query
    query = f"""
    MATCH (u:User) - [:isInterestedIn] -> (s:TechSkill) 
    WHERE id(s) = {id} 
    RETURN id(u) AS id, u.name AS name, u.email AS email, u.github AS github
    """ 

    result = session.run(query) ## Execute the function 
    ## The result is not subsciptible so we loop to get the single value 

    users = [
        models.fshipUser(
            id=record["id"], 
            name=record["name"], 
            gitHandle=record["github"], 
            email=record["email"]).toJSON()
            for record in result
    ]

    response = {
        "users" : users
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')


## Get users a user has connected with before, e.g via chat
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def getConnectedUsers(request, id):
    ## Start the session
    session = driver.session()
    # Define the query
    query = f"""
    MATCH (u:User) - [c:connectedWith] - (u2:User)
    WHERE id(u) = {id}
    RETURN toString(c.date) AS connectionDate, id(u2) AS id, u2.name AS name, 
    u2.email AS email, u2.github AS github
    """ 

    result = session.run(query) ## Execute the function 
    ## The result is not subsciptible so we loop to get the single value 

    users = [
        models.UserWithConnections(
            id=record["id"], 
            name=record["name"], 
            gitHandle=record["github"], 
            email=record["email"],
            date=record["connectionDate"]
            ).toJSON()
            for record in result
    ]

    response = {
        "users" : users
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')

## Get similar users from the same country
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def getSimilarUsersByCountry(request, id):
    ## Start the session
    session = driver.session()
    # Define the query
    query = f"""
    MATCH (u:User) - [:comesFROM] -> (c:Country) 
    WHERE id(c) = {id} 
    RETURN id(u) AS id, u.name AS name, u.email AS email, u.github AS github
    """ 

    result = session.run(query) ## Execute the function 
    ## The result is not subsciptible so we loop to get the single value 

    users = [
        models.fshipUser(
            id=record["id"], 
            name=record["name"], 
            gitHandle=record["github"], 
            email=record["email"]).toJSON()
            for record in result
    ]

    response = {
        "users" : users
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')

## Get similar users with the same bio
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def getSimilarUsersByBio(request, id):
    ## Start the session
    session = driver.session()
    # Define the query
    query = f"""
    MATCH (u:User) - [:hasBio] -> (b:Bio) 
    WHERE id(b) = {id} 
    RETURN id(u) AS id, u.name AS name, u.email AS email, u.github AS github
    """ 

    result = session.run(query) ## Execute the function 
    ## The result is not subsciptible so we loop to get the single value 

    users = [
        models.fshipUser(
            id=record["id"], 
            name=record["name"], 
            gitHandle=record["github"], 
            email=record["email"]).toJSON()
            for record in result
    ]

    response = {
        "users" : users
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')

## Get similar users with the same dislike
@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def getSimilarUsersByDislikes(request, id):
    ## Start the session
    session = driver.session()
    # Define the query
    query = f"""
    MATCH (u:User) - [:dislikes] -> (d:Dislike) 
    WHERE id(d) = {id} 
    RETURN id(u) AS id, u.name AS name, u.email AS email, u.github AS github
    """ 

    result = session.run(query) ## Execute the function 
    ## The result is not subsciptible so we loop to get the single value 

    users = [
        models.fshipUser(
            id=record["id"], 
            name=record["name"], 
            gitHandle=record["github"], 
            email=record["email"]).toJSON()
            for record in result
    ]

    response = {
        "users" : users
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')


"""
 Remaining function implementations
 -> registerUser()
 -> getSimilarUsers()
 -> getSimilarUsersByCountry()
 -> getSimilarUsersBySkill()
 -> getSimilarUsersByHobby()
 -> getSimilarUsersByBio()
 -> getSimilarUsersByDislikes()
"""
