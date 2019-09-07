import os
def tokenize(docID):
    list_words = []
    with open(docID,'r') as doc:
        content = doc.read()
        content = content.lower()
        text = content.split(' ')
        for  word in text:
            if not word in '\\n , . ? !'.split():
                list_words.append(word)
    return list_words

dict_words = dict()

def wordvec(list_words,id):
    set_words = set(list_words)
    for word in set_words:
        if word not in 'is,the,a,an,have,of,for,was,will,were,often,this,that,it,can,who,whom,what,and,or,upon'.split(','):
            if not word in dict_words:
                dict_words.__setitem__(word,[0,0,0,0,0,0,0,0,0,0])
                dict_words[word][id] = 1
            else:
                dict_words[word][id] = 1
    return 0

def op_not(vec):
    for i in range(len(vec)):
        if vec[i] == 0:
            vec[i]=1
        else:
            vec[i] =0
    return vec

def op_and(vec1,vec2):
    res = []
    for i,j in zip(vec1,vec2):
        res.append(i*j)
    return res

def op_or(vec1,vec2):
    res = []
    for i,j in zip(vec1,vec2):
        if i==1 or j==1:
            res.append(1)
        else:
            res.append(0)
    return res

def query_process(query):
    query = query.lower()
    query = query.split(' ')

    list_operands = []
    list_operations = []
    vec_operands = []
    for word in query:
        if word[0] == "\\":
            list_operations.append(word)
        else:
            list_operands.append(word)
            try:
                vec_operands.append(dict_words[word])
            except KeyError:
                print('word not in corpus')

    for word in list_operands:
        print(word,dict_words[word])

    count_not = 0
    for operation in list_operations:
        if operation =='\\not':
            vec_operands[count_not] = op_not(vec_operands[count_not])
            count_not +=1

    operation_count = 0

    res = vec_operands[0]
    for operation in list_operations:
        if operation == '\\and':
            operation_count+=1
            res = op_and(res,vec_operands[operation_count])
        elif operation =='\\or':
            operation_count+=1
            res = op_or(res,vec_operands[operation_count])
    return res


def writeFile_inverted_index(dict_words):
    fileInvI = 'invertedIndex.txt'
    with open(fileInvI,'w+') as file:
        for term,postingsList in dict_words.items():
            file.write(term)
            for ind,val in enumerate(postingsList):
                if val == 1:
                    file.write('->{}'.format(ind+1))
            file.write('\n')
inverted = {}
def ReadFile_inverted_index():
    with open('invertedIndex.txt') as f:
        for line in f:
            temp = line.split( )
            val = temp[1].split(",")
            inverted[temp[0]] = val



def rotate(str, n):
    return str[n:] + str[:n]

def writeFile_permuterm_index(dict_words):
    file = open("PermutermIndex.txt","w")
    keys = dict_words.keys()
    for key in sorted(keys):
        dkey = key + "$"
        for i in range(len(dkey),0,-1):
            out = rotate(dkey,i)
            file.write(out)
            file.write(" ")
            file.write(key)
            file.write("\n")
    file.close()

permuterm = {}
def ReadFile_perumterm_index():
    with open('PermutermIndex.txt','r') as permutefile:
        for line in permutefile:
            permuterm[line.split()[0]] = line.split()[1]
    return permuterm


def prefix_match(term, prefix):
    term_list = []
    for tk in term.keys():
        if tk.startswith(prefix):
            term_list.append(term[tk])
    return term_list

def query_process2(query):
    parts = query.split('*')
    if len(parts) == 3:
            case = 4
    elif parts[1] == '':
            case = 1
    elif parts[0] == '':
            case = 2
    elif parts[0] != '' and parts[1] != '':
            case = 3

    if case == 1:
            query = parts[0]
    elif case == 2:
            query = parts[1] + "$"
    elif case == 3:
            query = parts[1] + "$" + parts[0]

    term_list = prefix_match(permuterm,query)
    vec_term = []
    for term in term_list:
        vec_term.append(dict_words[term])
    res = vec_term[0]
    for vector in vec_term:
        res = op_or(res,vector)
    return res






def query_process1(query):
    list_operands = []
    list_operations = []
    for term in query.split(' '):
        if term[0] == '\\':
            list_operations.append(term)
        else:
            list_operands.append(term)
    vec_operands = []
    for operand in list_operands:
        vec_operands.append(query_process2(operand))

    count_not = 0
    for operation in list_operations:
        if operation =='\\not':
            vec_operands[count_not] = op_not(vec_operands[count_not])
            count_not +=1

    operation_count = 0

    res = vec_operands[0]
    for operation in list_operations:
        if operation == '\\and':
            operation_count+=1
            res = op_and(res,vec_operands[operation_count])
        elif operation =='\\or':
            operation_count+=1
            res = op_or(res,vec_operands[operation_count])


    return res

if __name__ =="__main__":
    list_docs = '1.txt 2.txt 3.txt 4.txt 5.txt 6.txt 7.txt 8.txt 9.txt 10.txt'.split()
    for id,docID in enumerate(list_docs):
        tk_words = tokenize(os.path.join('Documents',docID))
        # print(tk_words)
        wordvec(tk_words,id)


    # writeFile_inverted_index(dict_words)
    # writeFile_permuterm_index(dict_words)

    query = input('PART 1 NORMAL BOOLEAN RETRIEVAL (without Permuterm Index):-- Enter query:\n (all Capitals eg:\"\\NOT INFORMATION \\AND \\NOT RETRIEVAL\")\n')
    for ind,val in enumerate(query_process(query)):
        if val == 1:
            print('{}.txt'.format(ind+1))

    query = input('PART 2 WILD CARD QUERIES WITH BOOLEAN RETRIEVAL (wiht permuterm index):-- Enter query:\n (all Capitals eg:\"\\NOT INFO*TION \\AND \\NOT RET*EVAL\")\n')
    ReadFile_perumterm_index()
    query = query.lower()
    # print(query_process1(query))
    for ind,val in enumerate(query_process1(query)):
        if val == 1:
            print('{}.txt'.format(ind+1))
