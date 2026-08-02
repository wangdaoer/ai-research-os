"""AI Research OS API MVP entrypoint."""

from datetime import datetime


def health_check():
    return {
        "status": "ok",
        "service": "ai-research-os-api",
        "time": datetime.utcnow().isoformat()
    }


if __name__ == "__main__":
    print(health_check())
