class Node:
    def __init__(self, char, freq):
        self.left = None
        self.right = None
        self.father = None
        self.char = char
        self.freq = freq

    def is_left(self):
        return self.father.left == self

    def is_right(self):
        return self.father.right == self


def count_freq(text):
    freq_map = {}
    for c in text:
        if c not in freq_map:
            freq_map[c] = (text.count(c), '')
    return freq_map


def create_huffman_tree(nodes):
    queue = nodes[:]
    while len(queue) > 1:
        queue.sort(key=lambda item: item.freq)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = Node(None, node_left.freq + node_right.freq)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        queue.append(node_father)
    queue[0].father = None
    return queue[0]


def huffman_encoding(nodes, root, freq_map):
    for i, n in enumerate(nodes):
        node_tmp = n
        while node_tmp != root:
            if node_tmp.is_left():
                freq_map[n.char] = (freq_map[n.char][0], '0' + freq_map[n.char][1])
            else:
                freq_map[n.char] = (freq_map[n.char][0], '1' + freq_map[n.char][1])
            node_tmp = node_tmp.father
    return freq_map


def encode(text, freq_map):
    huffman_str = ''
    for char in text:
        huffman_str += freq_map[char][1]
    return huffman_str


def huffman_decode(huffman_str, freq_map):
    origin_str = ''
    while huffman_str != '':
        for k, v in freq_map.items():
            if v in huffman_str and huffman_str.index(v) == 0:
                origin_str += k
                huffman_str = huffman_str[len(v):]
    return origin_str


def huffman_encode(text):
    freq_map = count_freq(text)
    nodes = [Node(c, t[0]) for c, t in freq_map.items()]
    root = create_huffman_tree(nodes)
    freq_map = huffman_encoding(nodes, root, freq_map)
    encoded_str = encode(text, freq_map)
    return freq_map, root, nodes, encoded_str
