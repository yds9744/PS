from linkedlist import Node
from linkedlist import LinkedList

def solution(num1, num2):
    cur1 = num1.head.next
    cur2 = num2.head.next

    answer = LinkedList()
    carry = 0
    while cur1 and cur2:
        # calculate
        tmp = cur1.data + cur2.data + carry
        carry = tmp//10
        tmp = tmp%10
        # add node to answer
        answer.append(tmp)
        # next
        cur1 = cur1.next
        cur2 = cur2.next

    # remain values
    if cur2: cur1 = cur2
    while cur1:
        # calculate
        tmp = cur1.data + carry
        carry = tmp//10
        tmp = tmp%10
        # add node to answer
        answer.append(tmp)
        # next
        cur1 = cur1.next

    # remain carry
    if carry:
        answer.append(carry)

    answer.print()
    return answer


# test
solution(LinkedList([7, 1, 6, 1]), LinkedList([5, 9, 2, 9]))
