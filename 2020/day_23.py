
class Node:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value


class CircularLinkedList:
    def __init__(self, nodes):
        self.head = nodes[0]
        self.min = min(n.value for n in nodes)
        self.max = max(n.value for n in nodes)
        num_to_node_map = {}
        for node in nodes:
            num_to_node_map[node.value] = node
        self.num_to_node = num_to_node_map

    def add(self, after, node):
        node.prev = after
        node.next = after.next
        after.next.prev = node
        after.next = node
        self.num_to_node[node.value] = node

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
            nodes.append(node.value)
        return nodes

    def __repr__(self):
        return str(self.print_list())


class CrabCups:

    def __init__(self, starting_cups, total_cups=None):
        total_cups = total_cups or len(starting_cups)
        cups = starting_cups[:]
        for n in range(len(starting_cups), total_cups):
            cups.append(n+1)
        nodes = [Node(n) for n in use_inp]
        for i in range(len(nodes)):
            prev = i - 1
            if prev < 0:
                prev = len(nodes) - 1
            nodes[i].prev = nodes[prev]

            nxt = i + 1
            if nxt >= len(nodes):
                nxt = 0
            nodes[i].next = nodes[nxt]
        self.llist = CircularLinkedList(nodes)

    def select_destination_cup(self, cups_picked):
        destination = self.current_cup.value - 1
        while True:
            if destination < self.llist.min:
                destination = self.llist.max
            if destination not in [n.value for n in cups_picked]:
                break
            destination -= 1
        dest = self.llist.num_to_node[destination]
        return dest

    @property
    def current_cup(self):
        return self.llist.head

    @current_cup.setter
    def current_cup(self, value):
        self.llist.head = value

    def do_move(self):
        three_cups = self.llist.pick(3)
        dest = self.select_destination_cup(three_cups)
        for cup in three_cups:
            self.llist.add(dest, cup)
            dest = cup
        # advance current cup
        self.current_cup = self.current_cup.next

    def play(self, num_moves):
        for _ in range(num_moves):
            self.do_move()




if __name__ == '__main__':
    # puzzle_input = parse_input('day_23.in')
    # sample_input = parse_input('day_23.in.sample_01')
    # sample_input2 = parse_input('day_23.in.sample_02')

    puzzle_input = [int(c) for c in "135468729"]
    sample_input = [int(c) for c in "389125467"]
    use_inp = sample_input
    # PART2
    # for n in range(len(use_inp)+1, 1000001):
    #     use_inp.append(n)
    # nodes = [Node(n) for n in use_inp]
    # for i in range(len(nodes)):
    #     prev = i -1
    #     if prev < 0:
    #         prev = len(nodes)-1
    #     nodes[i].prev = nodes[prev]
    #
    #     nxt = i + 1
    #     if nxt >= len(nodes):
    #         nxt = 0
    #     nodes[i].next = nodes[nxt]
    #
    # llist = CircularLinkedList(nodes)
    # print(puzzle_input)


    #cups = puzzle_input[:]
    # PART2
    # for n in range(len(cups)+1, 1000001):
    #     cups.append(n)
    game = CrabCups(use_inp)
    #for i in range(100):
        #print(i)
        # three_cups = llist.pick(3)
        # destination = llist.head.data - 1
        # while True:
        #     if destination < llist.min:
        #         destination = llist.max
        #     if destination not in [n.data for n in three_cups]:
        #         break
        #     destination -= 1
        # dest = llist.num_to_node[destination]
        # for cup in three_cups:
        #     llist.add(dest, cup)
        #     dest = cup
        # # advance current cup
        # llist.head = llist.head.next
    game.play(100)

    print(game.llist.print_list())
    # one_index = llist.num_to_node[1]
    # op1 = one_index.next
    # op2 = op1.next
    # print(op1.data * op2.data)







