import time
now = time.ctime()
qna = {
    "Hi":"Hlo",
    "How Are you":" I Am Good",
    "What is Your Name":"My Name is Karthik",
    "What is Your Age":" My Age is 23",
    "What is the Time Now":now,
    
    }
while True:
    qs = input()
    
    if(qs=="quit"):
        break
    else:
        print(qna[qs])