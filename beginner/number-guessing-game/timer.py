from datetime import datetime
def timer():
    start_time = datetime.now()
    
    name = input ("what's your name? ")

    print (name)
    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"Elapsed time: {total_time}")
    print(total_time)
    print(start_time)
    print(end_time)

timer()