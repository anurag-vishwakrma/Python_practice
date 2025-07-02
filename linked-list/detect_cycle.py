# Check if the linked list has a loop


class LinkNode:

    def __init__(self, val=0, nxt = None):
        self.val = val
        self.nxt = nxt

    # @staticmethod
    # def is_loop_exist(node):
    #     visited = set()
    #     current = node
    #     while current:
    #         if current in visited:
    #             print("Loop exists.")
    #             return True
    #         visited.add(current)
    #         current = current.nxt
    #     print("Loop does not exist.")
    #     return False

    # Floyd's Tortoise and Hare Algorithm
    @staticmethod
    def is_loop_exist(node):
        slow = node
        fast = node
        while fast and fast.nxt:
            fast = fast.nxt.nxt
            slow = slow.nxt
            if slow == fast:
                print("Loop exists.")
                return True
        print("Loop does not exist.")
        return False


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
n4.nxt = n3

# LinkNode.print_list(n1)
LinkNode.is_loop_exist(n1)


