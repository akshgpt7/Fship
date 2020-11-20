# Fship - (Friend|Fellow)ship
A platform to expand your reach and meet new Fellows outside of your Pod, based off of interests/hobbies/dislikes!


## Adding test data

### Neo4j Queries

To add test data to your Neo4J instance, kindly execute the following queries:

#### Add users
You can copy the entire query and execute it as it is:
```
CREATE (u:User{name:"Frank Sinatra",email:"sinatra@gmail.com",github:"@EmpireState"}) 
CREATE (u1:User{name:"Jane Doe",email:"jane@gmail.com",github:"@Jane"}) 
CREATE (u2:User{name:"John Smith",email:"smith@gmail.com",github:"@Smithson"}) 
CREATE (u3:User{name:"Samuel Chinedu",email:"samuel@gmail.com",github:"@Samuel"}) 
CREATE (u4:User{name:"Utsav Coding",email:"utsav@gmail.com",github:"@Utsav"}) 
CREATE (u5:User{name:"Hillary Osman",email:"hillary@gmail.com",github:"@Hillary"}) 
CREATE (u6:User{name:"Janet Carly",email:"janet@gmail.com",github:"https://github.com/Ochibobo"}) RETURN u1,u2,u3,u4,u5,u6
```

#### Add countries
You can copy the entire query and execute it as it is:
```
CREATE (c:Country{name:"Nigeria"}) 
CREATE (c1:Country{name:"USA"}) 
CREATE (c2:Country{name:"India"}) 
CREATE (c3:Country{name:"Britain"}) RETURN c1,c2,c3,c3
```

#### Add timezones
You can copy the entire query and execute it as it is:
```
CREATE (t:Timezone{tz:"GMT-5"}) 
CREATE (t1:Timezone{tz:"GMT+1"}) 
CREATE (t2:Timezone{tz:"GMT+5.5"}) RETURN t,t1,t2
```

#### Link users to country
Execute one statement at a time. Statements are in different lines.
```
MATCH (u:User) WHERE u.email = "sinatra@gmail.com" MATCH (c:Country) WHERE c.name = "USA" MERGE (u) - [o:comesFROM] -> (c) RETURN u,o,c
MATCH (u:User) WHERE u.email = "jane@gmail.com" MATCH (c:Country) WHERE c.name = "Britain" MERGE (u) - [o:comesFROM] -> (c) RETURN u,o,c
MATCH (u:User) WHERE u.email = "smith@gmail.com" MATCH (c:Country) WHERE c.name = "USA" MERGE (u) - [o:comesFROM] -> (c) RETURN u,o,c
MATCH (u:User) WHERE u.email = "samuel@gmail.com" MATCH (c:Country) WHERE c.name = "Nigeria" MERGE (u) - [o:comesFROM] -> (c) RETURN u,o,c
MATCH (u:User) WHERE u.email = "utsav@gmail.com" MATCH (c:Country) WHERE c.name = "India" MERGE (u) - [o:comesFROM] -> (c) RETURN u,o,c
MATCH (u:User) WHERE u.email = "hillary@gmail.com" MATCH (c:Country) WHERE c.name = "Britain" MERGE (u) - [o:comesFROM] -> (c) RETURN u,o,c
MATCH (u:User) WHERE u.email = "janet@gmail.com" MATCH (c:Country) WHERE c.name = "USA" MERGE (u) - [o:comesFROM] -> (c) RETURN u,o,c
```
#### Create a constraint on user interests
You can copy the entire query and execute it as it is:
```
CREATE CONSTRAINT interest_constraint ON (t:TechSkill) ASSERT t.name IS UNIQUE
```


