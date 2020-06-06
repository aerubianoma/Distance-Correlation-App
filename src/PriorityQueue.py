class PriorityQueue():
       """A basic priority queue that dequeues items with the smallest priority number."""
       def __init__(self):
           """Initializes the queue with no items in it."""
           self.array = []
           self.count = 0

       def enqueue(self, item, priority):
           """Adds an item to the queue."""
           self.array.append([item, priority])
           self.count += 1

       def dequeue(self):
           """Removes the highest priority item (smallest priority number) from the queue."""
           max = -1
           dq = 0
           if(self.count > 0):
               self.count -= 1

               for i in range(len(self.array)):
                   if self.array[i][1] != None and self.array[i][1] > max:
                       max = self.array[i][1]

               if max == -1:
                   return self.array.pop(0)
               else:
                   for i in range(len(self.array)):
                       if self.array[i][1] != None and self.array[i][1] <= max:
                           max = self.array[i][1]
                           dq = i
                   return self.array.pop(dq)

       def requeue(self, item, newPrio):
           """Changes specified item's priority."""
           for i in range(len(self.array)):
               if self.array[i][0] == item:
                   self.array[i][1] = newPrio
                   break

       def returnArray(self):
           """Returns array representation of the queue."""
           return self.array

       def size(self):
           """Returnes the length of the queue."""
           return self.count
