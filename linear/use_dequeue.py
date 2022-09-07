from collections import deque


ticket_queue = deque()
print(len(ticket_queue))

ticket_queue.append("Jane")
ticket_queue.append("John")
ticket_queue.append("Linda")
print(ticket_queue)

ticket_queue.popleft("Jane")

