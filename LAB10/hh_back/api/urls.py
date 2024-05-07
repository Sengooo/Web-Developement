from django.urls import path, include
from api import views

urlpatterns = [
    #path('companies/', views.companies),
    path('companies/', views.Companies.as_view()),
    #path('companies/<int:id>/', views.companiesById),
    path('companies/<int:id>/', views.CompanyById.as_view()),
    #path('companies/<int:id>/vacancies/', views.companyIdVacancies),
    path('companies/<int:id>/vacancies/', views.VacancyListByCompany.as_view()),
    #path('vacancies/', views.vacancyList),
    path('vacancies/', views.Vacancies.as_view()),
    #path('vacancies/<int:id>/', views.vacancyDetail),
    path('vacancies/<int:id>/', views.VacancyDetails.as_view()),
    #path('vacancies/top_ten/', views.topTenVacancies)
    path('vacancies/top_ten/', views.VacancyTop10.as_view())
]
