#!/usr/local/bin/python3

class benchParser:
    def __init__(self, filepath):
        self.filepath = filepath
        self.input_list = []
        self.output_list = []
        self.gate_list = []
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
                gtype = strline[strline.index('=')+1:strline.index('(')]
                out = int(strline[:strline.index('=')])
                ins = [int(x) for x in strline[strline.index('(')+1:-2].split(',')]
                self.add_gate((out, gtype, ins))
    def dump(self):
        print(self.input_list)
        print(self.output_list)
        print(self.gate_list)
    def add_input(self, name):
        self.input_list.append(int(name))
    def add_output(self, name):
        self.output_list.append(int(name))
    def add_gate(self, gate):
        self.gate_list.append(gate)


