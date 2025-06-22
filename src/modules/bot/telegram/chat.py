from collections.abc import Awaitable
import logging
from typing import Any, Callable, Union

logger = logging.getLogger(__name__)

MessageCallback = Callable[[str], Union[Awaitable[Any], Any]]

class Chat:
    __message_listeners: list[MessageCallback] = []
    __error_listeners: list[MessageCallback] = []

    def __init__(self):
       ...

    def add_on_message_listener(self, cb: MessageCallback):
        self.__message_listeners.append(cb)
        return self

    def add_on_error_listener(self, cb: MessageCallback):
        self.__error_listeners.append(cb)
        return self

    async def emit_message(self, message: str | None):
        if message is not None:
            logger.info(f"Chat message: {message}")
            for listener in self.__message_listeners:
                await listener(message)

    async def emit_error(self, error: str | None):
        if error is not None:
            logger.error(f"Chat error: {error}")
            for listener in self.__error_listeners:
                await listener(error)