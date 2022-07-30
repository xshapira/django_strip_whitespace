from typing import Union
from django.conf import settings

STRIP_WHITESPACE_COMPRESSION_TYPE: Union[
    "compressed", "decompressed"
] = getattr(settings, "STRIP_WHITESPACE_COMPRESSION_TYPE", "decompressed")


STRIP_WHITESPACE_COMPRESSION_ALGORITHM: Union[
    str("gzip"),
    str("br"),
    str("zstd"),
    str("plain"),
] = "gzip"
