#!/usr/local/bin/python3

class Row:
    def __init__(self, path, data, target):
        self.path = path
        self.data = data
        self.target = target

from random import shuffle

class Data:
    def __init__(self, filepath, append_name=""):
        self.filepath = filepath
        self.append_name = append_name
        self.parse()
    def run(self):
        self.split_dataset()
        self.dump()
    def analysis(self):
        print('# of total data:', len(self.dataset))
        print('# of train data:', len(self.train))
        print('% of 1 in train:', len([x for x in self.train if x.target=='1'])/len(self.train))
        print('# of test data:', len(self.test))
        print('% of 1 in test:', len([x for x in self.test if x.target=='1'])/len(self.test))
    def parse(self):
        self.dataset = []
        with open(self.filepath,'r') as infile:
            for strline in infile.readlines():
                elements = strline.rstrip().split(' ')
                d = Row(elements[0],elements[1],elements[2])
                self.dataset.append(d)
    def split_dataset(self):
        num = int(4*len(self.dataset)/5)
        shuffle(self.dataset)
        self.train = self.dataset[:num]
        self.test = self.dataset[num:]
    def dump(self):
        with open('train'+self.append_name+'.data','w') as outfile:
            for d in self.train:
                outfile.write(d.data)
                outfile.write(' ')
                outfile.write(d.target)
                outfile.write('\n')
        with open('train'+self.append_name+'.map','w') as outfile:
            for d in self.train:
                outfile.write(d.path)
                outfile.write(' ')
                outfile.write(d.data)
                outfile.write(' ')
                outfile.write(d.target)
                outfile.write('\n')
        with open('test'+self.append_name+'.data','w') as outfile:
            for d in self.test:
                outfile.write(d.data)
                outfile.write(' ')
                outfile.write(d.target)
                outfile.write('\n')
        with open('test'+self.append_name+'.map','w') as outfile:
            for d in self.test:
                outfile.write(d.path)
                outfile.write(' ')
                outfile.write(d.data)
                outfile.write(' ')
                outfile.write(d.target)
                outfile.write('\n')
    

