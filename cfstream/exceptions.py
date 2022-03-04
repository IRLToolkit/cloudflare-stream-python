"""
The MIT License (MIT)

Copyright (c) 2022-present IRLToolkit Inc.

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

class CloudflareException(Exception):
    """Base exception class for cfstream."""
    pass

class HttpException(CloudflareException):
    """Base exception class for http exceptions."""
    def __init__(self, status: int, code: int = None, text: str = None):
        self.status: int = status
        self.code: int = code
        self.text: str = text
        exceptionMessage = '{0}'
        if self.code:
            exceptionMessage += ': {1} (api error code: {2})'
        super().__init__(exceptionMessage.format(self.status, self.text, self.code))

class ForbiddenException(HttpException):
    """Exception raised for HTTP 403 errors."""
    pass

class NotFoundException(HttpException):
    """Exception raised for HTTP 404 errors."""
    pass

class ApiException(HttpException):
    """Exception for errors returned by the Cloudflare API."""
    pass
