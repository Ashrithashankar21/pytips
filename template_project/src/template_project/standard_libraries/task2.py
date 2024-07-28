from datetime import datetime
from typing import List, Dict


def date_analytics(date_strings: List[str]) -> Dict[str, List[str]]:
    # Step 2: Convert the strings to datetime objects
    dates = [datetime.strptime(date, "%Y-%m-%d") for date in date_strings]

    # Step 3: Identify the earliest, latest, and all unique dates
    earliest_date = min(dates)
    latest_date = max(dates)
    unique_dates = sorted(set(dates))

    return {
        "earliest_date": earliest_date.strftime("%Y-%m-%d"),
        "latest_date": latest_date.strftime("%Y-%m-%d"),
        "unique_dates": [date.strftime("%Y-%m-%d") for date in unique_dates],
    }


if __name__ == "__main__":
    date_strings = ["2023-07-19", "2021-01-01", "2023-07-19", "2020-05-15"]
    result = date_analytics(date_strings)
    print(result)
