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
    def collapse_xor(self, filepath):
        index = 20000
        with open(filepath,'w') as outfile:
            for strline in self.strlines:
                if "XOR" in strline or "XNOR" in strline:
                    gtype = strline[strline.index('=')+1:strline.index('(')].replace(' ','')
                    out = int(strline[:strline.index('=')])
                    ins = [int(x) for x in strline[strline.index('(')+1:-2].split(',')]
                    if len(ins) > 2:
                        if gtype == "XNOR":
                            outfile.write(str(out)+' = NOT('+str(index)+')\n')
                        else:
                            outfile.write(str(out)+' = BUF('+str(index)+')\n')
                        if len(ins) == 3:
                            outfile.write(str(index)+' = XOR('+str(ins[0])+','+str(index+1)+')\n')
                            outfile.write(str(index+1)+' = XOR('+str(ins[1])+','+str(ins[2])+')\n')
                            index = index+2
                        elif len(ins) == 4:
                            outfile.write(str(index)+' = XOR('+str(index+1)+','+str(index+2)+')\n')
                            outfile.write(str(index+1)+' = XOR('+str(ins[0])+','+str(ins[1])+')\n')
                            outfile.write(str(index+2)+' = XOR('+str(ins[2])+','+str(ins[3])+')\n')
                            index = index+3
                        elif len(ins) == 5:
                            outfile.write(str(index)+' = XOR('+str(index+1)+','+str(index+2)+')\n')
                            outfile.write(str(index+1)+' = XOR('+str(ins[0])+','+str(ins[1])+')\n')
                            outfile.write(str(index+2)+' = XOR('+str(ins[2])+','+str(index+3)+')\n')
                            outfile.write(str(index+3)+' = XOR('+str(ins[3])+','+str(ins[4])+')\n')
                            index = index+4
                        elif len(ins) > 8:
                            outfile.write(str(index)+' = XOR('+str(index+1)+','+str(index+2)+')\n')
                            outfile.write(str(index+1)+' = XOR('+','.join([str(x) for x in ins[:5]])+')\n')
                            outfile.write(str(index+2)+' = XOR('+','.join([str(x) for x in ins[5:]])+')\n')
                            index = index+3
                        elif len(ins) > 5:
                            outfile.write(str(index)+' = XOR('+str(index+1)+','+str(index+2)+')\n')
                            outfile.write(str(index+1)+' = XOR('+','.join([str(x) for x in ins[:3]])+')\n')
                            outfile.write(str(index+2)+' = XOR('+','.join([str(x) for x in ins[3:]])+')\n')
                            index = index+3
                    else:
                        outfile.write(strline)
                else:
                    outfile.write(strline)
    def convert_xor(self, filepath):
        index = 40000
        with open(filepath,'w') as outfile:
            for strline in self.strlines:
                if "XOR" in strline or "XNOR" in strline:
                    gtype = strline[strline.index('=')+1:strline.index('(')].replace(' ','')
                    out = int(strline[:strline.index('=')])
                    ins = [int(x) for x in strline[strline.index('(')+1:-2].split(',')]
                    if gtype == "XNOR":
                        outfile.write(str(out)+' = NOT('+str(index)+')\n')
                    else:
                        outfile.write(str(out)+' = BUF('+str(index)+')\n')
                    if len(ins) == 2:
                        outfile.write(str(index)+' = OR('+str(index+1)+','+str(index+2)+')\n')
                        outfile.write(str(index+1)+' = AND('+str(ins[0])+','+str(index+3)+')\n')
                        outfile.write(str(index+2)+' = AND('+str(ins[1])+','+str(index+4)+')\n')
                        outfile.write(str(index+3)+' = NOT('+str(ins[1])+')\n')
                        outfile.write(str(index+4)+' = NOT('+str(ins[0])+')\n')
                        index = index+5
                    elif len(ins) == 3:
                        outfile.write(str(index)+' = OR('+str(index+1)+','+str(index+2)+')\n')
                        outfile.write(str(index+1)+' = AND('+str(ins[0])+','+str(index+3)+')\n')
                        outfile.write(str(index+2)+' = AND('+str(index+5)+','+str(index+4)+')\n')
                        outfile.write(str(index+3)+' = NOT('+str(index+5)+')\n')
                        outfile.write(str(index+4)+' = NOT('+str(ins[0])+')\n')
                        outfile.write(str(index+5)+' = OR('+str(index+6)+','+str(index+7)+')\n')
                        outfile.write(str(index+6)+' = AND('+str(ins[2])+','+str(index+8)+')\n')
                        outfile.write(str(index+7)+' = AND('+str(ins[1])+','+str(index+9)+')\n')
                        outfile.write(str(index+8)+' = NOT('+str(ins[1])+')\n')
                        outfile.write(str(index+9)+' = NOT('+str(ins[2])+')\n')
                        index = index+10
                    elif len(ins) == 4:
                        outfile.write(str(index)+' = OR('+str(index+1)+','+str(index+2)+')\n')
                        outfile.write(str(index+1)+' = AND('+str(index+10)+','+str(index+3)+')\n')
                        outfile.write(str(index+2)+' = AND('+str(index+5)+','+str(index+4)+')\n')
                        outfile.write(str(index+3)+' = NOT('+str(index+5)+')\n')
                        outfile.write(str(index+4)+' = NOT('+str(index+10)+')\n')
                        outfile.write(str(index+5)+' = OR('+str(index+6)+','+str(index+7)+')\n')
                        outfile.write(str(index+6)+' = AND('+str(ins[0])+','+str(index+8)+')\n')
                        outfile.write(str(index+7)+' = AND('+str(ins[1])+','+str(index+9)+')\n')
                        outfile.write(str(index+8)+' = NOT('+str(ins[1])+')\n')
                        outfile.write(str(index+9)+' = NOT('+str(ins[0])+')\n')
                        outfile.write(str(index+10)+' = OR('+str(index+11)+','+str(index+12)+')\n')
                        outfile.write(str(index+11)+' = AND('+str(ins[2])+','+str(index+13)+')\n')
                        outfile.write(str(index+12)+' = AND('+str(ins[3])+','+str(index+14)+')\n')
                        outfile.write(str(index+13)+' = NOT('+str(ins[3])+')\n')
                        outfile.write(str(index+14)+' = NOT('+str(ins[2])+')\n')
                        index = index+15
                    elif len(ins) == 5:
                        outfile.write(str(index)+' = OR('+str(index+1)+','+str(index+2)+')\n')
                        outfile.write(str(index+1)+' = AND('+str(index+10)+','+str(index+3)+')\n')
                        outfile.write(str(index+2)+' = AND('+str(index+5)+','+str(index+4)+')\n')
                        outfile.write(str(index+3)+' = NOT('+str(index+5)+')\n')
                        outfile.write(str(index+4)+' = NOT('+str(index+10)+')\n')
                        outfile.write(str(index+5)+' = OR('+str(index+6)+','+str(index+7)+')\n')
                        outfile.write(str(index+6)+' = AND('+str(ins[0])+','+str(index+8)+')\n')
                        outfile.write(str(index+7)+' = AND('+str(ins[1])+','+str(index+9)+')\n')
                        outfile.write(str(index+8)+' = NOT('+str(ins[1])+')\n')
                        outfile.write(str(index+9)+' = NOT('+str(ins[0])+')\n')
                        outfile.write(str(index+10)+' = OR('+str(index+11)+','+str(index+12)+')\n')
                        outfile.write(str(index+11)+' = AND('+str(ins[2])+','+str(index+13)+')\n')
                        outfile.write(str(index+12)+' = AND('+str(index+15)+','+str(index+14)+')\n')
                        outfile.write(str(index+13)+' = NOT('+str(index+15)+')\n')
                        outfile.write(str(index+14)+' = NOT('+str(ins[2])+')\n')
                        outfile.write(str(index+15)+' = OR('+str(index+16)+','+str(index+17)+')\n')
                        outfile.write(str(index+16)+' = AND('+str(ins[4])+','+str(index+18)+')\n')
                        outfile.write(str(index+17)+' = AND('+str(ins[3])+','+str(index+19)+')\n')
                        outfile.write(str(index+18)+' = NOT('+str(ins[3])+')\n')
                        outfile.write(str(index+19)+' = NOT('+str(ins[4])+')\n')
                        index = index+20
                    else:
                        print('gg')
                        print(gtype, out, ins)
                        exit()
                else:
                    outfile.write(strline)
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


