from django.urls import path
from . import views
from .views_all import accountsView, careGiverView, careHomeView

urlpatterns = [
    # path('WelcomePage', views.WelcomePage, name='Welcomepage'),
    path('', views.index, name='index'), 
    path('registerCareGiver', accountsView.registerCareGiver, name='registerCareGiver'), 
    path('registerCareHome', accountsView.registerCareHome, name='registerCareHome'), 
    path('login', accountsView.loginAccount, name='login'),
    path('logout', accountsView.logoutAccount, name='logout'),
    path('careGiverDashboard', careGiverView.careGiverDashboard, name='careGiverDashboard'), 
    path('careGiverBioData', careGiverView.careGiverBiodata, name='careGiverBioData'),
    path('careGiverEducation', careGiverView.careGiverEducation, name='careGiverEducation'),
    path('careGiverWorkType', careGiverView.careGiverWorkType, name='careGiverWorkType'),
    path('careHomeDashboard', careHomeView.careHomeDashboard, name='careHomeDashboard'), 
    path('careHomeProfile', careHomeView.careHomeProfile, name='careHomeProfile'), 
    path('careHomeSearch', careHomeView.careHomeSearch, name='careHomeSearch'), 
    path('bookCareGiver/<int:user_id>/', careHomeView.bookCareGiver, name='bookCareGiver'),
    path('bookCareGiver', careHomeView.bookCareGiver, name='bookCareGiver'),
    path('careGiverDetails/<int:user_id>/', careHomeView.careGiverDetails, name='bookCareGiver')
    
    
]