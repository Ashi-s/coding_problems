
class ALNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.arbitrary = None

def deepCopy(head):
    if head == None:
        return None

    current = head

    while current != None:
        new = ALNode(current.value)
        new.next = current.next
        current.next = new
        current = current.next.next

    current = head
    while current != None:
        current.next.arbitrary = current.arbitrary.next
        current = current.next.next

    current = head
    new_root = head.next
    while current.next != None:
        temp = current.next
        current.next = current.next.next
        current = temp

    return new_root
