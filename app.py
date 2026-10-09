import circuits as Circuits
import time
import random

if __name__ == '__main__':
    print('Hi - this is an example of how a quantum cpu can be used to solve problems')
    print('This example is called grovers algorithm it is simple in practice but its the gateway to more complex problems')
    print('--------')
    print('to start provide a list of items')
    udict = input('item, item:')
    items = udict.split(",")
    cleanDict = []
    for item in items:
        item = item.strip()
        cleanDict.append(item)
    print('--------')
    print('from here mark which item you would like to find, use the items index (first item is i=1)')
    target = input('Target:')
    start = time.perf_counter()
    result = Circuits.grovers_algorithm(len(cleanDict), int(target))
    quantum_result = time.perf_counter() - start
    index_r = int(result, 2)
    print(index_r)
    print(f"The circuit choosed the {index_r} index, which is {cleanDict[index_r - 1]}")
    start = time.perf_counter()
    for i, item in enumerate(cleanDict):
        if i == (int(target) - 1):
            break
    classical_result = time.perf_counter() - start
    print(f"Classical search method time: {classical_result}")
    print(f'Quantum algorithm search time: {quantum_result}')
    run_long = input('Would you like to run a longer simulator (y,n)')
    if run_long.lower() == 'y':
        print(f'param size: 14')
        long_list = []
        for i in range(14):
            long_list.append(i)
        target = random.randint(1, 14)
        print(f"target is {target}")
        start = time.perf_counter()
        result = Circuits.grovers_algorithm(14, target)
        quantum_result = time.perf_counter() - start
        index_r = int(result, 2)
        print(f"The circuit choosed the {index_r} index, which is {long_list[index_r - 1]}")
        start = time.perf_counter()
        for i, item in enumerate(long_list):
            if i == target:
                break
        classic_time = time.perf_counter() - start
        print(f"Classical search method time: {classic_time}")
        print(f'Quantum algorithm search time: {quantum_result}')





    
    
