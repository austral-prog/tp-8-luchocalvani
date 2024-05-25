def get_coordinate(record):
    a, b = record
    return b


def convert_coordinate(coordinate):
    a, b = coordinate
    return a, b


def create_record(azara_record, rui_record):
    a, b = azara_record
    c, d, e = rui_record
    if d == convert_coordinate(b):
        return (azara_record +  rui_record)
    else:
        return "not a match"

