from datetime import datetime, date

#1. Get the current day, month, year, hour, minute and timestamp from datetime module
def get_current_datetime_info():
    now = datetime.now()
    return {
        'day': now.day,
        'month': now.month,
        'year': now.year,
        'hour': now.hour,
        'minute': now.minute,
        'second': now.second,
        'timestamp': now.timestamp(),
    }

current_info = get_current_datetime_info()
print(current_info)

#2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
def format_current_datetime():
    return datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

print("Formatted current date:", format_current_datetime())

#3. Today is 5 December, 2019. Change this time string to time.Today is 5 December, 2019. Change this time string to time
def parse_specific_date(date_str="Today is 5 December, 2019."):
    cleaned = date_str.replace("Today is ", "").rstrip(".")
    return datetime.strptime(cleaned, "%d %B, %Y")

parsed_date = parse_specific_date()
print("Parsed date object:", parsed_date)

#4. Calculate the time difference between now and new year
def time_until_next_new_year():
    now = datetime.now()
    next_new_year = datetime(now.year + 1, 1, 1)
    return next_new_year - now

print("Time until New Year:", time_until_next_new_year())

#5. Calculate the time difference between 1 January 1970 and now
def seconds_since_epoch():
    return (datetime.now() - datetime(1970, 1, 1)).total_seconds()

print("Seconds since January 1, 1970:", seconds_since_epoch())