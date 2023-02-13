try:
    import ssl
    SSLContext = ssl.SSLContext
except ImportError:  # pragma: no cover
    ssl = None  # type: ignore
    SSLContext = object # type: ignore
    print(22)