import timeit
import sys
sys.path.append("..")
print(timeit.timeit('''
import sys
sys.path.append("..")
import pandas as pd
from lib.lib import locale
import numpy as np
from lib.lib import math
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next

    def setData(self, val):
        self.data = val

    def setNext(self, val):
        self.next = val
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head is None
    def add(self, item):
        new_node = Node(item)
        new_node.setNext(self.head)
        self.head = new_node
    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.getNext()
        return count
    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() is item:
                found = True
            else:
                current = current.getNext()
        return found
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.getData() is item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found:
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        else:
            raise ValueError
            print('Value not found.')

    def insert(self, position, item):
        if position > self.size() - 1:
            raise IndexError
            print("Index out of bounds.")
        current = self.head
        previous = None
        pos = 0
        if position == 0:
            self.add(item)
        else:
            new_node = Node(item)
            while pos < position:
                pos += 1
                previous = current
                current = current.getNext()
            previous.setNext(new_node)
            new_node.setNext(current)

    def index(self, item):
        current = self.head
        pos = 0
        found = False
        while current is not None and not found:
            if current.getData() is item:
                found = True
            else:
                current = current.getNext()
                pos += 1
        if found:
            pass
        else:
            pos = None
        return pos

    def pop(self, position = None):
        if  position != None and position > self.size():
            print('Index out of bounds')
            raise IndexError
            
        current = self.head
        if position is None:
            ret = current.getData()
            self.head = current.getNext()
        else:
            pos = 0
            previous = None
            while pos < position:
                previous = current
                current = current.getNext()
                pos += 1
                ret = current.getData()
            previous.setNext(current.getNext())
        return ret

    def append(self, item):
        temp = Node(item)
        temp.next = None
        if self.tail == None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
    def printList(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()
def fillMatrixZero(matriz,n):
    
    for i in range(n): 
        fila = LinkedList();
        for j in range(n):
            fila.append(0);
        matriz.append(fila);
def printMatrix(matriz):
    current = matriz.head
    for i in range(matriz.size()):
        current_2 = current.getData().head
        for j in range(matriz.size()):
            print(current_2.getData(),end = " ")
            current_2 = current_2.getNext()
        print(" ")        
        current = current.getNext()
class Distance_correlation_list():
    def __init__(self):
        self.x = LinkedList()
        self.y = LinkedList()
        self.matrix_distances_x = LinkedList();
        self.matrix_distances_y = LinkedList();
        self.row_average_x = LinkedList();
        self.column_average_x = LinkedList();
        self.total_average_x = 0.;
        self.row_average_y = LinkedList();
        self.column_average_y = LinkedList();
        self.total_avergae_y = 0.;
        self.A = LinkedList();
        self.B = LinkedList();
        self.distance_covariance_x_y = 0.;
        self.distance_covariance_x_x = 0.;
        self.distance_covariance_y_y = 0.;
        self.distance_correlation = 0.;
    def fillDistanceMatrix(self,n):
        fillMatrixZero(self.matrix_distances_x,n);
        fillMatrixZero(self.matrix_distances_y,n);
        current_distances_x = self.matrix_distances_x.head;
        current_distances_y = self.matrix_distances_y.head;
        current_x = self.x.head;
        current_y = self.y.head;
        for i in range(n):
            current_2_distances_x = current_distances_x.getData().head;
            current_2_distances_y = current_distances_y.getData().head;
            current_2_x = self.x.head;
            current_2_y = self.y.head;
            for j in range(n):
                current_2_distances_x.setData(np.linalg.norm(current_x.getData()-current_2_x.getData()));
                current_2_distances_y.setData(np.linalg.norm(current_y.getData()-current_2_y.getData()));
                current_2_distances_x = current_2_distances_x.getNext();
                current_2_distances_y = current_2_distances_y.getNext();
                current_2_x = current_2_x.getNext()
                current_2_y = current_2_y.getNext()        
            current_distances_x = current_distances_x.getNext();
            current_distances_y = current_distances_y.getNext();
            current_x = current_x.getNext();
            current_y = current_y.getNext();
    def generateAditionalValues(self,n):
        current_distances_x = self.matrix_distances_x.head;
        current_distances_y = self.matrix_distances_y.head;
        for i in range(n):
            count_x = 0;
            count_y = 0;
            current_2_distances_x = current_distances_x.getData().head;
            current_2_distances_y = current_distances_y.getData().head;
            for j in range(n):
                count_x += current_2_distances_x.getData()
                count_y += current_2_distances_y.getData()
                current_2_distances_x = current_2_distances_x.getNext();
                current_2_distances_y = current_2_distances_y.getNext();
            self.row_average_x.append(count_x/n);
            self.column_average_x.append(count_x/n);
            self.row_average_y.append(count_y/n);
            self.column_average_y.append(count_y/n);
            current_distances_x = current_distances_x.getNext();
            current_distances_y = current_distances_y.getNext();
        current_row_x = self.row_average_x.head;
        current_row_y = self.row_average_y.head;
        for i in range(n):
            count_x = 0;
            count_y = 0;
            current_2_row_x = self.row_average_x.head;
            current_2_row_y = self.row_average_y.head;
            for j in range(n):
                count_x += current_2_row_x.getData();
                count_y += current_2_row_y.getData();
                current_2_row_x = current_2_row_x.getNext();
                current_2_row_y = current_2_row_y.getNext();
            self.total_average_x = count_x/n;
            self.total_average_y = count_y/n;
            current_row_x = current_row_x.getNext();
            current_row_y = current_row_y.getNext();
    def fillCenteredMatrix(self,n):
        fillMatrixZero(self.A,n);
        fillMatrixZero(self.B,n);
        current_A = self.A.head;
        current_B = self.B.head;
        current_distances_x = self.matrix_distances_x.head;
        current_distances_y = self.matrix_distances_y.head;
        current_row_x = self.row_average_x.head;
        current_row_y = self.row_average_y.head;
        current_column_x = self.column_average_x.head;
        current_column_y = self.column_average_y.head;
        for i in range(n):
            current_2_A = current_A.getData().head;
            current_2_B = current_B.getData().head;
            current_2_distances_x = current_distances_x.getData().head;
            current_2_distances_y = current_distances_y.getData().head;
            for j in range(n):
                current_2_A.setData(current_2_distances_x.getData() - current_row_x.getData() - current_column_x.getData() + self.total_average_x);
                current_2_B.setData(current_2_distances_y.getData() - current_row_y.getData() - current_column_y.getData() + self.total_average_y);
                current_2_A = current_2_A.getNext()
                current_2_B = current_2_B.getNext() 
                current_column_x = current_column_x.getNext();
                current_column_y = current_column_y.getNext();
                current_2_distances_x = current_2_distances_x.getNext();
                current_2_distances_y = current_2_distances_y.getNext();
            current_A = current_A.getNext();
            current_B = current_B.getNext();
            current_row_x = current_row_x.getNext();
            current_row_y = current_row_y.getNext();
            current_distances_x = current_distances_x.getNext();
            current_distances_y = current_distances_y.getNext();
            current_column_x = self.column_average_x.head;
            current_column_y = self.column_average_y.head; 
    def calculateDistanceCovariance(self,n):
        current_A = self.A.head;
        current_B = self.B.head;
        for i in range(n):
            current_2_A = current_A.getData().head;
            current_2_B = current_B.getData().head;
            for j in range(n):
                self.distance_covariance_x_y +=  (current_2_A.getData())*(current_2_B.getData());
                self.distance_covariance_x_x +=  (current_2_A.getData())**2;
                self.distance_covariance_y_y +=  (current_2_B.getData())**2;
                current_2_A = current_2_A.getNext()
                current_2_B = current_2_B.getNext() 
            current_A = current_A.getNext();
            current_B = current_B.getNext();
        self.distance_covariance_x_y = self.distance_covariance_x_y*(1/n**2);
        self.distance_covariance_x_x = self.distance_covariance_x_x*(1/n**2);
        self.distance_covariance_y_y = self.distance_covariance_y_y*(1/(n**2));
    def calculateDistanceCorrelation(self,n):
        self.fillDistanceMatrix(n);
        self.generateAditionalValues(n);
        self.fillCenteredMatrix(n);
        self.calculateDistanceCovariance(n);     
        if self.distance_covariance_x_x*self.distance_covariance_y_y != 0:
            self.distance_correlation = math.sqrt((self.distance_covariance_x_y)/(math.sqrt(self.distance_covariance_x_x*self.distance_covariance_y_y)));
        else:
            self.distance_correlation = 0;
        #print("The distance correlation is: "+str(self.distance_correlation));
df = pd.read_csv('100_datos_aleatorios.csv')
locale.setlocale(locale.LC_ALL, '')
muestra_archivo = Distance_correlation_list()
for i in range(len(df.index)):
    muestra_archivo.x.append(locale.atof(df.loc[i]["x"]))
    muestra_archivo.y.append(locale.atof(df.loc[i]["y"]))
muestra_archivo.calculateDistanceCorrelation(len(df.index))''',number=10))

