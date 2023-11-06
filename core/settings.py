import config
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str


@dataclass
class Settings:
    bots: Bots


def get_settings(path: str):
    return Settings(
        bots = Bots(
            bot_token = config.BOT_TOKEN
        )
    )


settings = get_settings('input')
