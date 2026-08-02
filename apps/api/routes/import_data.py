"""Market data import route - MVP skeleton."""


def import_market_data(records: list):
    return {
        "imported": len(records),
        "status": "validated_pending",
    }
