class LinkNode:

    def __init__(self, val=0, nxt = None):
        self.val = val
        self.nxt = nxt

    @staticmethod
    def remove_cycle(head):
        slow = head
        fast = head
        met = False
        while fast and fast.nxt:
            fast = fast.nxt.nxt
            slow = slow.nxt
            if slow == fast:
                print("Loop exists.")
                met = True
                break
        if not met:
            return "Loop exists"
        else:
            while slow!=fast:
                slow = slow.nxt
                fast = fast.nxt
            slow.nxt = None
        return slow


    @staticmethod
    def print_list(head):
        while head:
            print(head.val, end="-->")
            head=head.nxt
        print(None)



n1=LinkNode(1)
n2=LinkNode(2)
n3=LinkNode(3)
n4=LinkNode(4)
n1.nxt = n2
n2.nxt = n3
n3.nxt = n4
n4.nxt = n2


LinkNode.remove_cycle(n1)
LinkNode.print_list(n1)
