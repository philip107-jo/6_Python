"""
    불리언 인덱싱과 마스킹
"""
import numpy as np
from load_utils import load_matrix,load_column,load_one_stock
arr=np.array([10,25,30,15,40])
mask=arr > 20
print(f" arr: {arr}")
print(f" arr > 20: {mask}")
print(f"arr[mask]:{arr[mask]}")
#대괄호 안에 mask를 넣으면 True에 해당하는 위치 값들만 배열로 만들어줌
print(f"True 개수:{mask.sum()}")

matrix=load_matrix()
big=matrix > 500_000
print(f"matrix > 500_000 :: shape {big.shape},dtype : {big.dtype}")

print(f"{matrix[big].shape}")

result=np.diff(matrix,axis=1) / matrix[:,:-1]    
print(result)

cond1 = result > 0.03   #3%넘게오른경우

#거래량(volume)
volumes=load_column("volume")[:,1:]  #(120,750) -> (120,749) 첫날제외
cond2=volumes > 2_000_000  #거래량이 200만주 초과
both=cond1 & cond2
print(f"수익률 3%이상이고,거래량이 200만주 이상:{both.sum()}")
print(f"수익률이 3%가되지않는 건수:{(~cond1).sum()}")

sample=np.array([0.05,0.02,0.0,0.12,-0.15])
sample2=np.where(sample > 0,"up",np.where(sample<0,"down","keep"))
print(sample2)


