def format_duration(seconds):

    if seconds == 0:
        return 'now'

    counter = {
        'years' : 0,
        'days' : 0,
        'hours' : 0,
        'minutes' : 0,
        'seconds' : 0
    }

    # do the maths and track in the dict
    counter['years'] = seconds // 31536000
    remainder = seconds % 31536000
    counter['days'] = remainder // 86400
    remainder = remainder % 86400
    counter['hours'] = remainder // 3600
    remainder = remainder % 3600
    counter['minutes'] = remainder // 60
    counter['seconds'] = remainder % 60

    time = [] # for building human-readable time

    # add the values to a list using correct singular/plural format
    for unit in counter.keys():
        if counter[unit] > 0:
            if counter[unit] == 1:
                time.append(f"{counter[unit]} {unit[:-1]}")
            else:
                time.append(f"{counter[unit]} {unit}")

    # join the list in a sentance with proper grammer
    if len(time) > 1:
        time.insert(-1, 'and')
        time = ', '.join(time[:-2]) + ' ' + time[-2] + ' ' + time[-1]
    else:
        time = str(time[0])

    return time

print(format_duration(0))
print(format_duration(1)) # "1 second")
print(format_duration(62)) # "1 minute and 2 seconds")
print(format_duration(120)) # "2 minutes")
print(format_duration(3600)) # "1 hour")
print(format_duration(3662)) # "1 hour, 1 minute and 2 seconds")