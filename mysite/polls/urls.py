from django.urls import path


from . import views

app_name ="polls"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # ex: /polls/choice/
    path("<int:question_id>/newchoice/", views.newchoice, name="newchoice"),
    # ex polls/reset
    path("<int:question_id>/reset/", views.reset, name="reset"),
    #ex polls/addquestions
    path("addques/", views.addques, name="addques"),
    path("newques/", views.newques, name="newques"),

    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),

]