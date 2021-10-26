from time import strftime, time
  #to record time

def type(prompt):
    global intext
    text =prompt.split()
    error =0
    for i in range(len(intext)):
        if i in(0, len (intext)-1):
            if intext[i] == text[i]:
                continue
            else:
                error= error+1
        else:
            if intext[i] == text[i]:
                if(intext[i+1] == text[i+1]) & (intext[i-1] ==text[i-1]):
                    continue
                else:
                    error += 1
            else:
                error +=1
    return error
def speed(inprompt, stime, etime):
    global time
    global intext
    intext= inprompt.split()
    twords = len(intext)
    speed = twords/time
    return speed


def elapse(stime,etime):
    time= etime - stime
    return time

if __name__ == '__main__':
    prompt = "Python is an interpreted high-level general-purpose programming language. "
    #this is para u have to type to check your typing speed
    print("Type this paragraph:--",prompt )
    

    input("Please enter when you are ready to check your typing speed!!")

    stime = time()
    inprompt = input()
    etime = time()
    

    time = round(elapse(stime,etime),2)
    speed = speed(inprompt,stime,etime)
    error = type(prompt)

    print("TOTAL TIME ELAPSED =" ,time,"SECONDS")
    print("YOUR AVERAGE TYPING SPEED IS" ,speed,"w/m")
    print("YOU HAVE",error,"ERRORS")
    

 