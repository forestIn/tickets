from django.conf.urls import url
from . import views

urlpatterns = [
    # # URL pattern for the UserListView
    # url(
    #     regex=r'^$',
    #     view=views.UserListView.as_view(),
    #     name='list'
    # ),

    # # URL pattern for the UserRedirectView
    # url(
    #     regex=r'^~redirect/$',
    #     view=views.UserRedirectView.as_view(),
    #     name='redirect'
    # ),

    # URL pattern for the UserUpdateView
    url(
        regex=r'^update/',
        view=views.UpdateCustomUserView.as_view(),
        name='update'
    ),

]