import json

import pytest
from fastapi import status

def test_create_summary(test_app_with_db):
    response = test_app_with_db.post(
        "/summaries/",
        data=json.dumps({"url": "https://foo.bar"})
    )

    print(response)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["url"] == "https://foo.bar"
