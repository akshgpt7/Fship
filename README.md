<div align="center">

# Fship

**(Friend|Fellow)ship**

---

</div>

## :ledger: Contents
- [About](#beginner-about)
  - [Technologies Used](#technologies-used)
- [Development Setup](#electric_plug-development-setup)
  - [Django server and virtual environment setup](#django-server-and-virtual-environment-setup)
  - [Neo4j database setup](#neo4j-database-setup)
  - [Frontend setup](#frontend-setup)
- [Usage](#zap-usage)

## :beginner: About
*A platform to expand your reach and meet new Fellows outside of your Pod!*<br>
A major goal of the MLH Fellowship is to expand your network and make wonderful friends. It becomes hard to reach out to people outside of your Pod, mainly because we know so less about the likes/dislikes/technical interests of other Fellows.<br>
**Fship** aims to bridge that gap by letting a Fellow find other like-minded Fellows and make Friends!

### Technologies Used
#### Backend (REST API)
 - Django
 - Django REST Framework (only for JWT authentication)
 - Neo4j (Graph database)
 
#### Frontend
 - Vue.js
 - UIkit

## :electric_plug: Development Setup

### Django server and virtual environment setup
1. Clone this repository by running `git clone https://github.com/akshgpt7/Fship`.
2. Make sure you have `pipenv` installed on your system. If not, do it by `pip install pipenv`.
3. cd to the API directory by `cd Fship/src/api`.
4. To activate a virtual environment for the project, run `pipenv shell`. After this, you'll be inside the virtual environment.
5. Install the dependencies by running `pipenv install`.
6. Run Django migrations by `python3 manage.py makemigrations` and then `python3 manage.py migrate`.
7. Setup the Neo4j databse from the next section.
8. Run `python3 manage.py runserver` to run the API server.

### Neo4j database setup
To get started with setting up __Neo4j__ on your Desktop:
* Make sure you have Java installed on your Machine and that the `_JAVA_HOME_` path is set.
* Download Neo4j from [here](https://neo4j.com/download/) and install it on your local machine.

However, if you don't want to download Neo4j locally on your machine, you can create an account for the Neo4j Sandbox, which is more of a free online Neo4j Database instance for about 10 Days. There will be no difference in how we utilise the Desktop version from how one may use the SandBox for our project. You can get started with the Sandbox [here](https://neo4j.com/sandbox/).

Now that you have __Neo4j__ set up, our project uses the official Neo4j Driver to communicate for communication between Neo4j and the Django project over the [Bolt protocol](https://en.wikipedia.org/wiki/Bolt_(network_protocol)). To install the driver, run this command in your pipenv virtual environment:

```
pipenv install neo4j
```

Now that you have your environment set up, open your Neo4j Application (if desktop) and follow [these](https://neo4j.com/developer/neo4j-desktop/) instructions to create a new database. If you are using the sandbox account, this is a good [blog](https://neo4j.com/blog/graphcast-neo4j-sandbox-quick-start-guide/) to help you get started. You will be asked to create a username and a password. Make sure you remember these as they will be very useful when connecting the Django project to the Neo4J database over the Neo4J Driver.

Once you have a new database created, start it and open the Neo4j browser (as instructions in the previous paragraph have shown you).

The following __cypher__ queries can help you get started (**Note: Replace all IDs by the actual id**):
Create User
```
CREATE (u:User{name:"John Smith",email:"johnsmith@gmail.com",password:"testing321",github:"https://github.com/JohnSmith"}) RETURN u
``` 
If all goes well, the above query should return a node. 

Now, to get the user id, which will be essential for the rest of the queries, do the following:
```
MATCH (u:User) RETURN id(u)
``` 
Notice that the id here is generated by Neo4j. The following queries depend on it. Let's call it _userID_. Any occurence of _userID_ in the following queries ought to be replaced by the exact integral id returned by the **MATCH** cypher query we executed above.
**Let's create some dummy data now to test out our endpoints.**

Create a country (You can choose any country name)
```
CREATE (c:Country{name:"Kenya"}) RETURN c
```

Create a timezone (You can choose any time-zone)
```
CREATE (t:Timezone{tz:"GMT+3"}) RETURN t
```

Both queries above should return nodes that should appear as circles on your Neo4j browser. 

Create a user bio (you can enter any text in the quotation marks present in the description)
```
MATCH (u:User) WHERE id(u) = userID MERGE (u) - [h:hasBio] -> (b:Bio{description:""}) RETURN u,h,b
```

Link John Smith, our create user, to the country and timezone we created:

```
MATCH (u:User) WHERE id(u) = userID MATCH (c:Country) WHERE id(c) = countryID MERGE (u) - [o:comesFROM] -> (c) RETURN u,o,c
```

```
MATCH (u:User) WHERE id(u) = 0 MATCH (tz:Timezone) WHERE id(tz) = timezoneID MERGE (u) - [f:followsTimeZone] -> (tz) RETURN u,f,tz
```

To get the countryID and timezoneID, you may press on the nodes that represent them and read their id values, which will be displayed at the bottom of that active window.

Next, create the user's interests - You can replace the the value of the tech skill name ("Go") with other values and run the query multiple times to create multiple skills.
```
MATCH (u:User) WHERE id(u) = userID MERGE (u) - [i:isInterestedIn] -> (t:TechSkill{name:"Go"}) RETURN u,i,t
```

Next, create the user's hobbies - You can replace the the value of the tech hobby name ("Cycling") with other values and run the query multiple times to create multiple hobbies.
```
MATCH (u:User) WHERE id(u) = userID MERGE (u) - [h:hasHobbie] -> (ho:Hobbie{name:"Cycling"}) RETURN u,h,ho
```

Create a user's dislike
```
MATCH (u:User) WHERE id(u) = userID MERGE (u) - [di:dislikes] -> (d:Dislike{description:"Going to Uni"}) RETURN u, di, d
```

To get a glimpse of how your graph looks like now, run the following:
```
MATCH (n) RETURN n
```
You should expect to see a graph, with nodes connected to a central node (the user).

**Congratulations**. Let's proceed to how you'll link it to the Django webserver.

- Navigate to `Fship/src/api/fship_app/views.py`. At the top, you will see the following line of code:
```
driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("user", "password"))
```
- If you are using a Desktop instance of Neo4j, all you have to do is replace the _user_ and _password_ fields with the username and password you used when creating the database. However, if you also changed the port, feel free to replace 7687 with your target port.

- If you are using Neo4J Snadbox, you have to replace the entire _neo4j://localhost:7687_ with the URL provided to you on the sandbox. Furthermore, replace the _user_ and _password_ fields with the username and password you used when creating the database.

- You can now navigate to `urls.py` file and use the routes to test the data you added to you Neo4J instance.

### Frontend setup
1. Make sure you have `npm` installed on your system. If not, [this](https://www.npmjs.com/get-npm) might help.
2. Navigate to the `src/frontend/frontend-fship` directory.
3. Install dependencies by `npm install`.
4. Run the dev server by `npm run serve`.
5. Head to `localhost:8080` in your browser to see the web app.

## :zap: Usage
A new user registers and adds their information, hobbies, technical skills, dislikes (things they'd love to rant about) to their profile. <br>
Different users can then either view all the registered Fellows, or filter them by various categories. Once they find a relatable Fellow, they can press the "Connect" button for that Fellow, to send them an Email, with an auto-generated custom Jitsi meeting link by us to talk to them! 