#### Create user interests
Execute one statement block at a time. Statement blocks are separated by (a) newline(s):
```
MATCH (u:User) WHERE u.email = "sinatra@gmail.com" 
MERGE(t:TechSkill{name:"Dart"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Go"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Java"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Python"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Django"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Flask"}) MERGE (u) - [i:isInterestedIn] -> (t) RETURN u,i,t

MATCH (u:User) WHERE u.email = "jane@gmail.com" 
MERGE(t:TechSkill{name:"HTML"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"CSS"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"VueJS"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Dart"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"NodeJS"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Bootstrap"}) MERGE (u) - [i:isInterestedIn] -> (t) RETURN u,i,t


MATCH (u:User) WHERE u.email = "smith@gmail.com" 
MERGE(t:TechSkill{name:"Django"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Neo4j"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Php"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Laravel"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Devops"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"NodeJS"}) MERGE (u) - [i:isInterestedIn] -> (t) RETURN u,i,t


MATCH (u:User) WHERE u.email = "samuel@gmail.com" 
MERGE(t:TechSkill{name:"Tensorflow"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Python"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"R"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Julia"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Neo4J"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Php"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Matplotlib"}) MERGE (u) - [i:isInterestedIn] -> (t) RETURN u,i,t


MATCH (u:User) WHERE u.email = "utsav@gmail.com" 
MERGE(t:TechSkill{name:"Python"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Flask"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"VueJS"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Django"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Tensorflow"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Matplotlib"}) MERGE (u) - [i:isInterestedIn] -> (t) RETURN u,i,t


MATCH (u:User) WHERE u.email = "hillary@gmail.com" 
MERGE(t:TechSkill{name:"Go"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Java"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"CSS"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"NodeJS"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Django"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"MySQL"}) MERGE (u) - [i:isInterestedIn] -> (t) RETURN u,i,t


MATCH (u:User) WHERE u.email = "janet@gmail.com" 
MERGE(t:TechSkill{name:"Matplotlib"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Dart"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Flutter"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Android"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Swift"}) MERGE (u) - [i:isInterestedIn] -> (t) WITH u
MERGE(t:TechSkill{name:"Java"}) MERGE (u) - [i:isInterestedIn] -> (t) RETURN u,i,t
```

#### Link users to timezones
Execute one statement-block at a time. Statements are separated by new a newline.
```
MATCH (u:User) WHERE u.email IN ["sinatra@gmail.com","janet@gmail.com","smith@gmail.com"]
MATCH (tz:Timezone) WHERE tz.tz = "GMT-5" MERGE (u) - [f:followsTimeZone] -> (tz) RETURN u,f,tz

MATCH (u:User) WHERE u.email IN ["hillary@gmail.com","jane@gmail.com","samuel@gmail.com"]
MATCH (tz:Timezone) WHERE tz.tz = "GMT+1" MERGE (u) - [f:followsTimeZone] -> (tz) RETURN u,f,t

MATCH (u:User) WHERE u.email IN ["utsav@gmail.com"]
MATCH (tz:Timezone) WHERE tz.tz = "GMT+5.5" MERGE (u) - [f:followsTimeZone] -> (tz) RETURN u,f,t
```

#### Create user hobbies
Execute one statement block at a time. Statement blocks are separated by (a) newline(s):
```
MATCH (u:User) WHERE u.email = "sinatra@gmail.com"
MERGE (ho:Hobbie{name:"Cycling"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Baking"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Hiking"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Reading"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Kayaking"}) MERGE (u) - [h:hasHobbie] -> (ho) RETURN u,h, ho


MATCH (u:User) WHERE u.email = "jane@gmail.com"
MERGE (ho:Hobbie{name:"Cycling"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Playing Ukelele"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Travelling"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Singing"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Blogging"}) MERGE (u) - [h:hasHobbie] -> (ho) RETURN u,h, ho


MATCH (u:User) WHERE u.email = "smith@gmail.com"
MERGE (ho:Hobbie{name:"Bowling"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Ice Skating"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Travelling"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Astrology"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Weaving"}) MERGE (u) - [h:hasHobbie] -> (ho) RETURN u,h, ho


MATCH (u:User) WHERE u.email = "samuel@gmail.com"
MERGE (ho:Hobbie{name:"Baseball"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Ice Skating"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Travelling"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Basketball"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Kayaking"}) MERGE (u) - [h:hasHobbie] -> (ho) RETURN u,h, ho


MATCH (u:User) WHERE u.email = "utsav@gmail.com"
MERGE (ho:Hobbie{name:"Cycling"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Jogging"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Soccer"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Snowboarding"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Singing"}) MERGE (u) - [h:hasHobbie] -> (ho) RETURN u,h, ho


MATCH (u:User) WHERE u.email = "hillary@gmail.com"
MERGE (ho:Hobbie{name:"Hunting"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Jogging"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Basketball"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Playing Ukelele"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Travelling"}) MERGE (u) - [h:hasHobbie] -> (ho) RETURN u,h, ho


MATCH (u:User) WHERE u.email = "janet@gmail.com"
MERGE (ho:Hobbie{name:"Videography"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Rafting"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Canoeing"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Playing Ukelele"}) MERGE (u) - [h:hasHobbie] -> (ho) WITH u
MERGE (ho:Hobbie{name:"Travelling"}) MERGE (u) - [h:hasHobbie] -> (ho) RETURN u,h, ho
```

