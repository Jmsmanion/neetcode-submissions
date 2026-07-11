class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.head = ListNode(-1, -1)

    def put(self, key: int, value: int) -> None:
        cur = self.head
        while cur:
            if cur.key == key:
                cur.value = value
                return
            if not cur.next:
                break
            cur = cur.next 
        cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        cur = self.head.next
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        prev = self.head
        while prev.next:
            if prev.next.key == key:
                prev.next = prev.next.next
                return
            prev = prev.next