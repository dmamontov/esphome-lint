"""Test"""

import uuid
from esphome.const import CONF_ID


def get_name_len(name: str) -> int:
    """Len var"""

    return len(name)


def start() -> None:
    """Run ..."""

    print(CONF_ID)
    print(uuid.uuid4().hex)
