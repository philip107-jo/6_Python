"""
    넘파이 배열 - 검색,정렬
    -where : 조건에 맞는 요소의 인덱스 반환 / 값 치환
    -argmax / argmin : 최댓값/최솟밗이 있는 인덱스를 반환
    -sort : 정렬
"""
import numpy as np

arr=np.array([10,5,22,15,8,20])
print(f"arr:{arr}")

#15보단 큰 값을 찾기
idx_info=np.where(arr > 15)
print(f"idx_info: {idx_info}")
print(arr[idx_info])

arr2=np.where(arr>10,99,0)
print(f"arr2: {arr2}")


arr=np.array([[10,20,5],[33,15,40]])
print(f"idx_info: {idx_info}")
print(f"argmax: {np.argmax(arr)}")
print(f"argmin: {np.argmin(arr)}")

print(arr.flatten())
print(f"열 기준 최댓값 인덱스:{np.argmax(arr,axis=0)}")
print(f"행 기준 최댓값 인덱스:{np.argmax(arr,axis=1)}")
arr=arr.flatten()
#np.sort(배열) : 원본배열을 변경하지않고,정렬된 새로운 배열을 반환
sorted_arr=np.sort(arr)
print(f"정렬된 배열:{sorted_arr}")

desc_arr=sorted_arr[::-1]
print(desc_arr)

print