"""Watchlist API routes - MVP skeleton."""


def get_watchlist():
    return {
        "items": [],
        "count": 0,
    }


def add_watchlist_item(item: dict):
    return {
        "status": "created",
        "item": item,
    }
