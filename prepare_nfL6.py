import os
import json
import random

fin = json.load(open('nfL6.json', 'r'))

fout_folder = 'nfL6/'
if os.path.exits

fout_train_source = open('train.source', 'w')
fout_train_target = open('train.target', 'w')
fout_valid_source = open('val.source', 'w')
fout_valid_target = open('val.target', 'w')
fout_test_source = open('test.source', 'w')
fout_test_target = open('test.target', 'w')

print(len(fin))

for item in fin:

    Q = item['question']
    A = item['answer']

    rvalue = random.random()

    if 0 <= rvalue <= 0.8:
        fout_train_source.write('{}\n'.format(A))
        fout_test_target.write('{}\n'.format(Q))

    elif 0.8 < rvalue <= 0.9:
        fout_valid_source.write('{}\n'.format(A))
        fout_valid_target.write('{}\n'.format(Q))

    else:
        fout_test_source.write('{}\n'.format(A))
        fout_test_target.write('{}\n'.format(Q))


