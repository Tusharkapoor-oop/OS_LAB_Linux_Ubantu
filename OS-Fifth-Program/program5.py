from threading import Thread,current_thread
from multiprocessing import Process,Value,Pipe,current_process
process=[
    {"pid":"P1","arrival":0,"burst":7},
    {"pid":"P2","arrival":2,"burst":4},
    {"pid":"P3","arrival":4,"burst":1},
    {"pid":"P4","arrival":5,"burst":4},
]
intervals=[
    ("P1",0,2),("P2",2,4),("P1",4,6),
    ("P3",6,7),("P2",7,9),("P4",9,10),
    ("P1",11,13),("P4",13,15),("P2",15,16),("P1",17,19)
]
def calculate_metrics():
    print("\n   ------Scheduling Metrics------  -----")
    print("Process\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    tat_total=wt_total=rt_total=0
    for p in process:
        runs=[x for x in intervals if x[0]==p["pid"]]
        first_start=runs[0][1]
        completion=runs[-1][2]
        tat=completion-p["arrival"]
        wt=tat-p["burst"]
        rt=first_start-p["arrival"]
        tat_total+=tat
        wt_total+=wt
        rt_total+=rt
        print(p["pid"],"\t",p["arrival"],"\t",p["burst"],"\t",completion,"\t\t",tat,"\t\t",wt,"\t\t",rt)
    n=len(process)
    print("Average TAT=",round(tat_total/n,2))
    print("Average WT=",round(wt_total/n,2))
    print("Average RT=",round(rt_total/n,2))
def show_gantt_chart():
    print("\n -- round robin Gantt Chart -----")
    print(" || ".join(pid for pid,_,_ in intervals))
    times=[intervals[0][1]]+[end for _,_,end in intervals]
    print(" ".join(str(t) for t in times))
def thread_task(name):
    print(name,"is running in thread:",current_thread().name)
def thread_demo():
    print("\n---Thread Demo---")
    t1=Thread(target=thread_task,args=("Thread-1",))
    t2=Thread(target=thread_task,args=("Thread-2",))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Thread demo completed.")
def child_pipe(conn):
    conn.send("Hello from child process")
    conn.close()
def pipe_demo():
    print("\n---Pipe Demo---")
    parent_conn,child_conn=Pipe()
    child=Process(target=child_pipe,args=(child_conn,))
    child.start()
    msg=parent_conn.recv()
    print("Parent received:",msg)
    child.join()
def update_shared(value):
    value.value+=10
def shared_memory_demo():
    print("\n---Shared Memory Demo---")
    shared_value=Value('i',5)
    print("before update:",shared_value.value)
    child=Process(target=update_shared,args=(shared_value,))
    child.start()
    child.join()
    print("Updated value:",shared_value.value)
def process_task(name):
    print(name,"is running in process:",current_process().name)
def process_demo():
    print("\n---Process Demo---")
    p1=Process(target=process_task,args=("Process-1",))
    p2=Process(target=process_task,args=("Process-2",))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Process demo completed.")
if __name__=="__main__":
    calculate_metrics()
    show_gantt_chart()
    thread_demo()
    pipe_demo()
    shared_memory_demo()
    process_demo()
