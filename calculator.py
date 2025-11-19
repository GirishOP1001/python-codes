while True:
    print("\n****************************************Basic Calculator****************************************")
    print()
    numbs = []
    conf = input("Do you want use the calculator? (Y/N) : ").strip().upper()
    match conf:
        case 'Y':
            while True:
                str_numofnum = input("How many numbers do you want to use for calculation? : ")
                if(str_numofnum == "exit"):
                    print("\n****************************************Exited****************************************\n")
                    break
                numofnum = int(str_numofnum)
                if(numofnum <= 1):
                    print("Invalid input!!!")
                    print()
                    print()
                    print("\n****************************************Basic Calculator****************************************")
                    print()
                    print("Do you want use to the calculator? (Y/N) : Y")
                    continue
                for i in range(1 , numofnum+1):
                    if i == 1:
                        th = "st"
                    elif i == 2:
                        th = "nd"
                    elif i == 3:
                        th = "rd"
                    else:
                        th = "th"
                    inp = "Enter your " + str(i) + str(th) + " number : "
                    num = float(input(inp))
                    numbs.append(num)
                print("\nYour numbers are :",numbs)
                while True:
                    operator = str(input("Enter the operator (+,-,*) : "))
                    match operator:
                        case '+':
                            result = sum(numbs)
                            print("\nYour required answer is :",result)
                            cont = input("\nDo you want to perform further calculations? [Y/N] : ").strip().upper()
                            if(cont == 'Y'):
                                continue
                            elif(cont == 'N'):
                                print("\n****************************************Exited****************************************\n")
                                print()
                                print()
                                break
                            else:
                                print("Invalid input! Please only choose from [Y/N]!")
                                print()
                                continue
                        case '-':
                            result = numbs[0]
                            for j in numbs[1:]:
                                result -= j
                            print("\nYour required answer is :",result)
                            cont = input("\nDo you want to perform further calculations? [Y/N] : ").strip().upper()
                            if(cont == 'Y'):
                                continue
                            elif(cont == 'N'):
                                print("\n****************************************Exited****************************************\n")
                                print()
                                print()
                                break
                            else:
                                print("Invalid input! Please only choose from [Y/N]!")
                                print()
                                continue
                        case '*':
                            result = numbs[0]
                            for j in numbs[1:]:
                                result *= j
                            print("\nYour required answer is :",result)
                            cont = input("\nDo you want to perform further calculations? [Y/N] : ").strip().upper()
                            if(cont == 'Y'):
                                continue
                            elif(cont == 'N'):
                                print("\n****************************************Exited****************************************\n")
                                print()
                                print()
                                break
                            else:
                                print("Invalid input! Please only choose from [Y/N]!")
                                print()
                                continue
                        case 'exit':
                            print("\n****************************************Exited****************************************\n")
                            print("****************************************Basic Calculator****************************************\n")                                   
                            print("Do you want to use the calculator? (Y/N) : Y")
                            for k in range(1,numofnum+1):
                                if k == 1:
                                    th = "st"
                                elif k == 2:
                                    th = "nd"
                                elif k == 3:
                                    th = "rd"
                                else:
                                    th = "th"
                                inp = "Enter your " + str(k) + str(th) + " number : "+str(numbs[k-1])
                                print(inp)
                            break
                        case _:
                            print("Invalid operator! Please enter one of (+,-,*)\n")
                            continue
        case 'N':
            print("\n****************************************Thank You****************************************")
            print()
            print()
            break
        case _:
            print("Invalid input! Please try again!")
            print()
            continue