class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    l3 = dummy
    carry = 0

    while l1 or l2 or carry:
        dig1 = l1.value if l1 else 0
        dig2 = l2.value if l2 else 0

        total = dig1 + dig2 + carry
        carry = total // 10
        
        l3.next = ListNode(total % 10)
        
        l1 = l1.next
        l2 = l2.next
        l3 = l3.next

    return dummy.next