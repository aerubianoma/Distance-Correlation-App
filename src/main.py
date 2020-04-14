import sys
sys.path.append("..")
import all_class as cl
if __name__ == "__main__":
    prueba = cl.dca.Distance_correlation();
    prueba.x = [1,2]
    prueba.y = [3,4]
    prueba.calculateDistanceCorrelation(2);
    
    