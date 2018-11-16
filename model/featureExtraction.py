#!/usr/local/bin/python3


class circuit:
    def __init__(self, parser):
        self.parser = parser
    def generate_existence_matrix(self):
        print(self.parser.fanout_map)
        for gate in self.parser.get_gates():
            print(gate)
            fanouts = self.parser.get_fanout(gate[0])
            print('\t', fanouts)
        return []

