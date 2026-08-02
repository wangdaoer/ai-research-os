"""Repository abstraction layer.

Business services should access stored research through this layer.
"""

_research_store = {}


def save_research(record):
    _research_store[record['research_id']] = record
    return record


def get_research(research_id):
    return _research_store.get(research_id)
