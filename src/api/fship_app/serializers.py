from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import fshipUser
from .views import driver


class CustomJWTSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        credentials = {
            'username': '',
            'password': attrs.get("password")
        }

        session = driver.session()

        query = f"""
        MATCH (u:User) WHERE u.github = \"{attrs.get("username")}\" AND u.password = \"{attrs.get("password")}\"
        RETURN id(u) AS id, u.github AS github
        """

        result = session.run(query)
        people = [[record["id"], record["github"]] for record in result]
        print(people)

        session.close()

        if people and len(people) >= 1:
            username = people[0][1]
            credentials['username'] = str(username)
            return super().validate(credentials)
        else:
            return {'token': None}