#### Create user bio
Execute one statement block at a time. Statement blocks are separated by (a) newline(s):
Prior to executing, ensure that each bio description is within one string body. You may have to make the queries appear on a straight line (but the cypher query 
window will format them otherwise).
```
MATCH (u:User) WHERE u.email = "sinatra@gmail.com"
MERGE (u) - [:hasBio] -> (b:Bio{description:"I started tinkering with electronics as a kid 
        alongside my father who had a PhD in Electrical Engineering from Stanford University. 
        In those days we had a den set up with a wide assortment of test equipment. 
        I never grew tired of working with oscilloscopes, variable frequency generators, 
        frequency counters, variable power supplies, breadboards,
        logic probes, digital and analog meters, capacitor and transistor testers, and soldering equipment"}) 

MATCH (u:User) WHERE u.email = "jane@gmail.com"
MERGE (u) - [:hasBio] -> (b:Bio{description:"I earned a Bachelor’s degree in Mechanical Engineering, 
        and then a Master’s degree in Electrical Engineering from the
        University of California Santa Barbara. While attending UCSB, 
        I began my software engineering career as a VMS Systems Programmer 
        for General Research Corporation, holding a secret security clearance. 
        There I became one of the divisions top programmers, updating device drivers, 
        writing the EDX Editor which became very popular, and earning steady recognition 
        for outstanding contributions."}) 

MATCH (u:User) WHERE u.email = "smith@gmail.com"
MERGE (u) - [:hasBio] -> (b:Bio{description:"I spent eight years as a VMS Systems Programmer writing 
        and maintaining their manufacturing execution software applications. 
        In this position I wrote, maintained and upgraded a database program 
        for tracking wafer defects that transformed and reduced defect tracking 
        time from 5 minutes to 10 seconds."}) 

MATCH (u:User) WHERE u.email = "samuel@gmail.com"
MERGE (u) - [:hasBio] -> (b:Bio{description:"I find the field of software engineering enormously rewarding 
        and I am excited to be a part of it. Originally we wrote procedural 
        code and created code libraries. Today, we create OOP programs using 
        OOAD principles and UML diagrams, following the SOLID and DRY principles 
        of good software design"}) 

MATCH (u:User) WHERE u.email = "utsav@gmail.com"
MERGE (u) - [:hasBio] -> (b:Bio{description:"Professionally, my primary languages are C#, VB.NET, Java, SQL, 
        C, C++, HTML, JavaScript, Assembly Language, Perl, and Python, 
        using Visual Studio and Eclipse."}) 

MATCH (u:User) WHERE u.email = "hillary@gmail.com"
MERGE (u) - [:hasBio] -> (b:Bio{description:"I never grew tired of working with oscilloscopes, variable frequency 
         generators, frequency counters, variable power supplies, breadboards, 
         logic probes, digital and analog meters, capacitor and transistor testers, 
         and soldering equipment."}) 

MATCH (u:User) WHERE u.email = "janet@gmail.com"
MERGE (u) - [:hasBio] -> (b:Bio{description:" I was involved in pioneering research at the UCSB Institute For Collaborative 
         Biotechnologies. There I designed and coded an Artificial Pancreas System 
         for type 1 diabetics that connected an insulin pump with a continuous glucose 
         monitor via a software feedback loop."})
```

**Finally, for the Neo4J project, add the APOC plugin which we use to calculate the similarity in Bios. Instructions on how to do this can be found (here)[https://neo4j.com/developer/neo4j-apoc/].
