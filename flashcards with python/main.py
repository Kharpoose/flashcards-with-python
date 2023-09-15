import random
import os


def study():
    global terms
    global term
    term = random.choice(terms)
    terms.remove(term)
    print(term,'::::', len(terms),'/', total_terms)

path = 'file folder'    
files = os.listdir(path)
for file in files:
    if 'txt' not in file:
        files.remove(file)        
#randomize
random.shuffle(files)
for file in files:
    print('#',file,'#')
    file = path+'/'+file
    # read file
    with open(file) as f:
        lines = f.readlines()
    # store file terms
    terms = []
    terms = list(set(terms))
    for line in lines:
        line = line.split(',')
        for l in line:
            terms.append(l)
    # remove blanks
    while '' in terms:
        terms.remove('')
    # Number of total terms
    total_terms = len(terms)
    ###
    # If answer is wrong or unknown
    unknown = []
    for i in range(total_terms):
        study()
        answer = input('y or n: ',)
        if answer == 'n':
            unknown.append(term)
    # Restudy inncorrect answers until you get them right
    while len(unknown) > 0:
        total_terms = len(unknown)
        terms = unknown
        unknown = []
        for i in range(total_terms):
            study()
            answer = input('y or n: ',)
            if answer == 'n':
                unknown.append(term)
        print(unknown)
    # print out some encouragement
    done = ['You rock!','Wonderful donezo!','You got this!','You make this easy','You are becoming a master']
    print(random.choice(done))
print('Alllllll DONE')