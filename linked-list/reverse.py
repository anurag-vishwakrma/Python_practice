# Reverse a Linked List
from traceback import print_list


class LinkNode:

    def __init__(self, val=0, nxt = None):
        self.val = val
        self.nxt = nxt

    @staticmethod
    def print_list(head):
        while head:
            print(head.val, end="-->")
            head=head.nxt
        print(None)

    @staticmethod
    def reverse_linked_list(head):
        current = head
        per = None


        while current:
            nxt = current.nxt
            current.nxt = per
            per = current
            current=nxt

        return per

n1=LinkNode(1)
n2=LinkNode(2)
n3=LinkNode(3)
n4=LinkNode(4)
n1.nxt = n2
n2.nxt = n3
n3.nxt = n4

LinkNode.print_list(n1)

reversed_head = LinkNode.reverse_linked_list(n1)
LinkNode.print_list(reversed_head)
