import hashlib
from urllib.parse import urlencode

from django import template
from django.conf import settings

register = template.Library()


@register.filter
def gravatar(user):
    email = user.email.lower().encode('utf-8')
    default = 'mm'
    size = 256
    url = 'https://lh3.googleusercontent.com/RtzFFVB7fqOvXW9w7OHziR_xq4muZW_UGhHJoDAgx1ghcgw9KBXbDycZrSeQilU8b51lxmH7LVT7psvHSqEAKddQkBz_DGgItxLZKiU5AP4gf7uGPb7cmDerq9-soqdASpLBzE5x8A5Z5gJC3CtypZiyBoQg7gNvc-YTsnrDOyWereQ50cEdxh-n7Hq_yPe3awOblYdYX-m-J7ZmZ12aND8gDnT16jwsHZZhRZ8Oz5_Hntf16JGwA3qgjQKZGxBK4-szMTERv-ynO3qcqmaVUD2YW5zxj279aLoLxNkF8y_VnNfuXoIEORLs-zuN6GC1RFVIZgfUvXXhAWblxBrUqhWdZT3DXSvJHpzs1rSjTv-2WFD8TdEzdzMdVt7NG-4j05YvrLBsjVYn05uNK3FihNQi638rIk670zNfH5VYz5tvTce8g7tBeBqI-Y85qv0f1irJj5vCCkMgQ-Yp7aXRsjx8da5tw9vVEzi15-ZsSKu7yuxx0TzH9Jl57y_92SKTd2lxEAq1WPVUMzdP9LYaG4J57boA5juaJVd1Gujh0oyHIZ_Am6WO3nkyKx8SadTOzzfgmpoGZf3bKneWOSJeOloDIIRYKo1tyE8TqmIVjTyVqOp9cwSDxFpQDBBcsQbhoJHKHrPvXXTUoZOzMtHjAmVJBKcL86meHNkYuI7m61AodjlPlELx3hs9DxwJhw=w655-h873-no?authuser=0'
    return url