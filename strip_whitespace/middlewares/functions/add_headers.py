from typing import Union

# Django import
from django.http.request import HttpRequest
from django.http.response import HttpResponse


def add(request: HttpRequest, response: HttpResponse, algorithm: Union["gzip", "br", "zstd", "plain"] = "gz"):
    accepted_encodings = request.META.get("HTTP_ACCEPT_ENCODING", "")

    if algorithm == "plain":
        """
        If algorithm is text/plain don't do anything 🤷‍♂️
        """

        response.headers["Content-Encoding"] = "text/plain; charset:utf-8"

    elif algorithm in accepted_encodings:
        """
        Developer has chosen an algorithm that's not accepted by the browser.
            So do as the developer says 😄
        """

        response.headers["Content-Encoding"] = algorithm

    else:
        """
        Developer has chosen an algorithm that's not accepted by the browser. 🤦‍♂️
            So raise an error and explain the error.
        """

        raise ValueError(
            f"""
            Error in 'strip_whitespace.middlewares.functions.add_headers'

                Accepted HTTP ENCODING = { accepted_encodings }

                    Please switch { algorithm } to any of these : { accepted_encodings } in settings.py
        """
        )
