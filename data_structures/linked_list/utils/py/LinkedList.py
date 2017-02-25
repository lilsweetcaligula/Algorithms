class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt

    def __repr__(self):
        PRESERVE_AGAINST_CYCLES = True
        DISPLAY_THRESHOLD       = 16

        node  = self
        vals  = []

        if PRESERVE_AGAINST_CYCLES:
            count = 0

        while node != None:
            if PRESERVE_AGAINST_CYCLES:
                if count > DISPLAY_THRESHOLD:
                    break
                count += 1

            vals.append(node.val)
            node = node.nxt

        return('->'.join(map(repr, vals)) 
               + ('...' if count > DISPLAY_THRESHOLD else ''))

    def __str__(self):
        node = self
        vals = []

        while node != None:
            vals.append(node.val)
            node = node.nxt

        return '->'.join(map(str, vals))

def ConvertArrayToLinkedList(values: {list, tuple}=None) -> Node:
    if values == None:
        return None

    dummy = Node(0)
    node  = dummy

    for value in values:
        node.nxt = Node(value)
        node     = node.nxt

    return dummy.nxt

def Equals(left: Node, right: Node) -> bool:
    if left == None and right == None:
        return True

    if left == None or right == None:
        return False

    lnode = left
    rnode = right

    while lnode != None and rnode != None:
        if lnode.val != rnode.val:
            return False
        else:
            lnode = lnode.nxt
            rnode = rnode.nxt
            
    return lnode == None and rnode == None 
