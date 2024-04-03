# Read phonemes_fr.txt file and randomly split lines to train and validation sets
import random

with open('phonemes_fr.txt', 'r') as file:
    lines = file.readlines()

random.shuffle(lines)

train = lines[:int(0.99*len(lines))]
val = lines[int(0.99*len(lines)):]
with open('train_list.txt', 'w') as file:
    file.write(''.join(train))

with open('val_list.txt', 'w') as file:
    file.write(''.join(val))

