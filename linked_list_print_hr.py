'''
PLATFORM - HackerRank
QUESTION CODE - Null
QUESTION LINK - https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem
THIS SOLUTION AUTHOR - avrlsngh

Program to add and print the added elements in a singly linked list.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

if __name__ == "__main__":
    n = int(input())
    llist = LinkedList()
    data = int(input())
    llist.head = Node(data)
    p = llist.head
    for _ in range(n-1):
        data = int(input())
        temp = Node(data)
        p.next = temp
        p = p.next

    p = llist.head
    for _ in range(n):
        print(p.data)
        p = p.next