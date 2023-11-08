def main():
    time = input("What time is it? ")

    new_time = convert(time)

    if new_time >= 7 and new_time <= 8:
        print("Breakfast Time")
    elif new_time >= 12 and new_time <= 13:
        print("Lunch Time")
    elif new_time >= 18 and new_time <= 19:
        print("Dinner Time")


def convert(time):

    hours, minutes = time.split(":")
    minutes = float(minutes)
    hours = float(hours)

    new_minutes = minutes / 60

    return new_minutes + hours


main()