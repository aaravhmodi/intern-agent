import sys

from pydantic_settings import BaseSettings, SettingsConfigDict

DEFAULT_NPX = "npx.cmd" if sys.platform == "win32" else "npx"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    outlook_mcp_command: str = DEFAULT_NPX
    outlook_mcp_package: str = "@softeria/ms-365-mcp-server@0.158.0"
    # Set true for Microsoft 365 work/school accounts (e.g. a uwaterloo.ca mailbox).
    outlook_org_mode: bool = False
    timezone: str = "America/Toronto"

    def outlook_server_args(self, *extra: str) -> list[str]:
        args = ["-y", self.outlook_mcp_package, "--read-only", "--preset", "mail,calendar"]
        if self.outlook_org_mode:
            args.append("--org-mode")
        return [*args, *extra]


def get_settings() -> Settings:
    return Settings()
