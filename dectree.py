from __future__ import print_function
training_data=[['green',3,'apple'],['yellow',3,'apple'],['red',1,'grape'],['red',1,'grape'],['yellow',3,'lemon']]
header=["color","diameter","label"]
def unique_vals(rows,col):
    return set([row[col] for row in rows])

unique_vals(training_data,0)
def class_counts(rows):
    counts={}
    for row in rows:
        label=row[-1]
        if label not in counts:
            counts[label]=0
        counts[label]+=1
    return counts  
class_counts(training_data)
def is_numeric(value):
    return isinstance(value,int)or isinstance(value,float)
is_numeric(7)
class Question:
    
    """A Question is used to partition a dataset.
    
    This class just records a 'column number' (e.g., 0 for Color) and a
    'column value' (e.g.,green). The 'match' method is used to compare 
    the feature value in an example to the feature value stored in the 
    question. See the demo below.
    """
    def __init__(self,column,value):
        self.column=column
        self.value=value
    def match(self,example):
        val=example[self.column]
        if is_numeric(val):
            return val>=self.value
        else:
            return val==self.value
    def __repr__(self):
        condition= "=="
        if is_numeric(self.value):
              condition= ">="
        return "Is %s %s %s?" % (header[self.column],condition, str(self.value))
        
Question(1,3)
q=Question(0,'green')
q
example=training_data[0]
def partition(rows,question):
    true_rows,false_rows=[],[]
    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows,false_rows 
true_rows,false_rows=partition(training_data,Question(0,'red'))
true_rows
false_rows
def gini(rows):
    counts=class_counts(rows)
    impurity=1 
    for lbl in counts:
        prob_of_lbl=counts[lbl]/float(len(rows))
        impurity -= prob_of_lbl**2
    return impurity     
no_mixing=[['apple','apple']]
gini(no_mixing)
some_mixing=[['apple','orange']]
gini(some_mixing)
lots_of_mixing=[['apple','orange','grape','grapefruit','blueberry']]
gini(lots_of_mixing)
def info_gain(left,right,current_uncertainty):
    p=float(len(left))/(len(left)+len(right))
    return current_uncertainty-p*gini(left)-(1-p)*gini(right)
current_uncertainty=gini(training_data)
current_uncertainty
true_rows,false_rows=partition(training_data,Question(0,'green'))
info_gain(true_rows,false_rows,current_uncertainty)
true_rows,false_rows=partition(training_data,Question(0,'red'))
true_rows
false_rows
true_rows,false_rows=partition(training_data,Question(0,'green'))
true_rows
false_rows
def find_best_split(rows):
    best_gain=0
    best_question=None
    current_uncertainty=gini(rows)
    n_features=len(rows[0])-1
    for col in range(n_features):
        values=set([row[col]for row in rows])
        for val in values:
            question=Question(col,val)
            true_rows,false_rows=partition(rows,question)
            if len(true_rows)==0 or len(false_rows)==0:
                continue
            gain=info_gain(true_rows,false_rows,current_uncertainty)
            if gain>=best_gain:
                best_gain,best_question=gain,question
    return best_gain,best_question
best_gain,best_question=find_best_split(training_data)
best_question
class Leaf:
    def __init__(self,rows):
        self.predictions=class_counts(rows)
class Decision_Node:
    def __init__(self,question,true_branch,false_branch):
        self.question=question
        self.true_branch=true_branch
        self.false_branch=false_branch
def build_tree(rows):
    gain,question=find_best_split(rows)
    if gain==0:
        return Leaf(rows)
    true_rows,false_rows=partition(rows,question)
    true_branch=build_tree(true_rows)
    false_branch=build_tree(false_rows)
    return Decision_Node(question,true_branch,false_branch)
def print_tree(node,spacing=""):
    if isinstance(node,Leaf):
        print(spacing + "Predict",node.predictions)
        return
    print(spacing + str(node.question))
    print(spacing + '--->True:')
    print_tree(node.false_branch,spacing + "  ")
    print(spacing + '--->False:')
    print_tree(node.false_branch,spacing + "  ")
my_tree=build_tree(training_data)
print_tree(my_tree)
def classify(row,node):
    if isinstance(node,Leaf):
        return node.predictions
    if node.question.match(row):
        return classify(row,node.true_branch)
    else:
        return classify(row,node.false_branch)
classify(training_data[0],my_tree)        







    
