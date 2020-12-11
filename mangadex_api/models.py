import json
from datetime import datetime

from .urls import ApiUrl
from .datas import GENRES, LINKS, LANGUAGES, DEMOGRAPHICS, PUB_STATUS, SEARCHABLE_LANGS
from .request import get_json

__all__ = ['Agent', 'Chapter', 'Manga']


class BaseModel:
    def __init__(self, id=None, request=False):
        self.id = id
        self.request = request

        if request:
            self.populate_manga()

class Agent(BaseModel):
    def __init__(self, *args, **kwargs):
        super(Agent, self).__init__(*args, **kwargs)

class Chapter(BaseModel):
    id = int()
    hash = str()

    manga_id = int()
    manga_title = str()
    volume = str()
    chapter = str()
    title = str()


    group = dict()

    uploader = int()
    timestamp = int()
    comments = int()
    views = int()

    server = str()

    _language = str()

    _pages = list()

    def populate_chapter(self):
        pass

class Manga(BaseModel):
    id = int()
    title = str()
    cover = str()
    description = str()

    #others
    hentai = False

    #stats
    views = int()
    followers = int()
    rating = float()
    rating_mean = float()
    rating_user_count = int()
    comments = int()

    #lists
    alt_titles = list()

    artists = list()
    authors = list()
    relations = list()

    covers = list()
    chapters = list()

    _language = str()
    _status = int()
    _demographic = int()

    _last_uploaded = int()

    _genres = list()
    _links = list()

    @property
    def language(self):
        return self._language

    @property
    def status(self):
        return self._status

    @property
    def demographic(self):
        return self._demographic

    @property
    def last_uploaded(self):
        return self._last_uploaded

    @property
    def genres(self):
        return self._genres

    @property
    def links(self):
        return self._links

    @language.setter
    def language(self, language):
        if language:
            language = (language, LANGUAGES[language.upper()])
            self._language = language

    @status.setter
    def status(self, status):
        self._status = (status, PUB_STATUS[status])

    @demographic.setter
    def demographic(self, demographic):
        if demographic:
            demographic = (demographic, DEMOGRAPHICS[demographic])
            self._demographic = demographic

    @last_uploaded.setter
    def last_uploaded(self, last_uploaded):
        if last_uploaded:
            last_uploaded = datetime.fromtimestamp(last_uploaded).strftime("%A, %B %d, %Y %I:%M:%S")
            self._last_uploaded = last_uploaded

    @genres.setter
    def genres(self, genres):
        if genres:
            new_genres = []
            for genre in genres:
                new_genres.append((genre, GENRES[genre]))
            self._genres = genres

    @links.setter
    def links(self, links):
        if links:
            new_links = []
            for domain, path in links.items():
                new_links.append({
                    'name': LINKS[domain]['name'],
                    'link': LINKS[domain]['prefix'] + path
                })
            self._links = new_links

    def parse_data(self, jdata):
        self.id = jdata['id']
        self.title = jdata['title']
        self.cover = jdata['mainCover']
        self.description = jdata['description']

        publication = jdata.get('publication')
        self.language = publication.get('language')
        self.status = publication.get('status')
        self.demographic = publication.get('demographic')

        self.hentai = jdata['isHentai']
        self.last_uploaded = jdata['lastUploaded']

        self.views = jdata['views']
        self.followers = jdata['follows']
        self.comments = jdata['comments']

        rating = jdata['rating']
        self.rating = rating['bayesian']
        self.rating_mean = rating['mean']
        self.rating_user_count = rating['users']

        self.alt_titles = jdata['altTitles']
        self.genres = jdata['tags']
        self.artists = jdata['artist']
        self.authors = jdata['author']
        self.relations = jdata['relations']
        self.links = jdata['links']

    def populate_manga(self, id=None):
        if not (id or self.id):
            raise ValueError('ID must be passed')
        jdata = get_json(ApiUrl.api_url(self) + '/' + str(self.id))
        self.parse_data(jdata['data'])

    def populate_covers(self):
        if not (id or self.id):
            raise ValueError('ID must be passed')
