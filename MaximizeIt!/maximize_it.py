from itertools import product

def maximize_it(list_elements, M):
    combinations = product(*list_elements)
    sum_of_combinations = [sum(combination) for combination in combinations]
    maximum_s = [x % M for x in sum_of_combinations]
    return max(maximum_s)
    
    
if __name__ == "__main__":
    K, M = (int(x) for x in input().split())
    all_elements = [[int(x) ** 2 for x in input().split()[1:]] for _ in range(K)]
    print(maximize_it(all_elements, M))
   
