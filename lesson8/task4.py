def to_seconds(seconds=0, minutes=0, hours=0, days=0, weeks=0):
    number_seconds_in_minute = 60
    number_seconds_in_hour = 60 * number_seconds_in_minute
    number_seconds_in_day = 24 * number_seconds_in_hour
    number_seconds_in_week = 7 * number_seconds_in_day

    result = seconds + minutes * number_seconds_in_minute + \
             hours * number_seconds_in_hour + \
             days * number_seconds_in_day + \
             weeks * number_seconds_in_week

    return result


if __name__ == "__main__":
    print(to_seconds(minutes=5, days=1))  # 86700