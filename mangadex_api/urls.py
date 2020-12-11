import posixpath

def urljoin(*path):
    return posixpath.join(*path)

class ApiUrl:

    scheme = 'https'
    netloc = 'mangadex.org'

    api_path = '/api/v2'
    old_api_path = '/api'

    def domain():
        return f'{ApiUrl.scheme}://{ApiUrl.netloc}'

    def api_url(instance):
        return ApiUrl.domain() + urljoin(ApiUrl.api_path, instance.__class__.__name__.lower())

    def old_api_url(instance):
        return ApiUrl.domain() + urljoin(ApiUrl.old_api_path, instance.__class__.__name__.lower())
