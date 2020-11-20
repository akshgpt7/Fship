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
    path('user/similar/country/<int:id>', views.getSimilarUsersByCountry, name= 'similarUsersWithCountry'), # Get users with same country
    path('user/similar/dislike/<int:id>', views.getSimilarUsersByDislikes, name= 'similarUsersWithDislike'), # Get users with same dislike
    path('hobbies/<str:hobby>/similarUsers/get', views.searchUsersByHobby, name= 'usersFromSearchedHobby'), # Get users with indicated hobby
    path('skills/<str:skill>/similarUsers/get', views.searchUsersByHobby, name= 'usersFromSearchedHobby'), # Get users with indicated tech skill
    path('country/<str:country>/users/get', views.searchUsersByCountry, name= 'usersFromSearchedCountry'), # Get users with indicated country
    path('user/<int:id>/skills/similarUsers/get', views.getSimilarUsersBySkill, name= 'similarUsersBySkill'), # Get users related to the current user by skill
    path('user/<int:id>/hobbies/similarUsers/get', views.getSimilarUsersByHobby, name= 'similarUsersByHobby'), # Get users related to the current user by hobby
    path('user/<int:id>/bio/similarUsers/get', views.getSimilarUsersByBio, name= 'similarUsersByBio'), # Get users related to the current user by bio
]
