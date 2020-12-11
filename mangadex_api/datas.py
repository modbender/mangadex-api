DEMOGRAPHICS = {
     1: "Shounen",
     2: "Shoujo",
     3: "Seinen",
     4: "Josei"
 }

GENRES = {
    1: "4-Koma",
    2: "Action",
    3: "Adventure",
    4: "Award Winning",
    5: "Comedy",
    6: "Cooking",
    7: "Doujinshi",
    8: "Drama",
    9: "Ecchi",
    10: "Fantasy",
    11: "Gyaru",
    12: "Harem",
    13: "Historical",
    14: "Horror",
    16: "Martial Arts",
    17: "Mecha",
    18: "Medical",
    19: "Music",
    20: "Mystery",
    21: "Oneshot",
    22: "Psychological",
    23: "Romance",
    24: "School Life",
    25: "Sci-Fi",
    28: "Shoujo Ai",
    30: "Shounen Ai",
    31: "Slice of Life",
    32: "Smut",
    33: "Sports",
    34: "Supernatural",
    35: "Tragedy",
    36: "Long Strip",
    37: "Yaoi",
    38: "Yuri",
    40: "Video Games",
    41: "Isekai",
    42: "Adaptation",
    43: "Anthology",
    44: "Web Comic",
    45: "Full Color",
    46: "User Created",
    47: "Official Colored",
    48: "Fan Colored",
    49: "Gore",
    50: "Sexual Violence",
    51: "Crime",
    52: "Magical Girls",
    53: "Philosophical",
    54: "Superhero",
    55: "Thriller",
    56: "Wuxia",
    57: "Aliens",
    58: "Animals",
    59: "Crossdressing",
    60: "Demons",
    61: "Delinquents",
    62: "Genderswap",
    63: "Ghosts",
    64: "Monster Girls",
    65: "Loli",
    66: "Magic",
    67: "Military",
    68: "Monsters",
    69: "Ninja",
    70: "Office Workers",
    71: "Police",
    72: "Post-Apocalyptic",
    73: "Reincarnation",
    74: "Reverse Harem",
    75: "Samurai",
    76: "Shota",
    77: "Survival",
    78: "Time Travel",
    79: "Vampires",
    80: "Traditional Games",
    81: "Virtual Reality",
    82: "Zombies",
    83: "Incest",
    84: "Mafia"
}

LANGUAGES = {
    'SA': "Arabic",
    'BD': "Bengali",
    'BG': "Bulgarian",
    'MM': "Burmese",
    'CT': "Catalan",
    'CN': "Chinese (Simp)",
    'HK': "Chinese (Trad)",
    'CZ': "Czech",
    'DK': "Danish",
    'NL': "Dutch",
    'GB': "English",
    'PH': "Filipino",
    'FI': "Finnish",
    'FR': "French",
    'DE': "German",
    'GR': "Greek",
    'HU': "Hungarian",
    'ID': "Indonesian",
    'IT': "Italian",
    'JP': "Japanese",
    'KR': "Korean",
    'LT': "Lithuanian",
    'MY': "Malay",
    'MN': "Mongolian",
    'IR': "Persian",
    'PL': "Polish",
    'BR': "Portuguese (Br)",
    'PT': "Portuguese (Pt)",
    'RO': "Romanian",
    'RU': "Russian",
    'RS': "Serbo-Croatian",
    'ES': "Spanish (Es)",
    'MX': "Spanish (LATAM)",
    'SE': "Swedish",
    'TH': "Thai",
    'TR': "Turkish",
    'UA': "Ukrainian",
    'VN': "Vietnamese"
}

LINKS = {
    # Bookwalker
    'bw': {
        'name': "Bookwalker",
        'prefix': "https://bookwalker.jp/"
    },
    # Baka-Updates Manga / MangaUpdates
    'mu': {
        'name': "Baka-Updates Manga",
        'prefix': "https://www.mangaupdates.com/series.html?id="
    },
    # MyAnimeList
    'mal': {
        'name': "My Anime List",
        'prefix': "https://myanimelist.net/manga/"
    },
    # Amazon
    'amz': {
        'name': "Amazon",
        'prefix': ""
    },
    # eBook Japan
    'ebj': {
        'name': "eBook Japan",
        'prefix': ""
    },
    # Official English Translation
    'engtl': {
        'name': "Official English Translation",
        'prefix': ""
    },
    # Raw
    'raw': {
        'name': "Raw",
        'prefix': ""
    },
    # Novel Updates
    'nu': {
        'name': "Novel Updates",
        'prefix': "https://www.novelupdates.com/series/"
    },
    # CD Japan
    'cdj': {
        'name': "CD Japan",
        'prefix': ""
    },
    # Kitsu
    'kt': {
        'name': "Kitsu",
        'prefix': "https://kitsu.io/manga/"
    },
    # Anime-Planet
    'ap': {
        'name': "Anime Planet",
        'prefix': "https://www.anime-planet.com/manga/"
    },
    # AniList
    'al': {
        'name': "AniList",
        'prefix': "https://anilist.co/manga/"
    },
    # Doujinshi.org
    'dj': {
        'name': "Doujinshi.org",
        'prefix': "https://www.doujinshi.org/book/"
    }
}

LISTING_ORDERS = {
    "Last Updated (Asc)": 0,
    "Last Updated (Des)": 1,
    "Title (Asc)": 2,
    "Title (Des)": 3,
    "Comments (Asc)": 4,
    "Comments (Des)": 5,
    "Rating (Asc)": 6,
    "Rating (Des)": 7,
    "Views (Asc)": 8,
    "Views (Des)": 9,
    "Follows (Asc)": 10,
    "Follows (Des)": 11
}

PUB_STATUS = {
    1: "Ongoing",
    2: "Completed",
    3: "Cancelled",
    4: "Hiatus"
}

SEARCHABLE_LANGS = {
    'GB': 1,
    'JP': 2,
    'PL': 3,
    'DE': 8,
    'FR': 10,
    'VN': 12,
    'CN': 21,
    'ID': 27,
    'KR': 28,
    'MX': 29,
    'TH': 32,
    'PH': 34,
    'HK': 35
}

SETTINGS = {
    # Settings for hentai toggle
    'hentai': {
        # No Hentai
        'hidden': 0,
        # Non-Hentai and Hentai
        'shown': 1,
        # Hentai Only
        'exclusive': 2
    }
}

VIEWING_CATEGORIES = {
    'ALL': 0,
    'READING': 1,
    'COMPLETED': 2,
    'ON_HOLD': 3,
    'PLAN_TO_READ': 4,
    'DROPPED': 5,
    'RE_READING': 6
}
