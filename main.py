list_1 = [
    {"id": "1", "name": "Shrey", "age": 25},
    {"id": "3", "age": 10, "name": "Hello"},
    {"id": "2", "name": "World", "age": 24},
]

list_2 = [
    {"id": "1", "marks": 100},
    {
        "id": "3",
        "marks": 90,
        "roll_no": 11,
        "extra_info": {
            "hello": "world",
        },
    },
]


def merge_lists(list_1, list_2) -> list:
    """
    Complete this function, by merging the information from list_1 and list_2
    to create a new list, which has all the information about each student from
    both lists in one single dict.

    - Both lists are unsorted
    - Both lists can have missing values (for ex list_2 has missing id=2)
    """
    if (len(list_1) == 0) or (len(list_2) == 0):
        return list_1 or list_2

    for object_one in list_1:
        for object_two in list_2:
            if object_one["id"] == object_two["id"]:
                object_one.update(object_two)
    return list_1

    """
    Time complexity => O(m*n)
    where m and n are length of list_1 and list_2 respectively.
    """


print(merge_lists(list_1, list_2))
