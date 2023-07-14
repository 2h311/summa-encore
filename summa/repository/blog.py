import os

import requests

from summa import app


payload = {
    "query": """
    query Assets {
        blogPosts {
            slug
            title
            id
            createdAt
            description
            richText {
                html
            }
        }
    }
"""
}

headers = {"authorization": f"Bearer {app.config.get('HYGRAPH_TOKEN')}"}
response = requests.post(app.config.get("HYGRAPH_ENDPOINT"), json=payload, headers=headers)
assert response.ok
