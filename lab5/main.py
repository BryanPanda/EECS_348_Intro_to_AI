import math
import sys
import student_code as nbc

def check_imports(source_name):

    imports = []

    with open(source_name,"r") as f:
        tokens = f.read().replace("\n", " ").split()

    for i in range(len(tokens)-1):
        if tokens[i] == 'import':
            imports.append(tokens[i+1])

    with open('student_code.py',"r") as f:
        tokens = f.read().replace("\n", " ").split()

    for i in range(len(tokens)-1):
        if tokens[i] == 'import':
            imports.append(tokens[i+1])

    print('Imported Packages:')
    for i in range(len(imports)):
        print('  %s' % imports[i])
    print(' ')

def f_score(filename,predict):

    actual = []
      
    with open(filename,'rt') as f:
        lines = f.readlines()

    for line in lines:
        line = line.replace('\n','')
        fields = line.split('|')
        wID = int(fields[0])
        sentiment = fields[1]
        actual.append(sentiment)

    tp = 0
    fp = 0
    tn = 0
    fn = 0
    for i in range(len(actual)):
        if predict[i] == '5' and actual[i] == '5':
            tp = tp + 1
        if predict[i] == '5' and actual[i] == '1':
            fp = fp + 1
        if predict[i] == '1' and actual[i] == '1':
            tn = tn + 1
        if predict[i] == '1' and actual[i] == '5':
            fn = fn + 1

    precision = float(tp)/float(tp+fp)
    recall = float(tp)/float(tp+fn)
    f_score = float(2.0)*precision*recall/(precision+recall)

    return(f_score)
    
def main():

    source_name = sys.argv[0]
    check_imports(source_name)

    bayes = nbc.Bayes_Classifier()
    bayes.train('train.txt')
    predict = bayes.classify('classifyA.txt')
    fA = f_score('answersA.txt',predict)

    print('Classifier F-Scores:')
    print('  Reviews A: %.2f' % fA)
    exit(0)


if __name__ == "__main__":
    main()
    
    
