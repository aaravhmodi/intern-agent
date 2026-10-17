from types import SimpleNamespace

import pytest
from pydantic import BaseModel

from internship_agent.ai_budget import BudgetExhausted, RunBudget


class Result(BaseModel):
    answer: str


class FakeCounter:
    def __init__(self, input_tokens: int) -> None:
        self.input_tokens = input_tokens
        self.calls = 0

    def count(self, **_kwargs: object) -> SimpleNamespace:
        self.calls += 1
        return SimpleNamespace(input_tokens=self.input_tokens)


def test_budget_stops_before_request_that_exceeds_fifty_cents() -> None:
    counter = FakeCounter(1_000_000)
    client = SimpleNamespace(responses=SimpleNamespace(input_tokens=counter))
    budget = RunBudget(0.50)
    messages = [{"role": "user", "content": "hello"}]
    budget.reserve(client, "gpt-6-luna", messages, 1000, Result)
    budget.reserve(client, "gpt-6-luna", messages, 1000, Result)
    assert budget.calls == 2
    with pytest.raises(BudgetExhausted):
        budget.reserve(client, "gpt-6-luna", messages, 1000, Result)
    assert budget.reserved_usd <= 0.50


def test_budget_fails_closed_for_another_model() -> None:
    counter = FakeCounter(10)
    client = SimpleNamespace(responses=SimpleNamespace(input_tokens=counter))
    with pytest.raises(BudgetExhausted):
        RunBudget(0.50).reserve(client, "gpt-6-astra", [], 1000, Result)
    assert counter.calls == 0
