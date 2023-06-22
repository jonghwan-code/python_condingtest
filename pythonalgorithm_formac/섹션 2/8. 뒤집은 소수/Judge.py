import time
import answer


case_num = 5


def judge():
    start = time.time()
    for i in range(1, case_num + 1):
        input_file = 'in' + str(i) + '.txt'
        output_file = 'out' + str(i) + '.txt'
        output = open(output_file, 'r').readline()

        result = answer.solution(input_file)

        if result != output + ' ':
            print('answer wrong!')
            print("output:", result)
            print("but we expected ", output)
    else:
        end = time.time()
        print("success!")
        print(f"{end - start: .5f} sec")


judge()
