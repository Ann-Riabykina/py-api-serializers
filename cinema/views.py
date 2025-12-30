from rest_framework import viewsets
from .models import (
    Genre,
    Actor,
    CinemaHall,
    Movie,
    MovieSession,
)
from .serializers import (
    GenreSerializer, ActorSerializer, CinemaHallSerializer,
    MovieListSerializer, MovieDetailReadSerializer,
    MovieDetailWriteSerializer, MovieSessionListSerializer,
    MovieSessionDetailReadSerializer, MovieSessionDetailWriteSerializer
)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class CinemaHallViewSet(viewsets.ModelViewSet):
    queryset = CinemaHall.objects.all()
    serializer_class = CinemaHallSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieListSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return MovieDetailWriteSerializer
        else:
            return MovieDetailReadSerializer


class MovieSessionViewSet(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return MovieSessionListSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return MovieSessionDetailWriteSerializer
        else:
            return MovieSessionDetailReadSerializer
