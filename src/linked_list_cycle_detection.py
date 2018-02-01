"""
https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

"""
Store the address of nodes in a set.

"""


def has_cycle(head):
    if head is None:
        return False
    node_address = set()
    while head.next is not None:
        if id(head) in node_address:
            node_address.add(id(head))
        else:
            return True
    return False


"""
Use two pointers. If there is any circle , both pointers would point to the same location at come time.

"""


def has_cycle_with_pointers(head):
    if head is None:
        return False

    # Can also do with the use of one pointer only [head and fast_pointer]
    slow_pointer = head
    fast_pointer = head

    while fast_pointer.next is not None and fast_pointer.next.next is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
        if slow_pointer == fast_pointer:
            return True
    return False

