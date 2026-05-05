def hours_to_seconds(hours):
    converted = hours * 3600
    return converted
def test(hours):
    secs = hours_to_seconds(hours)
    print(f"{hours} converted to seconds is {secs}")

test(1)
test(10)
test(100)