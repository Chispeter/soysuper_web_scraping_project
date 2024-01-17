# Espacio para testear
import os
  
  
# current working directory 
path = os.getcwd() 
print("Current Directory:", path) 
  
# parent directory 
parent = os.path.join(path, os.pardir) 
  
# prints parent directory 
print("\nParent Directory:", os.path.abspath(parent)) 