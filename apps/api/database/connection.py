"""Database connection layer for AI Research OS MVP.

Initial implementation keeps storage abstract so SQLite can be replaced by
PostgreSQL without changing business logic.
"""

DATABASE_URL = "sqlite:///./research_os.db"


def get_database_url():
    return DATABASE_URL
