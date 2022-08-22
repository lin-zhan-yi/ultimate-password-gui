def random_number():
    import random
    d=random.randint(1,100)
    return d

def ultimate_password():
    min_value=1
    max_value=100
    msg="Guess from{}~{}"
    starter=True
    s=random_number()
    while starter==True:
        q=int(input(msg.format(min_value,max_value)))
        if q>min_value and q <max_value:
            if q>s:
                print("Too large!")
                max_value=q
            elif q<s:
                print("Too small!")
                min_value=q
            elif q==s:
                print("correct!")
                starter=False
        else :
            print("請輸入區間內的數字")
ultimate_password()
