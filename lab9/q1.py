test_cases = int(input())
outputs = []
for i in range(test_cases):
    nums = str(input())
    try:
        num1 = int(nums[:nums.index(" ")+1])
        num2 = int(nums[nums.index(" ")+1:])
        quotient = num1/num2
        outputs.append(str(quotient))
    except ValueError:
        outputs.append("Invalid value")
    except ZeroDivisionError:
        outputs.append("Can't divide by zero")

print("\n[*] outputs: \n")
for output in outputs:
    print(output)