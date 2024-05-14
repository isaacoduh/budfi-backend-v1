import unittest.mock

from fastapi.testclient import TestClient
from main import app
from app.db.models import User
from app.db.base import get_session

client = TestClient(app)


def test_register():
    pass