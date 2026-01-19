# LESSON 3/4
from collections import *
def group_a(words: list[str]) -> list[str]:
    anagrams = defaultdict(list)

    for word in words:
        count =[0] * 26
        for char in word:
            count[ord(char) - ord("a")] += 1
        anagrams[tuple(count)].append(word)
    return list(anagrams.values())

# words = ["eat", "tea", "ate", "pea", "ape"]
# print(group_a(words))


def k_freq_char(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    return [num for num, freq in count.most_common(k)]

# nums = [1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,5,5]
# print(k_freq_char(nums, 2))

import heapq

def heap_k_freq_char(nums: list[int], k: int) -> list[int]:
    count = Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)

# print(heap_k_freq_char(nums,3))

def valid_p(s: str) -> bool:
    stack = []
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:
        if char in  pairs.values():
            stack.append(char)
        else:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack

# s = ("()[]{}")
# print(valid_p(s))

def valid_p1(s: str) -> bool:
    stack = []
    pairs = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for char in s:
        if char in pairs.values():
            stack.append(char)
        else:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None


    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

stack = Stack()

# stack.push(10)
# stack.push(20)
# stack.push(30)
#
# print(stack.size())
# stack.pop()
# print(stack.size())

class Stack2:
    def __init__(self):
        self.items = []

    def empty(self):
        len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.empty():
            return self.items[-1]
        return None


    def pop(self):
        if not self.empty():
            self.items.pop()
        return None

    def push(self, item):
        self.items.append(item)


# st = Stack()
# st.push(1)
# st.push(2)
# st.push(3)
#
# print(st.size())
# st.pop()
# print(st.size())


# LESSON 4/5

def check_valid_p(s: str) -> bool:
    stack = []
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:
        if char in pairs.values():
            stack.append(char)
        else:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return not stack

# s = "([{}])" #true
# print(check_valid_p(s))

class Stack3:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None


    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if not self.is_empty():
            self.items.pop()
        return None


# s = Stack3()
#
# s.push(10)
# s.push(20)
# s.push(30)
#
# print(s.size())
# print(s.peek())
#
# s.pop()
#
# print(s.size())
# print(s.peek())

import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def peek(self):
        if self.heap:
            return self.heap[0][1]
        return None


    def push(self, priority, item):
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        if self.heap:
            priority, item = heapq.heappop(self.heap)
            return item
        return None

# p = PriorityQueue()
#
# p.push(1, "Leonid")
# p.push(3, "Elena")
# p.push(7, "Pavel")
# p.push(1, "Natasha")
#
# print(p.size())
# print(p.peek())
#
# p.pop()
#
# print(p.size())
# print(p.peek())



def valid_parentheses(s: str) -> bool:
    stack = []
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:
        if char in pairs.values():
            stack.append(char)
        else:
            if not stack or stack[-1] != pairs(char):
                return False
            stack.pop()
        return not stack



class Stacks:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None


    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            self.items.pop()
        return None

# s = Stacks()
#
# s.push(10)
# s.push(20)
# s.push(30)
#
# print(s.size())
# print(s.peek())
#
# s.pop()
#
# print(s.size())
# print(s.peek())



class HeapStack:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def peek(self):
        if self.heap:
            return self.heap[0][1]
        return None


    def push(self, priority, item):
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        if self.heap:
            priority, item = heapq.heappop(self.heap)
            return item
        return None

# p = HeapStack()
#
# p.push(1, "Leonid")
# p.push(3, "Elena")
# p.push(7, "Pavel")
# p.push(1, "Natasha")
#
# print(p.size())
# print(p.peek())
#
# p.pop()
#
# print(p.size())
# print(p.peek())



def valid_parentheses1(s:str) -> bool:
    stack = []
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:
        if char in pairs.values():
            stack.append(char)
        else:
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return not stack

# ls = "({[]})"    #true
# print(valid_parentheses1(ls))


class HeapStack3:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def size(self):
        return len(self.heap)

    def peek(self):
        if self.heap:
            return self.heap[0][1]
        return None


    def push(self, priority, item):
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        if self.heap:
            priority, item = heapq.heappop(self.heap)
        return None

# p = HeapStack3()
#
# p.push(1, "Leonid")
# p.push(3, "Elena")
# p.push(7, "Pavel")
# p.push(1, "Natasha")
#
# print(p.size())
# print(p.peek())
#
# p.pop()
#
# print(p.size())
# print(p.peek())



def sliding_window_k(nums: list[int], k: int) -> int:
    if not nums or k <= 0:
        return 0

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

# nums = [1, 3, 2, 6, -1, 4, 1]
# k = 3
# print(sliding_window_k(nums, k))


