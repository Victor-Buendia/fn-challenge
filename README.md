# fn-challenge
FN Junior Data Engineer challenge.
## Overview
![Diagram](./assets/diagram.png)

### Tasks

- [api_handler.py > def request_day:](https://github.com/Victor-Buendia/fn-challenge/blob/2798f97fc152804539defe8e3d0b3d86c30bf64f/scripts/api_handler.py#L18) Write a Python function that is capable of saving new records for a given date [...]
- [api_handler.py > def request_month:](https://github.com/Victor-Buendia/fn-challenge/blob/2798f97fc152804539defe8e3d0b3d86c30bf64f/scripts/api_handler.py#L33): [...] and a script that can recover all event data for January 2024.
- [pgAdmin:](http://localhost:5050/browser/) Build a history table in a relational database for all of January 2024.
```sql
	SELECT * FROM public.user_events ORDER BY date
```
- [customers_engagement.sql:](https://github.com/Victor-Buendia/fn-challenge/blob/main/dbt/user_events/models/analysis/customers_engagement.sql) We want to measure our customers engagement, so you will need to write an SQL script that calculates weekly active users for January 2024 and saves it as a new table. An active user is any user that has an event for a given date.
- [active_corporations.sql:](https://github.com/Victor-Buendia/fn-challenge/blob/main/dbt/user_events/models/analysis/active_corporations.sql) Each user belongs to a corporate user. Write an SQL script that can also calculate the weekly number of active corporations.
- [summary.sql](https://github.com/Victor-Buendia/fn-challenge/blob/main/dbt/user_events/models/analysis/summary.sql) Finally, write an SQL script that can calculate the average, maximum and minimum number of events per user and corporate for each week in January 2024.

## Work timetable

## Data considerations

## Project considerations

## Usage
## Requirements
### Environment Variables

## Tech Stack
## Code structure

```bash
.
├── db
│   └── setup.sql								#
├── dbt
│   └── user_events
│       ├── models
│       │   ├── analysis
│       │   │   ├── active_corporations.sql		#
│       │   │   ├── customers_engagement.sql	#
│       │   │   └── summary.sql					#	
│       │   └── views
│                └── user_events_view.sql		#
├── dbt.Dockerfile								#
├── docker-compose.yaml							#
├── python.Dockerfile							#
├── scripts
│   ├── api_handler.py							#
│   ├── environment.py							#
│   ├── main.py									#
│   ├── models
│   │   └── user_event.py						#
│   ├── postgres_connector.py					#
│   ├── utils.py								#
│   └── validation
│       └── schemas.py							#
```
## Screenshots
## Final considerations