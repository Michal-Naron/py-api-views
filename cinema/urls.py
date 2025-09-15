from django.urls import path
from cinema.views import (
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallList,
    CinemaHallDetail,
    MovieViewSet
)


movie_list = MovieViewSet.as_view(
    actions={
        "get": "list",
        "post": "create",
    }
)
movie_detail = MovieViewSet.as_view(
    actions={
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy",
    }
)


urlpatterns = [
    path(
        "movies/",
        movie_list,
        name="movie-list"
    ),
    path(
        "movies/<int:pk>/",
        movie_detail,
        name="movie-detail"
    ),
    path(
        "genre/",
        GenreList.as_view(),
        name="genre-list"
    ),
    path(
        "genre/<int:pk>/",
        GenreDetail.as_view(),
        name="genre-detail"
    ),
    path(
        "actor/",
        ActorList.as_view(),
        name="actor-list"
    ),
    path(
        "actor/<int:pk>/",
        ActorDetail.as_view(),
        name="actor-detail"
    ),
    path(
        "cinemahall/",
        CinemaHallList.as_view(),
        name="cinemahall-list"
    ),
    path(
        "cinemahall/<int:pk>/",
        CinemaHallDetail.as_view(),
        name="cinemahall-detail"
    ),
]

app_name = "cinema"
