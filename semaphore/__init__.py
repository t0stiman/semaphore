#!/usr/bin/env python
#
# Semaphore: A simple (rule-based) bot library for Signal Private Messenger.
# Copyright (C) 2020
# Lazlo Westerhof <semaphore@lazlo.me>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
"""Semaphore: A simple (rule-based) bot library for Signal Private Messenger."""

from .meta import *

from .attachment import Attachment
from .bot import Bot, StopPropagation
from .chat_context import ChatContext
from .data_message import DataMessage
from .group import Group
from .job import Job
from .job_queue import JobQueue
from .message import Message
from .message_receiver import MessageReceiver
from .message_sender import MessageSender
from .reply import Reply
from .socket import Socket
