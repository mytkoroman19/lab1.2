def find_kth_largest(nums, k):
    if not (1 <= k <= len(nums)):
        raise ValueError("k повинен бути в межах від 1 до довжини нашого масиву.")
    
    index_nums = list(enumerate(nums))

    index_nums.sort(key=lambda x: x[1], reverse=True)

    original_index, value = index_nums[k - 1]

    return value, original_index


if __name__ == "__main__":
    nums = [4, 10, 5, 12, 3, 17, 1]
    print(f"Масив: {nums}")


    k_value = 2
    
    value, position = find_kth_largest(nums, k_value)


    print(f"{k_value}-й найбільший елемент: {value}")
    print(f"Його позиція в оригінальному масиві: {position}")
    


