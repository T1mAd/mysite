from django.urls import path, include


from . import views

app_name = "polls"

urlpatterns = [
    path("", views.IndexView.as_view(), name = "index"),
    path("meme/", views.meme, name = "meme"),
    path("<int:pk>/", views.DetailView.as_view(), name = "detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name = "results"),
    path("<int:q_id>/vote/", views.vote, name = "vote")
]


