import config
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str
    gpt_client_secret: str
    gpt_auth_data: str


@dataclass
class Settings:
    bots: Bots


def get_settings(path: str):
    return Settings(
        bots = Bots(
            bot_token = config.BOT_TOKEN,
            gpt_client_secret = config.GPT_CLIENT_SECRET,
            gpt_auth_data = config.GPT_AUTH_DATA
        )
    )


settings = get_settings('input')
