import numpy as np
from load_utils import load_dirty

arr,nan_idx,outlier_idx=load_dirty()
print(f"====np.nan ====")
print(f"np.nan == np.nan ? {np.nan==np.nan}")
print(f"np.nan != np.nan ? {np.nan!=np.nan}")

result=(arr==np.nan)
print(f" arr==np.nan:{result.sum()}")

result=np.isnan(arr)
print(f"총 개수:{len(arr)} / 결측: {result.sum()}")
print(f"결측치의 위치 :{np.where(result)[0]}")
print(f" 평균 : {np.mean(arr)} -> {np.nanmean(arr)}")

for name,f1,f2 in [
    ("mean",np.mean,np.nanmean),
    ("sum",np.sum, np.nansum),
    ( "std",np.std,np.nanstd),
     ("min",np.min,np.nanmin),
     ("max",np.max,np.nanmax)

]:
    r1=f1(arr)
    r2=f2(arr)
    print(f"{name} f1: {r1} f2: {r2}")

    