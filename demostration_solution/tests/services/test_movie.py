from unittest.mock import MagicMock

import pytest

from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie1 = Movie(id=1, title='title', description='description', trailer='trailer', year=2021, rating=1.2)
    movie2 = Movie(id=2, title='title', description='description', trailer='trailer', year=2022, rating=1.2)
    movie3 = Movie(id=3, title='title', description='description', trailer='trailer', year=2023, rating=1.2)

    movie_dao.get_one = MagicMock(return_value=movie1)
    movie_dao.get_all = MagicMock(return_value=[movie1, movie2, movie3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    movie_dao.partially_update = MagicMock()

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_create(self):
        movie4 = {
            'title': 'title',
            'description': 'description',
            'trailer': 'trailer',
            'year': 2023,
            'rating': 1.2
        }

        movie = self.movie_service.create(movie4)

        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie = {
            "id": 3,
            'title': 'title',
            'description': 'description',
            'trailer': 'trailer',
            'year': 2023,
            'rating': 1.2
        }
        self.movie_service.update(movie)

    def test_partially_update(self):
        movie = {
            "id": 3,
            'title': 'title',
            'description': 'description',
            'trailer': 'trailer',
            'year': 2023,
            'rating': 1.2
        }
        self.movie_service.update(movie)
