import operator
import math
class Stack:
     def __init__(self):
         self.items = []
     def empty(self):
         return self.items == []
     def push(self, item):
         self.items.append(item)
     def pop(self):
         return self.items.pop()
     def top(self):
         return self.items[len(self.items)-1]
     def size(self):
         return len(self.item)
class BinaryTreeNode:
  def __init__(self,valor):
    self.value = valor 
    self.left = None
    self.right = None
def isOperator(c):
	if (c == '+' or c == '-' or c == '*'
		or c == '/' or c == '^'): 
		return True
	else: 
		return False
def isOperatorExt(c):
	if (c == '+' or c == '-' or c == '*'
		or c == '/' or c == '^' or c==')' ): 
		return True
	else: 
		return False

def createExpressionTree(expresion):
  expresion=expresion.lower()
  ancestorPile = Stack()
  expresionTree = BinaryTreeNode(' ')
  ancestorPile.push(expresionTree)
  actualTree = expresionTree
  i=0
  while(i<len(expresion)):
    simbolo=expresion[i]
    if(simbolo=='('):
      actualTree.left= BinaryTreeNode('')
      ancestorPile.push(actualTree)
      actualTree=actualTree.left
      
    elif(not(isOperatorExt(simbolo))):
      a=i
      while ((i<len(expresion)-1)and(not(isOperatorExt(expresion[i+1])))):
        i+=1
      b=i+1
      actualTree.value = (expresion[a:b])
     
      actualTree=ancestorPile.pop()
    elif(isOperator(simbolo)):
      actualTree.value =simbolo
      
      actualTree.right=BinaryTreeNode('')
      ancestorPile.push(actualTree)
      actualTree=actualTree.right
    elif(simbolo==')'):
      actualTree=ancestorPile.pop()
      
    i+=1
  
  return expresionTree
def evaluateTree(expresionTree,valorX):
  operators = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv, '^':operator.pow}
  leftChild = expresionTree.left
  rightChild = expresionTree.right

  if (leftChild != None) and (rightChild != None) :
    fn = operators[expresionTree.value]
    return fn(evaluateTree(leftChild,valorX),evaluateTree(rightChild,valorX))
  else:
    #return int(expresionTree.value)
    if (expresionTree.value=='x'):
      return valorX
    elif (expresionTree.value=='pi'):
      return math.pi
    elif (expresionTree.value=='e'):
      return math.e
    else:
      return int(expresionTree.value)
expresion = "(x^2)"
arbol =createExpressionTree(expresion)
print (evaluateTree(arbol,2))
limiteInferior=5
limiteSuperior=10
step=0.5
i=limiteInferior
valX=[]
valY=[]
while (i<=limiteSuperior):
  valX.append(i)
  valY.append(evaluateTree(arbol,i))
  i+=step
print (valX)
print("\n")
print (valY)