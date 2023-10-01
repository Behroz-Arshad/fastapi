def noteEntity(item) -> dict:
    dic = {
        "id": str(item['id']),
        "title": item['title'],
        "desc": item['desc']
    }
    return dic


def notesEntity(items) -> list:
    notes_list = [noteEntity(item) for item in items]
    return notes_list