from collections import *
def sliding_window_dq(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0:
        return 0

    dq = deque()
    result = []

    for i, num in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and nums[dq[-1]] <= num:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
# k = 3
# print(sliding_window_dq(nums, k))


def slide_window(nums: list[int], k: int) -> int:
    if not nums or k >= 0:
        return 0

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, lrn(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


def max_window(nums: list[int], k: int) -> list[int]:
    if not nums or k <= 0:
        return []

    dq = deque()
    result = []

    for i, num in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and nums[dq[-1]] < num:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

# nums = [1,-2,-1,3,6,-8,12]
# print(max_window(nums, 3))



class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def reverse_linked_list_recursive(head):
    if not head or head.next:
        return head

    new_head = reverse_linked_list_recursive(head.next)
    head.next.next = head
    head.next = None

    return new_head

# head = ListNode(1, ListNode(2, ListNode(3)))
# reversed_head = reverse_linked_list_recursive(head)
# cur = reversed_head
# while cur:
#     print(cur.val)
#     cur = cur.next
# print("None")



def merge_two_lists_rec(l1, l2):
    if not l1: return l2
    if not l2: return l1
    if l1.val < l2.val:
        l1.next = merge_two_lists_rec(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists_rec(l1, l2.next)
        return l2

# l1 = ListNode(1, ListNode(3, ListNode(5)))
# l2 = ListNode(2, ListNode(4, ListNode(6)))
# merge = merge_two_lists_rec(l1, l2)
# cur = merge
# while cur:
#     print(cur.val)
#     cur = cur.next
# print("None")



def linked_list_cycle_detection(head):
    fast = head
    slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False

# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(4)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node2  # создаём цикл
# print(linked_list_cycle_detection(node1))  # True
#
# 1 → 2 → 3 → 4 → None (без цикла)
# node4.next = None
# print(linked_list_cycle_detection(node1))



def remove_n_from_end(head, n):
    def helper(node):
        if not node:
            return 0, node
        pos, node.next = helper(node.next)
        pos += 1
        if pos == n:
            return pos, node.next
        return pos, node
    _, new_head = helper(head)
    return new_head

# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# remove = remove_n_from_end(head, 3)
# cur = remove
# while cur:
#     print(cur.val)
#     cur = cur.next
# print("None")



class ListNode2:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    if not head or not head.next:
        return head

    new_head = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None
    return new_head

def merge_two_sort_lists(l1, l2):
    if not l1: return l2
    if not l2: return l1
    if l1.val < l2.val:
        l1.next = merge_two_sort_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_sort_lists(l1, l2.next)
        return l2

def linked_list_cycle_detection(head):
     fast = head
     slow = head

     while fast and fast.next:
         slow = slow.next
         fast = fast.next.next
         if fast == slow:
             return True
     return False

def remove_n_from_end(head, n):
    def helper(node):
        if not node:
            return 0, node
        pos, node.next = helper(node.next)
        pos += 1
        if pos == n:
            return pos, node.next
        return pos, node

    _, new_head = helper(head)
    return new_head


# LESSON 5/6
class LinkedList:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def reverse_list(head):
    if not head or not head.next:
        return head

    new_head = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return new_head

def merge_two_lists(l1, l2):
    if not l1: return l2
    if not l2: return l1
    if l1.val < l2.val:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists(l1, l2.next)
        return l2

def linked_cycle_list(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def remove_from_end(head, n):
    def helper(node):
        if not node:
            return 0, node
        pos, node.next = helper(node.next)
        pos += 1
        if pos == n:
            return pos, node.next
        return pos, node

    _, new_head = helper(head)
    return new_head

# head = LinkedList(1, ListNode(2, ListNode(3)))
# reversed = reverse_list(head)
# cur = reversed
# while cur:
#     print(cur.val, end=" → ")
#     cur = cur.next
# print("None", )
#
#
# l1 = LinkedList(1, ListNode(3, ListNode(5)))
# l2 = LinkedList(2, ListNode(4, ListNode(6)))
# merged = merge_two_lists(l1, l2)
# cur = merged
# while cur:
#     print(cur.val, end=" → ")
#     cur = cur.next
# print("None")
#
#
# node1 = ListNode(1)
# node2 = ListNode(2)
# node3 = ListNode(3)
# node4 = ListNode(4)
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node2  # создаём цикл
# print(linked_cycle_list(node1))  # True
#
# # 1 → 2 → 3 → 4 → None (без цикла)
# node4.next = None
# print(linked_cycle_list(node1))  # False
#
#
# head = LinkedList(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# new = remove_from_end(head, 2)
# cur = new
# while cur:
#     print(cur.val, end=" → ")
#     cur = cur.next
# print("None")


