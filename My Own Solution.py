def main():
    def prime(num):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                return True

        return False
    number_of_test_cases = int(input())
    for i in range(number_of_test_cases):
        ranges = input().split()
        left = int(ranges[0])
        right = int(ranges[1])
        left1 = None
        right1 = None
        while left < right:
            if prime(left):
                left1 = left
                break
            left = left+1
        while right >= left:
            if prime(right):
                right1 = right
                break
            right = right-1

        if left1 and right1:
            print(abs(left1-right1))
        elif left1 or right1:
            print(0)
        else:
            print(-1)

main()
