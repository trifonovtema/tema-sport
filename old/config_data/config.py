from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]
    telegram_webhook_secret: str
    telegram_base_webhook_url: str
    crypto_users_ids: list[int]
    webhook_path: str = "/webhook"


@dataclass
class OpenAI:
    openai_api_key: str
    assistant_id: str


@dataclass
class Config:
    tg_bot: TgBot
    open_ai: OpenAI


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    res = Config(
        tg_bot=TgBot(
            token=env("BOT_TOKEN"),
            telegram_webhook_secret=env("TELEGRAM_WEBHOOK_SECRET"),
            telegram_base_webhook_url="https://" + env("DOMAIN_NAME"),
            admin_ids=list(map(int, env.list("ADMIN_IDS"))),
            crypto_users_ids=list(map(int, env.list("CRYPTO_USERS_IDS"))),
        ),
        open_ai=OpenAI(
            openai_api_key=env("OPENAI_API_KEY"), assistant_id=env("ASSISTANT_ID")
        ),
    )

    return res
