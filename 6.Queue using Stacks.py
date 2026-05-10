class QueueUsingStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self,value):
        return self.stack_in.append(value)

    def dequeue(self):
        if not self.stack_out:      #if stack out is empty
            while self.stack_in:    # move everything from stack_in to stack_out
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:  # if still stack out is empty
            print("Empty")
            return None
        return self.stack_out.pop()     # if all move to stack out remove top/last item

    def is_empty(self):
        return not self.stack_out and not self.stack_in

    def size(self):
        return (len(self.stack_in) + len(self.stack_out))

    def front_item(self):
        if not self.stack_out:
            if not self.stack_in:
                print("Empty")
                return None
            return self.stack_in[0]     # If stack_out is empty, then the front must still be sitting at the bottom of stack_in
        return self.stack_out[-1]       #top item of stack out

#    def front_item(self):
#       if self.is_empty():
#            return None
#        if self.stack_out:  # front is at top of stack_out
#           return self.stack_out[-1]
#        return self.stack_in[0]  # otherwise, bottom of stack_in

    def rear_item(self):
        if not self.stack_out and not self.stack_in:
            print("Empty")
            return None
        if self.stack_in:
            return self.stack_in[-1]        # newest in stack_in
        else:
            return self.stack_out[0]     # bottom of stack_out