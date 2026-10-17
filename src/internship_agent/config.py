import sys
from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

DEFAULT_NPX = "npx.cmd" if sys.platform == "win32" else "npx"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    outlook_mcp_command: str = DEFAULT_NPX
    outlook_mcp_package: str = "@softeria/ms-365-mcp-server@0.158.0"
    # Set true for Microsoft 365 work/school accounts (e.g. a uwaterloo.ca mailbox).
    outlook_org_mode: bool = False
    timezone: str = "America/Toronto"

    openai_api_key: str | None = None
    openai_model: str = "gpt-6-luna"
    openai_writing_model: str = "gpt-6-luna"
    resume_path: Path = Path("../website/public/ModiAaravResume.pdf")
    candidate_context_path: Path = Path("candidate_context.md")
    data_dir: Path = Path("data")
    # Open (not applied/skipped) postings the dashboard keeps topped up.
    target_open_postings: int = 15
    # Grok is used only for searching X posts (x_search), kept cheap and capped.
    xai_api_key: str | None = None
    xai_model: str = "grok-4.20-0309-non-reasoning"
    xai_max_calls_per_run: int = 3

    # Where to look for startups and postings: canada, usa, europe.
    search_regions: list[str] = ["canada", "usa", "europe"]

    # Gmail sending (dashboard "Send" button). Use a Google app password, never your
    # account password: https://myaccount.google.com/apppasswords
    gmail_address: str | None = None
    gmail_app_password: SecretStr | None = None

    # Automatic follow-ups (`leads followups`): off unless switched on. One goes out
    # after this many days without a reply, to at most this many people in one run.
    followups_enabled: bool = False
    followup_days: int = 5
    followup_daily_limit: int = 25

    # Daily run (`leads daily`): ntfy topic your phone subscribes to (https://ntfy.sh).
    # No topic means no push. The legacy daily count controls remain accepted for old .envs;
    # the current prep run covers every open posting in the database.
    daily_new_postings: int = 10
    daily_prepare: int = 6
    daily_min_score: int = 60
    ntfy_server: str = "https://ntfy.sh"
    ntfy_topic: str | None = None
    dashboard_url: str | None = None

    # Browser-driven applications. Sign in once with `internship-agent leads browser-login`.
    auto_submit_applications: bool = True
    application_browser_dir: Path = Path("data/application-browser")

    # Extra hostnames the dashboard answers to, e.g. a Tailscale IP when run on another machine.
    dashboard_allowed_hosts: list[str] = []

    @property
    def gmail_ready(self) -> bool:
        password = self.gmail_app_password.get_secret_value() if self.gmail_app_password else ""
        return bool(self.gmail_address and password.strip())

    def outlook_server_args(self, *extra: str) -> list[str]:
        args = ["-y", self.outlook_mcp_package, "--read-only", "--preset", "mail,calendar"]
        if self.outlook_org_mode:
            args.append("--org-mode")
        return [*args, *extra]


def get_settings() -> Settings:
    return Settings()
