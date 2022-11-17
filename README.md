# Octodata

Tools for getting your Octopus Energy electricity data into a SQLite database,
for exploration in [Datasette](https://datasette.io).

## Usage

1. Install the dependencies: `pip install -r requirements.txt`
2. Find your API key, serial number and MPAN from
   https://octopus.energy/dashboard/developer/
3. Rename `.env-example` to `.env` and fill in the details
4. Fetch all your historic data with `python all.py`. This may take a few
   minutes
5. Get daily updates with `python daily.py`
6. Use Datasette to explore your data: `datasette readings.db`

## Useful queries

### Total usage by month

```sql
select 
    strftime("%m-%Y", start_time) as 'month-year',
    sum(usage) as monthly_usage
from readings 
group by strftime("%m-%Y", start_time);
```

### Average usage per month

```sql
select 
    strftime("%m-%Y", start_time) as 'month-year',
    avg(usage) as avg_usage
from readings 
group by strftime("%m-%Y", start_time);
```

### Average use on Mondays

```sql
select 
    strftime("%m-%Y", start_time) as 'month-year',
    avg(usage) as avg_usage 
from readings 
where strftime("%w", start_time) = "1"
group by strftime("%m-%Y", start_time);
```

### Average use per hour:

```sql
select 
    strftime("%H", start_time) as time,
    avg(usage) as avg_usage 
from readings 
group by strftime("%H", start_time);
```
