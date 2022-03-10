# Linked List : Dictionary Comprehension

head = {
    "value": 10,
    "next": {
        "value": 11,
        "next": {
            "value": 12,
            "next": {
                "value": 13,
                "next": {
                    "value": 7,
                    "next": None
                }
            }

        }
    }
}

print(head["next"]["next"]["value"])

# linked list

print(my_ll.head.next.next.value)
