# tests/conftest.py

import pytest
from fastapi.testclient import TestClient
from users.run import app
from users.infrastructure.database import Base, engine, SessionLocal

@pytest.fixture(scope="module")
def test_client():
    # Crear las tablas
    Base.metadata.create_all(bind=engine)
    client = TestClient(app)
    yield client
    # Eliminar las tablas
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db_session():
    session = SessionLocal()
    yield session
    session.close()
