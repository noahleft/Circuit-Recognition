#!/usr/local/bin/python3

class benchParser:
    def __init__(self, filepath):
        self.filepath = filepath
        self.input_list = []
        self.output_list = []
        self.gate_map = {}
        self.fanout_map = {}
        self.read()
    def read(self):
        with open(self.filepath) as infile:
            self.strlines = infile.readlines()
        for strline in self.strlines:
            if "INPUT" in strline:
                self.add_input(strline[6:-2])
            if "OUTPUT" in strline:
                self.add_output(strline[7:-2])
            if '=' in strline:
                gtype = strline[strline.index('=')+1:strline.index('(')].replace(' ','')
                out = int(strline[:strline.index('=')])
                ins = [int(x) for x in strline[strline.index('(')+1:-2].split(',')]
                self.add_gate((out, gtype, ins))
    def dump(self):
        print(self.input_list)
        print(self.output_list)
        print(self.gate_map)
    def add_input(self, name):
        self.input_list.append(int(name))
    def get_input(self):
        return self.input_list
    def add_output(self, name):
        self.output_list.append(int(name))
    def get_output(self):
        return self.output_list
    def add_gate(self, gate):
        self.gate_map[gate[0]] = gate
        self.add_fanout(gate)
    def add_fanout(self, gate):
        for fanin in gate[2]:
            if fanin in self.fanout_map:
                self.fanout_map[fanin].append(gate[0])
            else:
                self.fanout_map[fanin] = [gate[0]]
    def get_gate(self, idx):
        if idx in self.gate_map:
            return self.gate_map[idx]
        elif idx in self.input_list:
            return (idx, 'INPUT', [])
        else:
            return None
    def get_gates(self):
        return self.gate_map.values()
    def get_fanout(self, idx):
        if idx in self.fanout_map:
            return self.fanout_map[idx]
        else:
            return []
    def get_gtype(self, idx):
        if idx in self.gate_map:
            return self.gate_map[idx][1]
        else:
            return 'INPUT'


