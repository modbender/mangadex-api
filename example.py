from pprint import pprint
from mangadex_api.models import Manga

m = Manga(12714, request=True)
pprint(m.alt_titles)
