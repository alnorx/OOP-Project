# Alan Nortey
# GitHub username: alnorx
# CS 161 Project 10

class Movie:
    """Movies class contains Title, genre, director and year as object"""
    def __init__(self, title, genre, director, year):
        """Init method for Movie class"""
        self._title = title
        self._genre = genre
        self._director = director
        self._year = year

    def get_title(self):
        """Get method for Movie class. Returns movie's title"""
        return self._title

    def get_genre(self):
        """Get method for Movie class. Returns movie's genre"""
        return self._genre

    def get_director(self):
        """Get method for Movie class. Returns movie's director"""
        return self._director

    def get_year(self):
        """ Get method for Movie class. Returns movie's year of release"""
        return self._year


class StreamingService:
    """StreamingService class has two objects, name and catalog. The catalog is a dictionary of Movies,
    with the titles as the keys and the Movie objects as the corresponding values """
    def __init__(self, name):
        self._name = name
        self._catalog = {}

    def get_name(self):
        """Get method for object "name" in StreamingService class"""
        return self._name

    def get_catalog(self):
        """Get method for object "catalog" in StreamingService class"""
        return self._catalog

    def add_movie(self, movie_object):
        """Add movies to catalog.
        Take object from Movie class and adds it to catalog"""
        self._catalog[movie_object.get_title()] = movie_object

    def delete_movie(self, title):
        """Delete movies in catalog.
        Take title from Movie class and deletes movie in catalog"""
        if title in self._catalog:
            del self._catalog[title]


class StreamingGuide:
    def __init__(self):
        """ Contains one data member, a list of StreamingService objects"""
        self._streaming_service = []

    def add_streaming_service(self, streaming_service_object):
        """ Takes StreamingService object as an argument and adds it to the list"""
        self._streaming_service.append(streaming_service_object)

    def delete_streaming_service(self, service_name):
        """Takes the name of a streaming service as an
        argument and if it's in the list, removes it."""
        for service in self._streaming_service:
            if service.get_name() == service_name:
                self._streaming_service.remove(service)
                break

    def who_streams_this_movie(self, title):
        """ Takes a movie title as a parameter and
        returns either a dictionary or the value None"""
        for service in self._streaming_service:
            catalog = service.get_catalog()
            if title in catalog:
                movie = catalog[title]
                return {
                    "title": movie.get_title(),
                    "year": movie.get_year(),
                    "services": [s.get_name() for s in self._streaming_service]}
        return None

