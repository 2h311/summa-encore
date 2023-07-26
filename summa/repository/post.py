import os, re

import requests

from summa import app

months = {
    "01": "Jan",
    "02": "Feb",
    "03": "Mar",
    "04": "Apr",
    "05": "May",
    "06": "Jun",
    "07": "Jul",
    "08": "Aug",
    "09": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dec",
}


def get_posts(payload: dict) -> list[dict]:
    headers = {"authorization": f"Bearer {app.config.get('HYGRAPH_TOKEN')}"}
    response = requests.post(
        app.config.get("HYGRAPH_ENDPOINT"), json=payload, headers=headers
    )
    assert response.ok, "An Error Occured"
    posts = response.json()["data"]["blogPosts"]
    # readjust the createdAt date
    for post in posts:
        year, month, day = re.match(
            "(\d{4})-(\d{2})-(\d{2})", post["createdAt"]
        ).groups()
        post["createdAt"] = f"{day} {months.get(month)} {year}"
    return posts


def get_first_four():
    payload = {
        "query": """
        query Assets {
            blogPosts(orderBy: publishedAt_ASC, last: 4) {
                slug
                title
                description
                createdAt
                images {
                    url
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
            blogPosts(orderBy: publishedAt_ASC) {
                slug
                title
                id
                createdAt
                description
                images {
                    url
                }
                richText {
                    html
                }
            }
        }
    """
    }
    return get_posts(payload)
