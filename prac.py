def start_timer():
   time_sec = 0
   for repetitions in range(1,9):
        print(repetitions)
        if repetitions == 1 or repetitions == 3 or repetitions == 5 or repetitions == 7 :
            time_sec = 25
        elif repetitions == 2 or repetitions == 4 or repetitions == 6 :
            time_sec = 5
        elif repetitions == 8:
            time_sec = 20
        print(time_sec)    
        repetitions+=1  
start_timer()        