# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def print(self):
        print(self.val, self.next)
        

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: ListNode
        :type list2: ListNode
        :rtype: ListNode
        """
        temp = ListNode()  
        current = temp     

        current1 = list1
        current2 = list2

        while current1 and current2:
            if current1.val <= current2.val:
                current.next = current1
                current1 = current1.next
            else:
                current.next = current2
                current2 = current2.next
            current = current.next 

       
        if current1:
            current.next = current1
        elif current2:
            current.next = current2

        return temp.next
            
            
                
        
    def doTests(self):
        #print(self.mergeTwoLists(
        #    ListNode(1,ListNode(2, ListNode(4)) ), ListNode(1,ListNode(3, ListNode(4) ) )
        #))
        self.mergeTwoLists(ListNode(None), ListNode(None)).print()
        self.mergeTwoLists(ListNode(None, None), ListNode(0, None)).print()


def main():
    Solution().doTests()

if __name__ == '__main__':
    main()