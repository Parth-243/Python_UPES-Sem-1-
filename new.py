import time
n= 100000000
def wrapper_fun():
  def wrapped():
    start_time= time.time()
    # end_time= time.time() # sec
    end_time= time.time()*100 # milli sec
    diff= end_time-start_time 

    # print(f"The execution time for n = {n} is\n {diff} sec")
    print(f"The execution time for n = {n} is\n {diff} milli sec")
        
def testfn(n):
  for i in range(0,n):
    res = i*10

start_time= time.time()
#excute function
testfn(n);

# end_time= time.time() # sec
end_time= time.time()*100 # milli sec
diff= end_time-start_time 

# print(f"The execution time for n = {n} is\n {diff} sec")
print(f"The execution time for n = {n} is\n {diff} milli sec")