def isLengthEvenOrOdd(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next

    return count % 2 == 1