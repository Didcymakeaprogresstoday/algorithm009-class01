#哑巴节点的创建 游标的使用 明确指针的含义
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #创建哑节点
        hair = ListNode(0)
        #创建游标
        pre = hair
        while l1 and l2:
            if l1.val <= l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        pre.next =  l1 if l1 else l2
        return hair.next     

