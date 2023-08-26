importtime
 
while True:
    # 获取当前时间
    current_time = time.strftime("%H:%M:%S", time.localtime())
    # 打印时钟
    print(current_time)
    # 每隔一秒更新时钟
    time.sleep(1)
