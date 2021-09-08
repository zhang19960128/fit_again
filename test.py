import numpy as np
a=np.random.rand(10000,10000);
b=np.random.rand(10000,10000);
#c=np.matmul(a,b);
print(np.linalg.inv(a))