"""class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next

    def setData(self, val):
        self.data = val

    def setNext(self, val):
        self.next = val
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head is None
    def add(self, item):
        new_node = Node(item)
        new_node.setNext(self.head)
        self.head = new_node
    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.getNext()
        return count
    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() is item:
                found = True
            else:
                current = current.getNext()
        return found
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.getData() is item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found:
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
        else:
            raise ValueError
            print('Value not found.')

    def insert(self, position, item):
        if position > self.size() - 1:
            raise IndexError
            print("Index out of bounds.")
        current = self.head
        previous = None
        pos = 0
        if position == 0:
            self.add(item)
        else:
            new_node = Node(item)
            while pos < position:
                pos += 1
                previous = current
                current = current.getNext()
            previous.setNext(new_node)
            new_node.setNext(current)

    def index(self, item):
        current = self.head
        pos = 0
        found = False
        while current is not None and not found:
            if current.getData() is item:
                found = True
            else:
                current = current.getNext()
                pos += 1
        if found:
            pass
        else:
            pos = None
        return pos

    def pop(self, position = None):
        if  position != None and position > self.size():
            print('Index out of bounds')
            raise IndexError
            
        current = self.head
        if position is None:
            ret = current.getData()
            self.head = current.getNext()
        else:
            pos = 0
            previous = None
            while pos < position:
                previous = current
                current = current.getNext()
                pos += 1
                ret = current.getData()
            previous.setNext(current.getNext())
        return ret

    def append(self, item):
        temp = Node(item)
        temp.next = None
        if self.tail == None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
    def printList(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()
def fillMatrixZero(matriz,n):
    
    for i in range(n): 
        fila = LinkedList();
        for j in range(n):
            fila.append(0);
        matriz.append(fila);
def printMatrix(matriz):
    current = matriz.head
    for i in range(matriz.size()):
        current_2 = current.getData().head
        for j in range(matriz.size()):
            print(current_2.getData(),end = " ")
            current_2 = current_2.getNext()
        print(" ")        
        current = current.getNext()
class Distance_correlation_list():
    def __init__(self):
        self.x = LinkedList()
        self.y = LinkedList()
        self.matrix_distances_x = LinkedList();
        self.matrix_distances_y = LinkedList();
        self.row_average_x = LinkedList();
        self.column_average_x = LinkedList();
        self.total_average_x = 0.;
        self.row_average_y = LinkedList();
        self.column_average_y = LinkedList();
        self.total_avergae_y = 0.;
        self.A = LinkedList();
        self.B = LinkedList();
        self.distance_covariance_x_y = 0.;
        self.distance_covariance_x_x = 0.;
        self.distance_covariance_y_y = 0.;
        self.distance_correlation = 0.;
    def fillDistanceMatrix(self,n):
        fillMatrixZero(self.matrix_distances_x,n);
        fillMatrixZero(self.matrix_distances_y,n);
        current_distances_x = self.matrix_distances_x.head;
        current_distances_y = self.matrix_distances_y.head;
        current_x = self.x.head;
        current_y = self.y.head;
        for i in range(n):
            current_2_distances_x = current_distances_x.getData().head;
            current_2_distances_y = current_distances_y.getData().head;
            current_2_x = self.x.head;
            current_2_y = self.y.head;
            for j in range(n):
                current_2_distances_x.setData(np.linalg.norm(current_x.getData()-current_2_x.getData()));
                current_2_distances_y.setData(np.linalg.norm(current_y.getData()-current_2_y.getData()));
                current_2_distances_x = current_2_distances_x.getNext();
                current_2_distances_y = current_2_distances_y.getNext();
                current_2_x = current_2_x.getNext()
                current_2_y = current_2_y.getNext()        
            current_distances_x = current_distances_x.getNext();
            current_distances_y = current_distances_y.getNext();
            current_x = current_x.getNext();
            current_y = current_y.getNext();
    def generateAditionalValues(self,n):
        current_distances_x = self.matrix_distances_x.head;
        current_distances_y = self.matrix_distances_y.head;
        for i in range(n):
            count_x = 0;
            count_y = 0;
            current_2_distances_x = current_distances_x.getData().head;
            current_2_distances_y = current_distances_y.getData().head;
            for j in range(n):
                count_x += current_2_distances_x.getData()
                count_y += current_2_distances_y.getData()
                current_2_distances_x = current_2_distances_x.getNext();
                current_2_distances_y = current_2_distances_y.getNext();
            self.row_average_x.append(count_x/n);
            self.column_average_x.append(count_x/n);
            self.row_average_y.append(count_y/n);
            self.column_average_y.append(count_y/n);
            current_distances_x = current_distances_x.getNext();
            current_distances_y = current_distances_y.getNext();
        current_row_x = self.row_average_x.head;
        current_row_y = self.row_average_y.head;
        for i in range(n):
            count_x = 0;
            count_y = 0;
            current_2_row_x = self.row_average_x.head;
            current_2_row_y = self.row_average_y.head;
            for j in range(n):
                count_x += current_2_row_x.getData();
                count_y += current_2_row_y.getData();
                current_2_row_x = current_2_row_x.getNext();
                current_2_row_y = current_2_row_y.getNext();
            self.total_average_x = count_x/n;
            self.total_average_y = count_y/n;
            current_row_x = current_row_x.getNext();
            current_row_y = current_row_y.getNext();
    def fillCenteredMatrix(self,n):
        fillMatrixZero(self.A,n);
        fillMatrixZero(self.B,n);
        current_A = self.A.head;
        current_B = self.B.head;
        current_distances_x = self.matrix_distances_x.head;
        current_distances_y = self.matrix_distances_y.head;
        current_row_x = self.row_average_x.head;
        current_row_y = self.row_average_y.head;
        current_column_x = self.column_average_x.head;
        current_column_y = self.column_average_y.head;
        for i in range(n):
            current_2_A = current_A.getData().head;
            current_2_B = current_B.getData().head;
            current_2_distances_x = current_distances_x.getData().head;
            current_2_distances_y = current_distances_y.getData().head;
            for j in range(n):
                current_2_A.setData(current_2_distances_x.getData() - current_row_x.getData() - current_column_x.getData() + self.total_average_x);
                current_2_B.setData(current_2_distances_y.getData() - current_row_y.getData() - current_column_y.getData() + self.total_average_y);
                current_2_A = current_2_A.getNext()
                current_2_B = current_2_B.getNext() 
                current_column_x = current_column_x.getNext();
                current_column_y = current_column_y.getNext();
                current_2_distances_x = current_2_distances_x.getNext();
                current_2_distances_y = current_2_distances_y.getNext();
            current_A = current_A.getNext();
            current_B = current_B.getNext();
            current_row_x = current_row_x.getNext();
            current_row_y = current_row_y.getNext();
            current_distances_x = current_distances_x.getNext();
            current_distances_y = current_distances_y.getNext();
            current_column_x = self.column_average_x.head;
            current_column_y = self.column_average_y.head; 
    def calculateDistanceCovariance(self,n):
        current_A = self.A.head;
        current_B = self.B.head;
        for i in range(n):
            current_2_A = current_A.getData().head;
            current_2_B = current_B.getData().head;
            for j in range(n):
                self.distance_covariance_x_y +=  (current_2_A.getData())*(current_2_B.getData());
                self.distance_covariance_x_x +=  (current_2_A.getData())**2;
                self.distance_covariance_y_y +=  (current_2_B.getData())**2;
                current_2_A = current_2_A.getNext()
                current_2_B = current_2_B.getNext() 
            current_A = current_A.getNext();
            current_B = current_B.getNext();
        self.distance_covariance_x_y = self.distance_covariance_x_y*(1/n**2);
        self.distance_covariance_x_x = self.distance_covariance_x_x*(1/n**2);
        self.distance_covariance_y_y = self.distance_covariance_y_y*(1/(n**2));
    def calculateDistanceCorrelation(self,n):
        self.fillDistanceMatrix(n);
        self.generateAditionalValues(n);
        self.fillCenteredMatrix(n);
        self.calculateDistanceCovariance(n);     
        if self.distance_covariance_x_x*self.distance_covariance_y_y != 0:
            self.distance_correlation = math.sqrt((self.distance_covariance_x_y)/(math.sqrt(self.distance_covariance_x_x*self.distance_covariance_y_y)));
        else:
            self.distance_correlation = 0;
        #print("The distance correlation is: "+str(self.distance_correlation));
        
df = pd.read_csv('100_datos_aleatorios.csv')
locale.setlocale(locale.LC_ALL, '')
muestra_archivo = Distance_correlation_list()
for i in range(len(df.index)):
    muestra_archivo.x.append(locale.atof(df.loc[i]["x"]))
    muestra_archivo.y.append(locale.atof(df.loc[i]["y"]))
#muestra_archivo.fillCenteredMatrix()
muestra_archivo.calculateDistanceCorrelation(len(df.index))
#muestra_archivo.fillDistanceMatrix(len(df.index))"""

