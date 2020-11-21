from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name =  'index'),
    path('user/<int:id>', views.getUserDetails, name='userDetails'), ## Get a user's primary details 
    path('user/<int:id>/hobbies', views.getUserHobies, name='userHobbies'), # Get a user's hobbies
    path('user/<int:id>/skills', views.getUserSkills, name='userTechSkills'), # Get a user's hobbies
    path('user/<int:id>/bio', views.getUserBio, name='userBio'), # Get a user's bio
    path('user/<int:id>/location', views.getUserTimeZoneAndCountry, name= 'userLocation'), # Get a user's location
    path('user/<int:id>/dislikes', views.getUserDislikes, name='userDislikes'), # Get a user's dislikes
    path('skills/all', views.getAllSkills, name='allSkills'), # Get all skills
    path('dislikes/all', views.getAllDislikes, name='allDislikes'), # Get all dislikes
    path('hobbies/all', views.getAllHobbies, name='allHobbies'), # Get all hobbies
    path('hobbies/<int:id>/users', views.getUsersWithSelectedHobby, name='usersWithCurrentHobies'), # Get users with a particular hobby
    path('skills/<int:id>/users', views.getUsersWithSelectedSkill, name='usersWithCurrentSkills'), # Get users with a particular skill
    path('dislikes/<int:id>/users', views.getUsersWithSelectedDislike, name='usersWithCurrentDislike'), # Get users with a particular dislike
    path('user/<int:id>/connectedUsers', views.getConnectedUsers, name='usersWithCurrentSkills'), # Get users connected to current user
    path('user/similar/country/<int:id>', views.getSimilarUsersByCountry, name='similarUsersWithCountry'), # Get users with same country
    path('user/similar/dislike/<int:id>', views.getSimilarUsersByDislikes, name='similarUsersWithDislike'), # Get users with same dislike
    path('hobbies/<str:hobby>/similarUsers', views.searchUsersByHobby, name='usersFromSearchedHobby'), # Get users with indicated hobby
    path('skills/<str:skill>/similarUsers', views.searchUsersByHobby, name='usersFromSearchedHobby'), # Get users with indicated tech skill
    path('country/<str:country>/users', views.searchUsersByCountry, name='usersFromSearchedCountry'), # Get users with indicated country
    path('user/<int:id>/skills/similarUsers', views.getSimilarUsersBySkill, name='similarUsersBySkill'), # Get users related to the current user by skill
    path('user/<int:id>/hobbies/similarUsers', views.getSimilarUsersByHobby, name='similarUsersByHobby'), # Get users related to the current user by hobby
    path('user/<int:id>/bio/similarUsers', views.getSimilarUsersByBio, name='similarUsersByBio'), # Get users related to the current user by bio
]
