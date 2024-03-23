from datetime import datetime as date
from datetime import timedelta

def str_to_date(string: str) -> date.date:
	return date.strptime(string, "%Y-%m-%d").date() if string not in ["", None] else None

def date_to_str(_date: date.date) -> str:
	return _date.strftime("%Y-%m-%d") if _date != None else None

def get_str_dates(start: str, end: str) -> list:
	start_date = str_to_date(start)
	end_date = str_to_date(end)
	diff_days = (end_date - start_date).days

	return [date_to_str(start_date + timedelta(days=delta)) for delta in range(diff_days)]