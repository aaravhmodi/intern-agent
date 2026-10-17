"""Conservative OpenAI spending guard for one daily run."""

import json

from openai import OpenAI
from pydantic import BaseModel


class BudgetExhausted(Exception):
    """The next model request cannot fit within the run budget."""


class RunBudget:
    """Reserve worst-case request costs before sending them.

    Luna's long-context rates are used even for short prompts. A completed call
    retains its conservative reservation; failed calls retain it too because a
    failed client request can still have generated billable tokens.
    """

    def __init__(self, limit_usd: float) -> None:
        self.limit_usd = limit_usd
        self.reserved_usd = 0.0
        self.calls = 0

    def reserve(
        self,
        client: OpenAI,
        model: str,
        messages: list[dict[str, str]],
        max_output_tokens: int,
        text_format: type[BaseModel],
    ) -> None:
        if model != "gpt-6-luna":
            raise BudgetExhausted("Daily budget supports gpt-6-luna only")
        if self.limit_usd <= self.reserved_usd:
            raise BudgetExhausted("Daily AI budget exhausted")
        # This endpoint counts message roles and other request framing too.
        counted = client.responses.input_tokens.count(model=model, input=messages).input_tokens
        # The parser also sends a JSON schema. Every UTF-8 byte can contribute at
        # most one text token; double its size and add framing headroom.
        schema_bytes = len(json.dumps(text_format.model_json_schema()).encode("utf-8"))
        upper_input = counted + 2 * schema_bytes + 1024
        # Published long-context Luna rates (USD per million), which are higher
        # than short-context rates: input $0.20, output $0.75.
        reservation = (upper_input * 0.20 + max_output_tokens * 0.75) / 1_000_000
        if self.reserved_usd + reservation > self.limit_usd:
            raise BudgetExhausted("Next AI request exceeds daily $0.50 budget")
        self.reserved_usd += reservation
        self.calls += 1

    @property
    def remaining_usd(self) -> float:
        return max(0.0, self.limit_usd - self.reserved_usd)
