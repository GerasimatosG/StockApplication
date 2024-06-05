from domain.item import Item


def mapItems(data: list):
    items = []
    for row in data:
        item = Item(row[0], row[1], row[2], row[3], row[4])
        items.append(item)
    return items


def mapItemsForAvailability(data: list):
    items = []
    for row in data:
        item = Item(row[0], row[1], row[2], row[3], row[4])
        items.append(item)
    return items[0] if items else None
