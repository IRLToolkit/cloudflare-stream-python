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

import logging
import aiohttp

from .exceptions import *

_log = logging.getLogger(__name__)

#logging.getLogger('aiohttp').setLevel(logging.DEBUG)

class HttpClient:
    def __init__(self, accountId: str, apiToken: str):
        self.accountId: str = accountId
        self.apiToken: str = apiToken

        self.baseUrl = 'https://api.cloudflare.com/client/v4/accounts/{}/stream'.format(self.accountId)

    async def _perform_request(self, method: str, path: str, **kwargs):
        url = self.baseUrl + (path if path.startswith('/') else '/' + path)
        
        headers: Dict[str, str] = {
            'Authorization': 'Bearer ' + self.apiToken
        }
        kwargs['headers'] = headers

        async with aiohttp.ClientSession() as session:
            async with session.request(method, url, **kwargs) as resp:
                _log.debug('Made {} request to {}, got {} status'.format(method, url, resp.status))
                responseData = None
                if resp.content_type == 'application/json':
                    responseData = await resp.json()
                #if responseData and not responseData['success']:
                #    raise ApiException(resp.status, responseData['errors'][0]['code'], responseData['errors'][0]['message'])
                if not resp.ok:
                    if resp.status == 403:
                        raise ForbiddenException(403)
                    elif resp.status == 404:
                        raise NotFoundException(404)
                    else:
                        print(await resp.text())
                        raise HttpException(resp.status)
                return responseData['result'] if responseData else None

    async def verify_credentials(self):
        return False

    async def get_inputs(self):
        pass

    async def get_input(self, uid):
        pass
