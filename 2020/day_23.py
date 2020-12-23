
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"{self.prev.data} <- {self.data} -> {self.next.data}"

class CircularLinkedList:
    def __init__(self, nodes):
        self.head = nodes[0]
        self.min = min(n.data for n in nodes)
        self.max = max(n.data for n in nodes)
        num_to_node_map = {}
        for node in nodes:
            num_to_node_map[node.data] = node
        self.num_to_node = num_to_node_map

    def add(self, after, node):
        node.prev = after
        node.next = after.next
        after.next.prev = node
        after.next = node
        self.num_to_node[node.data] = node

    def remove(self, node):
        if self.head == node:
            self.head = node.next
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def pick(self, num_to_pick):
        picks = []
        for i in range(num_to_pick):
            picks.append(self.remove(self.head.next))
        return picks

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        nodes = []
        for node in self.traverse(starting_point):
            nodes.append(node.data)
        return nodes

    def __repr__(self):
        return str(self.print_list())


if __name__ == '__main__':
    # puzzle_input = parse_input('day_23.in')
    # sample_input = parse_input('day_23.in.sample_01')
    # sample_input2 = parse_input('day_23.in.sample_02')

    puzzle_input = [int(c) for c in "135468729"]
    sample_input = [int(c) for c in "389125467"]
    use_inp = puzzle_input
    # PART2
    for n in range(len(use_inp)+1, 1000001):
        use_inp.append(n)
    nodes = [Node(n) for n in use_inp]
    for i in range(len(nodes)):
        prev = i -1
        if prev < 0:
            prev = len(nodes)-1
        nodes[i].prev = nodes[prev]

        nxt = i + 1
        if nxt >= len(nodes):
            nxt = 0
        nodes[i].next = nodes[nxt]

    llist = CircularLinkedList(nodes)
    # print(puzzle_input)


    cups = puzzle_input[:]
    # PART2
    # for n in range(len(cups)+1, 1000001):
    #     cups.append(n)

    for i in range(10000000):
        #print(i)
        three_cups = llist.pick(3)
        destination = llist.head.data - 1
        while True:
            if destination < llist.min:
                destination = llist.max
            if destination not in [n.data for n in three_cups]:
                break
            destination -= 1
        dest = llist.num_to_node[destination]
        for cup in three_cups:
            llist.add(dest, cup)
            dest = cup
        # advance current cup
        llist.head = llist.head.next

    # print(llist.print_list())
    one_index = llist.num_to_node[1]
    op1 = one_index.next
    op2 = op1.next
    print(op1.data * op2.data)







