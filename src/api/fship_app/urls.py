from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name =  'index'),
    path('user/<int:id>/get', views.getUserDetails, name= 'userDetails'), ## Get a user's primary details 
    path('user/<int:id>/hobbies/get', views.getUserHobies, name= 'userHobbies'), # Get a user's hobbies
    path('user/<int:id>/skills/get', views.getUserSkills, name= 'userTechSkills'), # Get a user's hobbies
    path('user/<int:id>/bio/get', views.getUserBio, name= 'userBio'), # Get a user's bio
    path('user/<int:id>/location/get', views.getUserTimeZoneAndCountry, name= 'userLocation'), # Get a user's location
    path('user/<int:id>/dislikes/get', views.getUserDislikes, name= 'userDislikes'), # Get a user's dislikes
    path('skills/get/all', views.getAllSkills, name= 'allSkills'), # Get all skills
    path('hobbies/get/all', views.getAllHobbies, name= 'allHobbies'), # Get all hobbies
    path('hobbies/<int:id>/users/get', views.getUsersWithSelectedHobby, name= 'usersWithCurrentHobies'), # Get users with a particular hobby
    path('skills/<int:id>/users/get', views.getUsersWithSelectedSkill, name= 'usersWithCurrentSkills'), # Get users with a particular skill
    path('user/<int:id>/connectedUsers/get', views.getConnectedUsers, name= 'usersWithCurrentSkills'), # Get users connected to current user
]


# getUsersWithCurrentHobby