#!/usr/local/bin/python3

ev_template = ['AND','OR','NAND','NOR','XOR','XNOR','INV','BUF']

def exists(x, template):
    if template in x:
        return '1'
    else:
        return '0'

existence_vector = lambda x: ''.join([exists(x, t) for t in ev_template])

class circuit:
    def __init__(self, parser):
        self.parser = parser
    def generate_existence_matrix(self, rows):
        # print(self.parser.fanout_map)
        dev_map = {}
        for gate in self.parser.get_gates():
            # print(gate)
            name = gate[0]
            gtype = gate[1]
            fanins = gate[2]
            fanins_gtype = [self.parser.get_gtype(g) for g in fanins]
            fanouts = self.parser.get_fanout(gate[0])
            fanouts_gtype = [self.parser.get_gtype(g) for g in fanouts]
            # print('\t',fanouts, fanouts_gtype)
            # print('fanin ev:',existence_vector(fanins_gtype),'fanout ev:',existence_vector(fanouts_gtype))
            dev = existence_vector(fanins_gtype+fanouts_gtype)
            # print('dev:',dev)
            if dev in dev_map:
                dev_map[dev] += 1
            else:
                dev_map[dev] = 1
        repr_map = {}
        for key, value in dev_map.items():
            if value in repr_map:
                repr_map[value]+=[key]
            else:
                repr_map[value]=[key]
        # print(repr_map)
        representative_matrix = []
        for key, value in sorted(repr_map.items(),reverse=True):
            for item in value:
                if len(representative_matrix) < rows:
                    representative_matrix.append(item)
                    # print(key)
                else:
                    return representative_matrix
        if len(representative_matrix) < rows:
            empty_vector = existence_vector([])
            for idx in range(rows - len(representative_matrix)):
                representative_matrix.append(empty_vector)
        return representative_matrix
    def xor_tree_detection(self):
        self.xor_cache = {}
        for gate in self.parser.get_gates():
            if self.is_xor(gate):
                # check fanout xors
                # check fanin xors
                # print('check', gate)
                xor_length = self.traverse_fanout(gate) + self.traverse_fanin(gate)
                # print(xor_length)
                if xor_length > 10:
                    # print('detect xor tree')
                    return 1
        return 0
    def traverse_fanout(self, gate):
        if gate[0] in self.xor_cache:
            return self.xor_cache[gate[0]]
        result = [self.traverse_fanout(g) for g in self.fanout_xors(gate)]
        if result:
            if self.is_xor(gate):
                self.xor_cache[gate[0]] = max(result)+1
                return max(result)+1
            else:
                self.xor_cache[gate[0]] = max(result)
                return max(result)
        else:
            self.xor_cache[gate[0]] = 0
            return 0
    def traverse_fanin(self, gate):
        if gate[0] in self.xor_cache:
            return self.xor_cache[gate[0]]
        result = [self.traverse_fanin(g) for g in self.fanin_xors(gate)]
        if result:
            if self.is_xor(gate):
                self.xor_cache[gate[0]] = max(result)+1
                return max(result)+1
            else:
                self.xor_cache[gate[0]] = max(result)
                return max(result)
        else:
            self.xor_cache[gate[0]] = max(result)+1
            return 0
    def fanout_xors(self, gate):
        return [gate for gate in [self.parser.get_gate(idx) for idx in self.parser.get_fanout(gate[0])] if self.is_xor(gate) or self.is_buf(gate)]
    def fanin_xors(self, gate):
        return [gate for gate in [self.parser.get_gate(idx) for idx in gate[2]] if self.is_xor(gate) or self.is_buf(gate)]
    def is_buf(self, gate):
        if gate[1] == 'BUF' or gate[1] == 'NOT' or gate[1] == 'INV':
            return True
        else:
            return False
    def is_xor(self, gate):
        if gate[1] == 'XOR' or gate[1] == 'XNOR':
           return True
        else:
           return False
    def generate_target(self):
        return self.xor_tree_detection()

