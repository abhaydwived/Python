import time
wait_time=1
max_retries=10
attempts=0
while(max_retries>attempts):
    print("Attempt",attempts+1,"- Wait time",wait_time)
    time.sleep(wait_time)
    wait_time*=2
    attempts+=1