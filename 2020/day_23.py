class Node:

    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value


class CircularLinkedList:

    def __init__(self, nodes):
        for i in range(len(nodes)):
            nodes[i].prev = nodes[i - 1 if i - 1 >= 0 else len(nodes) - 1]
            nodes[i].next = nodes[i + 1 if i + 1 < len(nodes) else 0]
        self.head = nodes[0]

    def insert_nodes(self, nodes, after=None):
        after = after or self.head
        before = after.next

        nodes[0].prev = after
        nodes[-1].next = before

        before.prev = nodes[-1]
        after.next = nodes[0]

    def traverse(self, starting_point=None):
        starting_point = starting_point or self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node


class CrabCups:

    def __init__(self, starting_cups, total_cups=None):
        total_cups = total_cups or len(starting_cups)
        all_cups = starting_cups[:]
        for n in range(len(starting_cups), total_cups):
            all_cups.append(n + 1)
        nodes = [Node(n) for n in all_cups]
        self.llist = CircularLinkedList(nodes)
        self.cup_min = min(n.value for n in self.llist.traverse())
        self.cup_max = max(n.value for n in self.llist.traverse())
        self.value_to_node = {}
        for node in nodes:
            self.value_to_node[node.value] = node

    def pick(self, how_many_to_pick):
        picks = []
        ptr = self.current_cup
        for i in range(how_many_to_pick):
            ptr = ptr.next
            picks.append(ptr)
        self.current_cup.next = ptr.next
        ptr.next.prev = self.current_cup
        return picks

    def select_destination_cup(self, cups_picked):
        dest_cup_value = self.current_cup.value - 1
        while True:
            if dest_cup_value < self.cup_min:
                dest_cup_value = self.cup_max
            if dest_cup_value not in [n.value for n in cups_picked]:
                break
            dest_cup_value -= 1
        destination = self.value_to_node[dest_cup_value]
        return destination

    def insert_cups(self, cups_to_insert, after):
        self.llist.insert_nodes(cups_to_insert, after)

    @property
    def current_cup(self):
        return self.llist.head

    @current_cup.setter
    def current_cup(self, value):
        self.llist.head = value

    def do_move(self):
        cups_picked = self.pick(3)
        destination = self.select_destination_cup(cups_picked)
        self.insert_cups(cups_picked, destination)
        self.current_cup = self.current_cup.next

    def play(self, num_moves):
        for _ in range(num_moves):
            self.do_move()
        return self

    def get_cups(self, starting_cup=None, starting_with_cup_value=None):
        starting_cup = starting_cup or self.current_cup
        if starting_with_cup_value:
            starting_cup = self.value_to_node[starting_with_cup_value]
        return list(self.llist.traverse(starting_cup))

    def get_cup_by_value(self, value):
        return self.value_to_node[value]


if __name__ == '__main__':
    puzzle_input = [int(c) for c in '135468729']
    sample_input = [int(c) for c in '389125467']

    # Part 1
    cups = CrabCups(sample_input).play(100).get_cups(starting_with_cup_value=1)
    assert ''.join([str(cup.value) for cup in cups[1:]]) == '67384529'

    cups = CrabCups(puzzle_input).play(100).get_cups(starting_with_cup_value=1)
    print(''.join([str(cup.value) for cup in cups[1:]]))

    # Part 2
    cup = CrabCups(sample_input, total_cups=1000000).play(10000000).get_cup_by_value(1)
    assert cup.next.value * cup.next.next.value == 149245887792

    cup = CrabCups(puzzle_input, total_cups=1000000).play(10000000).get_cup_by_value(1)
    print(cup.next.value * cup.next.next.value)
