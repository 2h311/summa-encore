import os

import requests


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

headers = {"authorization": f"Bearer {}"}
# response = requests.post(, json=payload, headers=headers)
assert response.ok
