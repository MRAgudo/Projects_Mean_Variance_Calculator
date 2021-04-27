import numpy as np

def calculate(list):
  #output mean, variance, std, max, min, sum of row & col., return as 3x3 dict
  
  if len(list) < 9: #condition to see if list contains 9 elements
    raise ValueError('List must contain nine numbers.') 
  else:
    list_array = np.reshape(list, (3,3)) # converts list into 3x3 numpy array
  
  #dictionary containing statistics as keys and values 0
  calculations = {
    'mean':0,
    'variance':0,
    'standard deviation':0,
    'max':0,
    'min':0,
    'sum':0
  }
  #empy arrays for each calculation of row and column
  mean_row= []
  mean_col = []
  std_row =[]
  std_col = []
  var_row =[]
  var_col = []
  maxum_row = []
  maxum_col = []
  minum_row= []
  minum_col = []
  sum_of_row = []
  sum_of_col = []
  
  for j in range(3): #for calculations of each row, appends to associated emtpy arra
      mean_row.append(np.mean(list_array[:,j]).tolist())
      var_row.append(np.var(list_array[:,j]).tolist())
      std_row.append(np.std(list_array[:,j]).tolist())
      maxum_row.append(np.max(list_array[:,j]).tolist())
      minum_row.append(np.min(list_array[:,j]).tolist())
      sum_of_row.append(np.sum(list_array[:,j]).tolist())
  
  for i in range(3): #for columns
      mean_col.append(np.mean(list_array[i,:]).tolist())
      var_col.append(np.var(list_array[i,:]).tolist())
      std_col.append(np.std(list_array[i,:]).tolist())
      maxum_col.append(np.max(list_array[i,:]).tolist())
      minum_col.append(np.min(list_array[i,:]).tolist())
      sum_of_col.append(np.sum(list_array[i,:]).tolist())
  
  #set new values to keys 
  calculations['mean'] = [mean_row,mean_col,np.mean(list_array)] 
  calculations['variance'] = [var_row,var_col,np.var(list_array)]
  calculations['standard deviation'] = [std_row,std_col,np.std(list_array)]
  calculations['max'] = [maxum_row,maxum_col,np.max(list_array)]
  calculations['min'] = [minum_row,minum_col,np.min(list_array)]
  calculations['sum'] = [sum_of_row,sum_of_col,np.sum(list_array)]
 
  return calculations