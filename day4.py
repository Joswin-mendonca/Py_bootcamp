queue = [3,4,5]
queue
def enqueue(num):
    return queue.append(num)
def dequeue():
    return queue.pop()
n = int(input("Enter 1 to push and 2 to pop:"))
if(n==1):
    num = int(input("Enter the number to push")) 
    enqueue(num)
else:
    dequeue()
queue