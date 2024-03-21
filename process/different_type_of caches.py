# Meme Cache
# Memcached is running on localhost (127.0.0.1) port 11211, using the pymemcache binding:

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "127.0.0.1:11211",
    }
}

# One excellent feature of Memcached is its ability to share a cache over multiple servers.

CACHES1 = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": [
            "172.19.26.240:11211",
            "172.19.26.242:11211",
        ],
    }
}

# Redis Server

CACHE2 = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}

# Often Redis servers are protected with authentication.
# In order to supply a username and password, add them in the LOCATION along with the URL:

CACHES3 = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://username:password@127.0.0.1:6379",
    }
}
