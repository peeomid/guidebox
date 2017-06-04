api_key = None
api_base = 'https://api-public.guidebox.com/v2'
quota = {
            "rate-limit": 0,   #'X-RateLimit-Limit':
            "rate-remaining": 0,   #'X-RateLimit-Remaining':
            "quota": 0,   #'Guidebox-Quota':
            "quota-max": 0     #'Guidebox-Quota-Max':
        }
#Resources
from guidebox.resource import (Channel, Clip, Episode, Genre, Movie, Person, Quota, Region, Search, Segment, Show, Source, Tag, Update)

from guidebox.version import VERSION
