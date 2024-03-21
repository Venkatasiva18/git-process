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

# Database Caching
CACHE4 = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "my_cache_table",
    }
}

# Filesystem caching¶
# The file-based backend serializes and stores each cache value as a separate file.
# To use this backend set BACKEND to "django.core.cache.backends.
# filebased.FileBasedCache" and LOCATION to a suitable directory.
# For example, to store cached data in /var/tmp/django_cache, use this setting:

CACHES5 = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "/var/tmp/django_cache",
    }
}
# If you’re on Windows, put the drive letter at the beginning of the path, like this:

CACHE6 = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "c:/foo/bar",


    }
}

# Local-memory caching¶
# This is the default cache if another is not specified in your settings file.
# If you want the speed advantages of in-memory caching but don’t have the capability of running Memcached,
# consider the local-memory cache backend. This cache is per-process (see below) and thread-safe.
# To use it, set BACKEND to "django.core.cache.backends.locmem.LocMemCache". For example:

CACHE7 = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    }
}


