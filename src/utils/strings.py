from enum import Enum


class API(Enum):
    SUCCESS = 200
    EMPTY = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500
    SERVICE_UNAVAILABLE = 503


class API_STATUS(Enum):
    SUCCESS = 0
    WARNING = 1
    ERROR = 2
    INFO = 3