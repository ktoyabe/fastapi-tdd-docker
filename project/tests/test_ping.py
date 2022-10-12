from fastapi import status

from app import main


def test_ping(test_app):
    # Given
    # test_app

    # When
    response = test_app.get("/ping")

    # Then
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"environment": "dev", "ping": "pong!", "testing": True}
