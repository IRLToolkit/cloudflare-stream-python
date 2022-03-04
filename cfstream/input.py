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
from dataclasses import dataclass, field
from enum import Enum

from .http import *
from .client import *
from .source import *
from .exceptions import *

_log = logging.getLogger(__name__)

class RecordingMode(Enum):
    Off = "off"
    Automatic = "automatic"

class StatusState(Enum):
    Connected = "connected"
    Connecting = "connecting"
    Disconnected = "disconnected"

class StatusReason(Enum):
    Connected = "connected"
    Reconnected = "reconnected"
    Reconnecting = "reconnecting"
    ClientDisconnect = "client_disconnect"
    FailedToConnect = "failed_to_connect"
    FailedToReconnect = "failed_to_reconnect"
    NewConfigurationAccepted = "new_configuration_accepted"

@dataclass
class AbstractStatus:
    state: StatusState
    reason: StatusReason
    statusEnteredAt: str = None
    statusLastSeen: str = None

@dataclass
class InputStatus:
    current: AbstractStatus = None
    history: list = None

@dataclass
class RtmpCredentials:
    url: str
    streamKey: str

@dataclass
class SrtCredentials:
    url: str
    streamId: str
    passphrase: str

@dataclass
class RecordingProperties:
    mode: RecordingMode = RecordingMode.Off
    requireSignedUrls: bool = False
    allowedOrigins: list = field(default_factory = list)
    timeoutSeconds: int = 0

@dataclass
class PartialInput:
    """Partial object representation of a Cloudflare Stream input."""
    uid: str
    meta: dict = None
    created: str = None
    modified: str = None

@dataclass
class Input(PartialInput):
    """Full object representation of a Cloudflare Stream input."""
    status: InputStatus = None
    rtmps: RtmpCredentials = None
    rtmpsPlayback: RtmpCredentials = None
    srt: SrtCredentials = None
    srtPlayback: SrtCredentials = None
    recording: RecordingProperties = None
