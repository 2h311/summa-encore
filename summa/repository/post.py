import os

import requests

from summa import app


def get_posts(payload: dict) -> list[dict]:
    headers = {"authorization": f"Bearer {app.config.get('HYGRAPH_TOKEN')}"}
    response = requests.post(
        app.config.get("HYGRAPH_ENDPOINT"), json=payload, headers=headers
    )
    assert response.ok, "An Error Occured"
    return response.json()["data"]["blogPosts"]


def get_first_four():
    payload = {
        "query": """
        query Assets {
            blogPosts(first: 4) {
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
    return get_posts(payload)


def get_all_post():
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
    return get_posts(payload)
