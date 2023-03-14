l1 = [2,4,3]
l2 = [5,6,4]

class lstnode:
    def addtwonum(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = l1
        b = l2

        arr1 = []
        arr2 = []

        while a:
            arr1.append(a.val)
            a = a.next

        while b:
            arr2.append(b.val)
            b = b.next

        arr1.reverse()
        arr2.reverse()

        inta = int("".join(str(x) for x in arr1)) #converting list to string
        intb = int("".join(str(x) for x in arr2))

        c = list(str(inta + intb))

        head = l3 = ListNode(c.pop())

        c.reverse()

        #traverse remaining digits, assigning  each to new ListNode
        for i in c:
            l3.next = ListNode(i)
            l3 = l3.next

        return head
    
lstnode.addtwonum(l1,l2)