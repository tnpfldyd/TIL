
def solution(numbers):
    answer = []
    
    # 중복된 수를 제거하기위해 set 타입을 선언합니다.
    set_ = set()

    # 서로 다른 인덱스 두개를 뽑아냅니다.
    # 이 때 두 번째 값은 첫 번째 값의 인덱스 보다 +1 한 인덱스를 뽑아냅니다.
    # 동일한 인덱싱을 피하고, 한 번 더했던 인덱스끼리 다시 더하는것을 방지하기 위해서입니다.
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            n1 = numbers[i]
            n2 = numbers[j]
            
            # 서로 다른 인덱스에서 뽑아낸 값을 합하고, set 변수에 추가합니다.
            sum_ = n1 + n2
            set_.add(sum_)
            
    # 정렬을 위해 순서가 없는 set 타입을 순서가 있는 list 타입으로 형변환합니다.
    list_ = list(set_)

    # 변환한 리스트를 정렬합니다.
    answer = sorted(list_) 
            
    return answer