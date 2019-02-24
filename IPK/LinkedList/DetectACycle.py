"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    visitedDict = {}

    if head == None:
        return False

    while head.next != None:
        if head in visitedDict:
            return True
        visitedDict[head] = head.data
        head.next

    return False

