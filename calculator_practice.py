from math import*

print('계산 방법을 선택하십시오\n1.곱하기\n2.나누기\n3.더하기\n4.빼기\n5.제곱\n6.제곱근')
choice = input('선택:')
final = ''
if choice == '1':
    first = int(input('앞자리 수를 입력하세요 :'))
    second = int(input('뒤에 숫자를 입력하세요 :'))
    final = ''

    result = '{}x{}={}\n'.format(first , second, first * second)
    final = final + result

    print(final)
elif choice == '2':
    first = int(input('앞자리 수를 입력하세요 :'))
    second = int(input('뒤에 숫자를 입력하세요 :'))
    final = ''

    result = '{}/{}={}\n'.format(first , second, first / second)
    final = final + result

    print(final)

elif choice == '3':
    first = int(input('앞자리 수를 입력하세요 :'))
    second = int(input('뒤에 숫자를 입력하세요 :'))
    final = ''

    result = '{}+{}={}\n'.format(first , second, first + second)
    final = final + result

    print(final)

elif choice == '4':
    first = int(input('앞자리 수를 입력하세요 :'))
    second = int(input('뒤에 숫자를 입력하세요 :'))
    final = ''

    result = '{}-{}={}\n'.format(first , second, first - second)
    final = final + result

    print(final)

elif choice == '5':
    first = int(input('앞자리 수를 입력하세요 :'))
    second = int(input('뒤에 숫자를 입력하세요 :'))
    final = ''

    result = '{}^{}={}\n'.format(first , second, pow(first, second))
    final = final + result

    print(final)

elif choice == '6':
    first = int(input('수를 입력하세요 :'))
    final = sqrt(first)
    print(round(final, 3)) #소수점 3번째까지

else :
    print('다시 선택해주세요.')