
# Stored Secrets handling module in Python

`storedsecrets` is a module implementing a simple approach to keep
your secrets (API keys, passwords, ...) outside of your project files,
so that you can protect them better (e.g. in an encrypted archive, or
any form of external volume), and you don't leak them accidentally
through your favorite versioning tool and platform.

`storedsecrets` exposes a `StoredSecrets` class to handle your secrets.

Typical usage:

    >>> import storedsecrets
    >>> my_secrets = storedsecrets.StoredSecrets("mysecretfile.json")
    >>> API_KEY = my_secrets.get('API_KEY')

If the path of the file is not absolute, it will be searched for in
the directory named in env var `SECRETS`, or in `~/etc/secrets` by
default.

This is minimalist work for the moment.
