def min_to_hour(minutes):
    """
    converts input minutes to HH:MM format
    :param minutes: input integer representative of minutes
    :return: HH:MM 12hr formatting
    """
    hour = int(minutes / 60)
    minute = minutes % 60
    ampm = ""
    if minutes < 720:
        ampm = "AM"
    else:
        ampm = "PM"
        hour -= 12
    time = "%d:02d" % (hour, minute)

    return time + ' ' + ampm


def reverse_min(time):
    """
    converts input HH:MM into minutes
    :param time: input HH:MM
    :return: HH:MM in minutes format
    """
    parse = time.split(':')
    hour = parse[0]
    splitting = parse[1].split(' ')
    minute = splitting[0]
    ampm = splitting[1]

    minutes = float(hour) * 60 + float(minute)

    if ampm.upper() == "AM":
        return minutes
    else:
        return minutes + 720



