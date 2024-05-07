# insert the element in the heap
def heappush(heap, item):
    # Append the new item to the heap.
    heap.append(item)
    # Rebalance the heap by moving the new item up to its correct position.
    siftdown(heap, 0, len(heap) - 1)

#remove the element from the heap
def heappop(heap):
    # Check if the heap is empty.
    if not heap:
        raise IndexError("pop from empty heap")
    # Remove and return the smallest item from the heap.
    lastelt = heap.pop()
    # If the heap is not empty, move the last item to the root position and rebalance the heap.
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        siftup(heap, 0)
        return returnitem
    # If the heap was originally empty, return the last item.
    return lastelt

# Rebalance the heap by moving the new item up to its correct position.
def siftdown(heap, startpos, pos):
    # Move the item at pos down to its correct position in the heap.
    newitem = heap[pos] #get the new item.
    # Continue moving the item down until it is at its correct position.
    while pos > startpos: #searching for parent node of new item.
        parentpos = (pos - 1) >> 1 #parent will be at the left of the new item
        parent = heap[parentpos] #get parent node.
        if newitem < parent: #in min heap the child node is greater than or equal to the parent node.
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem

#  move a newly inserted element up the heap to its correct position by comparing it with its parent and swapping if necessary.
def siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up to its final resting place (by sifting its parent down).
    heap[pos] = newitem
    siftdown(heap, startpos, pos)
