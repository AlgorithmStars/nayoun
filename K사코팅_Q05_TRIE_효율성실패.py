class CharTrieNode(object):
    def __init__(self, char):
        self.char = char
        self.cnt = 1
        self.children = dict() # key: char, value: node address

        # 그야말로 문제를 위한 변수
        self.child_strings = []

    def get_char(self):
        return self.char

    def get_children(self):
        return self.children

    def get_children_chars(self):
        return self.children.keys()

    def get_child_with_char(self, char):
        return self.children[char]

    def get_cnt(self):
        return self.cnt

    def get_child_strings(self):
        return self.child_strings

    def add_child(self, char, child_node):
        self.children[char] = child_node

    def add_cnt(self):
        self.cnt += 1

    def add_child_strings(self, child_str):
        self.child_strings.append(child_str)


class CharTrie(object):
    def __init__(self, words):
        self.words = words # data
        self.root = CharTrieNode('.')

        for word in self.words:
            self.insert_word(word)

    def insert_word(self, word):
        _parent = self.root

        for idx in range(len(word)):
            char = word[idx]
            p_chars = _parent.get_children_chars()

            if char in p_chars:
                cur = _parent.get_child_with_char(char)
                cur.add_cnt()
                cur.add_child_strings(word[idx + 1:])

                _parent = cur

            else:
                new_child = CharTrieNode(char)
                new_child.add_child_strings(word[idx + 1:])

                _parent.add_child(char, new_child)
                _parent = new_child

    def print_trie(self, ):
        self._print(self.root, 1)


    def _print(self, node, depth):
        print('\t' * depth, 'char: {}, cnt: {}, child_strs: {}'.format(
                    node.get_char(), node.get_cnt(), node.get_child_strings()))
        if node.get_children() == dict():
            return

        children = node.get_children()
        for child in children:
            self._print(children[child], depth + 1)


    # for KAKAO CF part 5
    def get_query_cnt(self, query, n_wild):
        _parent = self.root

        for char in query:
            _p_chars = _parent.get_children_chars()
            if char not in _p_chars:
                return 0

            cur = _parent.get_child_with_char(char)
            _parent = cur

        # return _parent.get_cnt()
        parent_child_strings = _parent.get_child_strings()
        searched = list(filter(lambda x: len(x) == n_wild, parent_child_strings))

        return len(searched)


def solution(words, queries):
    WILD = '?'
    forward_trie = CharTrie(words)

    reversed_words = [w[::-1] for w in words]
    reverse_trie = CharTrie(reversed_words)

    num_searched = []
    for query in queries:
        if query[-1] == WILD:
            wild_idx = query.index(WILD)
            n_wild = len(query) - wild_idx
            result = forward_trie.get_query_cnt(query[:wild_idx], n_wild)

        else:
            query = query[::-1]
            wild_idx = query.index(WILD)
            n_wild = len(query) - wild_idx
            result = reverse_trie.get_query_cnt(query[:wild_idx], n_wild)

        num_searched.append(result)

    return num_searched



if __name__ == '__main__':
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
    answer = solution(words, queries)
    print(answer)