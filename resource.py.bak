from __future__ import unicode_literals

import json

from guidebox import api_requestor
from guidebox import error
from guidebox.compat import string_type


def guidebox_format(resp):
    types = {
        'channel': Channel,
        'clip': Clip,
        'episode': Episode,
        'genre': Genre,
        'movie': Movie,
        'person': Person,
        'quota': Quota,
        'segment': Segment,
        'show': Show,
        'source': Source,
        'tag': Tag,
        'update': Update
    }

    #Recursively Set Objects for Lists
    if isinstance(resp, dict) and 'object' in resp and resp['object'] == 'list':
        resp['results'] = [guidebox_format(i) for i in resp['results']]
        return GuideboxObject.construct_from(resp)
    if isinstance(resp, dict) and not isinstance(resp, GuideboxObject):
        resp = resp.copy()
        if 'object' in resp and isinstance(resp['object'], string_type):
            klass = types.get(resp['object'], GuideboxObject)
        else:
            klass = GuideboxObject

        #Check For Arrays
        for key in resp:
            if isinstance(resp[key], list):
                resp[key] = [guidebox_format(i) for i in resp[key]]
        return klass.construct_from(resp)
    else:
        return resp

class GuideboxObject(dict):

    def __init__(self, id=None, **params):
        super(GuideboxObject, self).__init__()
        if id:
            self['id'] = id

    @classmethod
    def construct_from(cls, values):
        instance = cls(values.get('id'))
        for k, v in values.items():
            instance[k] = guidebox_format(v)
        return instance

    def __getattr__(self, k):
        try:
            return self[k]
        except KeyError:
            raise AttributeError(k) #pragma: no cover

    def __setattr__(self, k, v):
        self[k] = v

    def __repr__(self):
        ident_parts = [type(self).__name__]

        if isinstance(self.get('object'), string_type):
            ident_parts.append(self.get('object'))

        if isinstance(self.get('id'), string_type):
            ident_parts.append('id=%s' % (self.get('id'),))

        unicode_repr = '<%s at %s> JSON: %s' % (
            ' '.join(ident_parts), hex(id(self)), str(self))

        return unicode_repr

    def __str__(self):
        return json.dumps(self, sort_keys=True, indent=2)

class APIResource(GuideboxObject):
    @classmethod
    def retrieve(cls, id, **params):
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', '%s/%s' % (cls.endpoint, id), params)
        return guidebox_format(response)

# API Operations
class ListableAPIResource(APIResource):
    @classmethod
    def list(cls, **params):
        for key, value in params.items():
            if isinstance(params[key], dict):
                for subKey in value:
                    params[str(key) + '[' + subKey + ']'] = value[subKey]
                del params[key]
            elif isinstance(params[key], list):
                params[str(key) + '[]'] = params[key]
                del params[key]
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', cls.endpoint, params)
        return guidebox_format(response)

class ImageableAPIResource(APIResource):
    @classmethod
    def images(cls, id, **params):
        for key, value in params.items():
            if isinstance(params[key], dict):
                for subKey in value:
                    params[str(key) + '[' + subKey + ']'] = value[subKey]
                del params[key]
            elif isinstance(params[key], list):
                params[str(key) + '[]'] = params[key]
                del params[key]
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', '%s/%s/images' % (cls.endpoint, id), params)
        return guidebox_format(response)

class Channel(ListableAPIResource, ImageableAPIResource):
    endpoint = '/channels'

class Clip(ListableAPIResource, ImageableAPIResource):
    endpoint = '/clips'

class Episode(ListableAPIResource, ImageableAPIResource):
    endpoint = '/episodes'

class Genre(ListableAPIResource):
    endpoint = '/genres'

class Movie(ListableAPIResource, ImageableAPIResource):
    endpoint = '/movies'
    @classmethod
    def related(cls, id, **params):
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', '%s/%s/related' % (cls.endpoint, id), params)
        return guidebox_format(response)

    @classmethod
    def trailers(cls, id, **params):
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', '%s/%s/videos' % (cls.endpoint, id), params)
        return guidebox_format(response)

class Person(ImageableAPIResource):
    endpoint = '/person'
    @classmethod
    def credits(cls, id, **params):
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', '%s/%s/credits' % (cls.endpoint, id), params)
        return guidebox_format(response)

class Quota(APIResource):
    endpoint = '/quota'
    @classmethod
    def retrieve(cls, **params):
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', cls.endpoint, params)
        print response

class Region(ListableAPIResource):
    endpoint = '/regions'

class Search(APIResource):
    endpoint = '/search'
    @classmethod
    def movies(cls, **params):
        params['type'] = 'movie'
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', cls.endpoint, params)
        return guidebox_format(response)

    @classmethod
    def shows(cls, **params):
        params['type'] = 'show'
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', cls.endpoint, params)
        return guidebox_format(response)

    @classmethod
    def person(cls, **params):
        params['type'] = 'person'
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', cls.endpoint, params)
        return guidebox_format(response)

    @classmethod
    def channels(cls, **params):
        params['type'] = 'channel'
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', cls.endpoint, params)
        return guidebox_format(response)

class Segment(ListableAPIResource, ImageableAPIResource):
    endpoint = '/segments'

class Show(ListableAPIResource, ImageableAPIResource):
    endpoint = '/shows'
    @classmethod
    def seasons(cls, id, **params):
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', '%s/%s/seasons' % (cls.endpoint, id), params)
        return guidebox_format(response)

    @classmethod
    def related(cls, id, **params):
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', '%s/%s/related' % (cls.endpoint, id), params)
        return guidebox_format(response)

    @classmethod
    def episodes(cls, id, **params):
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', '%s/%s/episodes' % (cls.endpoint, id), params)
        return guidebox_format(response)

    @classmethod
    def clips(cls, id, **params):
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', '%s/%s/clips' % (cls.endpoint, id), params)
        return guidebox_format(response)

    @classmethod
    def segments(cls, id, **params):
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', '%s/%s/segments' % (cls.endpoint, id), params)
        return guidebox_format(response)

    @classmethod
    def available_content(cls, id, **params):
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', '%s/%s/available_content' % (cls.endpoint, id), params)
        return guidebox_format(response)

class Source(ListableAPIResource):
    endpoint = '/sources'

class Tag(ListableAPIResource):
    endpoint = '/tags'

class Update(APIResource):
    endpoint = '/updates'
    @classmethod
    def all(cls, **params):
        requestor = api_requestor.APIRequestor()
        response = requestor.request('get', '%s' % (cls.endpoint), params)
        return guidebox_format(response)

class Postcard(ListableAPIResource):
    endpoint = '/postcards'
    @classmethod
    def create(cls, **params):
        if isinstance(params, dict):
            if 'from_address' in params:
                params['from'] = params['from_address']
                params.pop('from_address')
            if 'to_address' in params:
                params['to'] = params['to_address']
                params.pop('to_address')
        return super(Postcard, cls).create(**params)
