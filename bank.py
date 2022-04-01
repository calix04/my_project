print('거 래 선 택\n 1.출금\n 2.계좌이체')
choose = input('선택:')

if choose == '1':
    banknumber = input('계좌번호를 입력해주십시오: ')
    money = input('얼마를 출금 하시겠습니까? : ' )
    password = input('비밀번호를 입력하십시오 :')
    if password == '1235' :
        print('{}원이 출금되었습니다.'.format(money))
    else:
        for password in range(5) :
            print('비밀번호를 다시 입력해주십시오.')
            password = input('비밀번호를 입력하십시오 :')
            if password == '1235' :
                print('{}원이 출금되었습니다.'.format(money))
                break
        else:
            print('비밀번호가 잠금처리 되었습니다 은행에 방문하여 주십시오. ')
        
elif choose == '2':
    banknumber = input('이체 계좌번호를 입력하여주십시오: ')
    money = input('얼마를 이체 하시겠습니까? :')
    password = input('비밀번호를 입력하십시오 :')
    if password == '1235' :
        print('{}원이 이체 되었습니다.'.format(money))
    else:
        for password in range(5) :
            print('비밀번호를 다시 입력해주십시오.')
            password = input('비밀번호를 입력하십시오 :')
            if password == '1235' :
                print('{}원이 이체 되었습니다.'.format(money))
                break
        else:
            print('비밀번호가 잠금처리 되었습니다. 은행에 방문하여 주십시오.')
