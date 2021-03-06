from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from . import models
import json
from neo4j import GraphDatabase
from django.views.decorators.csrf import csrf_exempt

driver = GraphDatabase.driver("bolt://34.224.62.229:32879", auth=("neo4j", "pushup-barge-meetings"))


# Create your views here.
## This function basically retrieves all users
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
                        email=record["email"],
                        password="Confidential").toJSON()

                for record in result
                ]
    # Close the session                
    session.close()
    return HttpResponse(json.dumps(people), content_type='application/json; charset=UTF-8')


## Function to get primary user details <id, name, github name and email address
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
    for record in result:
        person = models.fshipUser(
            id=record["id"], 
            name=record["name"], 
            gitHandle=record["github"], 
            email=record["email"],
            password="Confidential"
        )

    ## Close the session
    session.close()

    return HttpResponse(json.dumps(person.toJSON()), content_type='application/json; charset=UTF-8')

## Get a user's hobbies
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
def getUserTimeZoneAndCountry(request, id):
    ## Start the session
    session = driver.session()
    # Define the query
    query = f"""
    MATCH (u:User) - [:followsTimeZone] -> (tz:Timezone), (u) - [:comesFROM] -> (c:Country)
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


## Return a list of all dislikes, together their frequencies available in the database
def getAllDislikes(request):
    ## Start the session
    session = driver.session()
    # Define the query
    query = f"""
    MATCH (d:Dislike) WITH count(d) AS frequency, d RETURN id(d) AS id, d.description AS dislike, frequency ORDER BY frequency
    """ 

    result = session.run(query) ## Execute the function 
    ## The result is not subsciptible so we loop to get the single value 
    ## Get all skills
    dislikes:list = []
    dislikes = [
        models.Dislike(
            id=record["id"], 
            description=record["dislike"], 
        ).toJSON()
        for record in result
    ]

    ## Close the session
    session.close()

    ## Create a dict with id and hobbies
    response = {
        "dislikes" : dislikes,
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')


## Return a list of all skills, together their frequencies available in the database
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


def getAllCountries(request):
    ## Start the session
    session = driver.session()
    # Define the query
    query = f"""
    MATCH (c:Country) WITH count(c) AS frequency, c 
    RETURN id(c) AS id, c.name AS country, frequency ORDER BY frequency
    """ 

    result = session.run(query) ## Execute the function 
    ## The result is not subsciptible so we loop to get the single value 
    ## Get all skills
    countries:list = []
    countries = [ {"id": record["id"], "country": record["country"]} for record in result ]

    ## Close the session
    session.close()

    ## Create a dict with id and hobbies
    response = countries
    

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')


## Get a list of users who have the selected hobby
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
            password="Confidential",
            email=record["email"]).toJSON()
            for record in result
    ]

    response = {
        "users" : users
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')


## Get a list of users who have the selected dislike
def getUsersWithSelectedDislike(request, id):
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
            password="Confidential",
            email=record["email"]).toJSON()
            for record in result
    ]

    response = {
        "users" : users
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')


## Retrieve users linked to a particular skill
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
            password="Confidential",
            email=record["email"]).toJSON()
            for record in result
    ]

    response = {
        "users" : users
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')


## Get users a user has connected with before, e.g via chat
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
            password="Confidential",
            email=record["email"]).toJSON()
            for record in result
    ]

    response = {
        "users" : users
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')

## Get similar users with the same dislike
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
            password="Confidential",
            email=record["email"]).toJSON()
            for record in result
    ]

    response = {
        "users" : users
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')


## Search users who have a hobby indicated on the search phrase
def searchUsersByHobby(request, hobby):
    ## Start the session
    session = driver.session()
    # Define the query
    query = f"""
    MATCH (u:User) - [:hasHobbie] -> (h:Hobbie)
    WHERE toLower(h.name) = toLower(\"{hobby}\")
    RETURN id(u) AS id, u.name AS name, u.email AS email, u.github AS github
    """ 

    result = session.run(query) ## Execute the function 
    ## The result is not subsciptible so we loop to get the single value 

    users = [
        models.fshipUser(
            id=record["id"], 
            name=record["name"], 
            gitHandle=record["github"], 
            email=record["email"],
            password="Confidential"
            ).toJSON()
            for record in result
    ]

    response = {
        "users" : users
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')


## Search users who have a tech skill indicated by the search phrase
def searchUsersByHobby(request, skill):
    ## Start the session
    session = driver.session()
    # Define the query
    query = f"""
    MATCH (u:User) - [:isInterestedIn] -> (s:TechSkill)
    WHERE toLower(s.name) = toLower(\"{skill}\")
    RETURN id(u) AS id, u.name AS name, u.email AS email, u.github AS github
    """ 

    result = session.run(query) ## Execute the function 
    ## The result is not subsciptible so we loop to get the single value 

    users = [
        models.fshipUser(
            id=record["id"], 
            name=record["name"], 
            gitHandle=record["github"], 
            email=record["email"],
            password="Confidential"
            ).toJSON()
            for record in result
    ]

    response = {
        "users" : users
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')

## Search for users who are from a specific country
def searchUsersByCountry(request, country):
    ## Start the session
    session = driver.session()
    # Define the query
    query = f"""
    MATCH (u:User) - [:comesFrom] -> (c:Country)
    WHERE toLower(c.name) = toLower(\"{country}\")
    RETURN id(u) AS id, u.name AS name, u.email AS email, u.github AS github
    """ 

    result = session.run(query) ## Execute the function 
    ## The result is not subsciptible so we loop to get the single value 

    users = [
        models.fshipUser(
            id=record["id"], 
            name=record["name"], 
            gitHandle=record["github"], 
            password="Confidential",
            email=record["email"],
            ).toJSON()
            for record in result
    ]

    response = {
        "users" : users
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')

## Get users who are most similar to the one whose id you pass
def getSimilarUsersByHobby(request, id):
    ## Start the session
    session = driver.session()
    ## Define the query
    ## This query defines a similarity co-efficient between 0 and 1. Only users with a score
    ## greater that zero are returned, meaning, the current user must share at least one
    ## skill with a user for a user to be returned. The greater the similarity, the higher
    ## the coeffecient. 
    query = f"""
    MATCH (u:User) - [:hasHobbie] -> (h:Hobbie) 
    WHERE id(u) = {id} 
    WITH collect(h) AS hobbies, u 
    MATCH (u1:User) - [has:hasHobbie] -> (h1:Hobbie) 
    WHERE h1 in hobbies AND u<> u1  WITH u1, size(hobbies)
    AS totalHobbies, count(has) AS freq WITH u1, 
    (toFloat(freq)/totalHobbies) AS coef 
    RETURN id(u1) AS id, u1.name AS name, u1.email AS email, u1.github AS github, 
    coef AS similarity_coefficient
    ORDER BY coef DESC
    """ 

    result = session.run(query) ## Execute the function 
    ## The result is not subsciptible so we loop to get the single value 

    similar_users = [
        models.SimilarUser(
            id=record["id"], 
            name=record["name"], 
            gitHandle=record["github"], 
            email=record["email"],
            coefficient = record["similarity_coefficient"]
            ).toJSON()
            for record in result
    ]

    response = {
        "users" : similar_users
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')


## Get users who are most similar to the one whose id you pass
def getSimilarUsersBySkill(request, id):
    ## Start the session
    session = driver.session()
    ## Define the query
    ## This query defines a similarity co-efficient between 0 and 1. Only users with a score
    ## greater that zero are returned, meaning, the current user must share at least one
    ## skill with a user for a user to be returned. The greater the similarity, the higher
    ## the coeffecient. 
    query = f"""
    MATCH (u:User) - [:isInterestedIn] -> (ts:TechSkill)
    WHERE id(u) = {id} 
    WITH collect(ts) AS skills, u 
    MATCH (u1:User) - [has:isInterestedIn] -> (ts1:TechSkill)
    WHERE ts1 in skills 
    AND u<> u1  WITH u1, size(skills) AS totalSkills, 
    count(has) AS freq WITH u1, 
    (toFloat(freq)/totalSkills) AS coef 
    RETURN id(u1) AS id, u1.name AS name, u1.email AS email, u1.github AS github, 
    coef AS similarity_coefficient
    ORDER BY coef DESC
    """ 

    result = session.run(query) ## Execute the function 
    ## The result is not subsciptible so we loop to get the single value 

    similar_users = [
        models.SimilarUser(
            id=record["id"], 
            name=record["name"], 
            gitHandle=record["github"], 
            email=record["email"],
            coefficient = record["similarity_coefficient"]
            ).toJSON()
            for record in result
    ]

    response = {
        "users" : similar_users
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')


## Get users who are most similar to the one whose id you pass
def getSimilarUsersByBio(request, id):
    ## Start the session
    session = driver.session()
    ## Define the query
    ## This query defines a similarity co-efficient between 0 and 1. Only users with a score
    ## greater that zero are returned, meaning, the current user must share at least one
    ## skill with a user for a user to be returned. The greater the similarity, the higher
    ## the coeffecient. 
    query = f"""
        MATCH (u:User) - [:hasBio] -> (b:Bio) 
        WHERE id(u) = {id} 
        MATCH (u1:User) - [:hasBio] -> (b1:Bio)
        WHERE id(u) <> id(u1)
        WITH apoc.text.jaroWinklerDistance(b.description, b1.description)
        AS bio_similarity_coefficient, u1, b1 
        RETURN id(u1) AS id, u1.name AS name, u1.github AS github,
        u1.email AS email, id(b1) AS bio_id, b1.description AS description,
        bio_similarity_coefficient 
        ORDER BY bio_similarity_coefficient DESC
        """ 

    result = session.run(query) ## Execute the function 
    ## The result is not subsciptible so we loop to get the single value 

    similar_users = [
        models.UsersWithSimilarHobbies(
            user= models.fshipUser(
                    id=record["id"], 
                    name=record["name"], 
                    gitHandle=record["github"],
                    password="Confidential",
                    email=record["email"],
            ),
            bio= models.Bio(
                id=record["bio_id"], 
                description=record["description"],
            ),
            coefficient = record["bio_similarity_coefficient"]
            ).toJSON()
            for record in result
        ]

    response = {
        "users" : similar_users
    }

    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')


## Route used to register a new user
"""

{
    "user":{
        "name":"name"
        "email":"email",
        "github" :"github"
        "password":"password"
    },
    "bio" : "bio description",
    "country":"country name",
    "timezone": "timezone",
    "skills": ["skillA","skillB","skillC"],
    "hobbies":["hobbyA","hobbyB","hobbyC"]
    "dislikes" ["dislikeA","dislikeB","dislikeC"]
}
"""


@csrf_exempt
def registerUser(request):
    ## Start the session
    session = driver.session()
    # This query is used to register a new user
    # It accepts the user details, their hobbies, skills, country, bio, timezone and dislikes
    query_builder = """
        MERGE (u:User{email: "%s", github: "%s", password: "%s", name: "%s"})
        WITH u
        MERGE (b:Bio{description: "%s"}) 
        MERGE (u) - [:hasBio] -> (b)
        WITH u
        MERGE (c:Country{name: "%s"})
        MERGE (u) - [:comesFROM] -> (c)
        WITH u
        MERGE (tz:Timezone{tz:"%s"})
        MERGE (u) - [:followsTimeZone] -> (tz)
        WITH u
        UNWIND %s AS skill
        MERGE (ts:TechSkill{name: skill}) 
        MERGE (u) - [:isInterestedIn] -> (ts)
        WITH u
        UNWIND %s AS hobby
        MERGE (h:Hobbie{name:hobby})
        MERGE (u) - [:hasHobbie] -> (h)
        WITH u
        UNWIND %s AS dislike
        MERGE (d:Dislike{description:dislike})
        MERGE (u) - [:dislikes] -> (d)
        WITH u
        RETURN id(u) AS id, u.name AS name, u.password AS password, u.email AS email, u.github AS github
        """
    
    json_body = json.loads(request.body.decode('utf-8'))
    password = json_body["password"]
    email = json_body["email"]
    github = json_body["github"]
    name = json_body["name"]
    bio = json_body["bio"]
    if len(json_body["location"]) > 1:
        country = json_body["location"][0]
        timezone = json_body["location"][1]
    else:
        country = ""
        timezone = ""
    skills = json_body["skills"]
    hobbies = json_body["hobbies"]
    dislikes = json_body["dislikes"]

    query = query_builder % (email,github, password, name,
                    bio,country,timezone,skills,hobbies,dislikes)


    result = session.run(query) ## Execute the query 
    ## The result is not subsciptible so we loop to get the single value

    person: fshipUser = None

    #  ## Get the user details
    User.objects.create(
        username=json_body["github"],
        email=json_body["email"],
        password=json_body["password"]
    )
    for record in result:
        person = models.fshipUser(
            id=record["id"], 
            name=record["name"], 
            gitHandle=record["github"], 
            email=record["email"],
            password=record["password"]
        )

    ## Close the session
    session.close()

    response:dict = {}

    if person is None:
        response = {
            "user" : {}
        }
    else:
        response = {
            "user" : person.toJSON()
        }


    return HttpResponse(json.dumps(response), content_type='application/json; charset=UTF-8')



"""
 Remaining function implementations
 -> connectUser()
 -> getUserConnections()
"""

