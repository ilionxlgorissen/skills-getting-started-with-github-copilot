from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities_state():
    original_activities = deepcopy(activities)

    yield

    activities.clear()
    activities.update(deepcopy(original_activities))
