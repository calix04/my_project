print('회원가입/로그인\n 1.회원가입\n 2.로그인')
choose = input('선택:')

if choose == '1':    
    wrong ='success'
    id = input('아이디를 입력하여주십시오 :')
    id_ = id
    password = input('비밀번호를 입력하여주십시오 :')
    password_ = password
    passwordagain = input('비밀번호를 다시 입력하여주십시오 :')  
    passwordagain_ = passwordagain
    if passwordagain == passwordagain_ :
        print('비밀번호가 정상처리되었습니다.')
    else :
        print('비밀번호가 동일하지않습니다.')
        for st in range(3) :
            password = input('비밀번호를 다시 입력하십시오 :')
            if password == password_ :
                print('(비밀번호가 정상처리 되었습니다.')
                break
            else :
                print('비밀번호가 틀렸다.')
                    
                wrong ='fail'
                    
    
          
    if wrong == 'fail':

        print('잠시후에 다시 시도해주십시오.')

    else :
        
            phonenumber = input('전화번호를 입력하여주십시오 :')
            
            print('인증번호를 보냈습니다.')
            import random
            number_0 = (random.randint(0,9))
            number_1 = (random.randint(0,9))
            number_2 = (random.randint(0,9))
            number_3 = (random.randint(0,9))
            pass_number = ("{}{}{}{}".format(number_0, number_1, number_2,number_3))
            print('인증번호' , pass_number)
            number_pass = input('인증번호를 입력하세요 : ')
            if pass_number == number_pass:
                    print('확인되었습니다.')
                    home = input('주소를 입력하십시오 :')
                    print('회원가입이 성공적으로 완료되었습니다.')
                    print('당신의 아이디는' + id_ + '이고 당신의 비밀번호는' + password_ +'입니다.')
            else :
                for number_pass in range(10):
                    print('틀렸습니다.')
                    number_pass = input('번호를 다시 입력해주세요:' )
                    if pass_number == number_pass:
                        print('완료')
                        home = input('주소를 입력하십시오 :')
                        print('회원가입이 성공적으로 완료되었습니다.')
                        print('당신의 아이디는' + id_ + '이고 당신의 비밀번호는' + password_ +'입니다.')
                        break
                    else :
                        print ('틀렸습니다')
                        home = input('주소를 입력하십시오 :')
                        print('회원가입이 성공적으로 완료되었습니다.')
                        print('당신의 아이디는' + id_ + '이고 당신의 비밀번호는' + password_ +'입니다.')

elif choose == '2':

    id = input('아이디 :')
    id_ = id
    password = input('비밀번호 :')
    password_ = password
    

    if id == id_ :
        print ('아이디가 올바르게 입력되었습니다.')

    else:
        print('아이디가 올바르지 않습니다.')

    if password == password_ :
        print('비밀번호가 올바르게 입력되었습니다.')
    else :
        print('비밀번호가 올바르지 않습니다.')