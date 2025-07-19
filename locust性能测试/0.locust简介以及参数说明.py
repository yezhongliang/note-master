"""
线程和协程的区别：
1、一个线程可以包含多个协成
2、线程和进程是同步机制，协成是异步机制
3、线程的切换由操作系统调度，协成是用户自己进行调度
4、协成更加轻量级、资源消耗更低

下载命令：pip install locust
官方文档：https://cloud.tencent.com/developer/article/1594240

locust核心概念：
User类：
    概念：表示要生成进行压力测试的用户
    用户：每个user实例相当于一个用户
task：
    用于处理用户的行为，比如：登录会员-> 获取会员信息-> 获取其他信息等等
    TastSet：定义用户将执行的一组任务的类，测试任务开始后，每个locust用户会从TastSet中随机挑选一个任务执行


locust的运行与监控
    图形化界面运行：
        1. 通过命令行启动Locust服务，然后访问 http://localhost:8089 （页面地址）
        2. 在页面设置执行压测的策略，并发的用户数，每秒启动的用户数，执行多长时间等
        3. 点击start，开启执行压测

    命令行界面：
        locust -f locustfile.py --headless -u 100 -r 10 -t 30s

        上面命令参数说明：
            -f  --locustfile： 指定locus文件，执行哪个文件
            –headless：无界面模式执行locust，类似selenium的无头模式
            -u  --user：并发的用户数
            -r  --spawn-rate：用户生成速率
            -t  --run-time：测试运行的时长
        其他参数：
            -H  --host：指定测试主机地址
            -L  --no-reset-stats：测试期间不重置统计数据
            –csv： 将结果保存为 CSV 文件
            --web-host：设置web页面的访问IP
            --log-file：将日志输出保存到指定文件
            --tags：为测试任务添加标签，用于筛选和组织测试结果。这对于管理多个测试任务非常有用
            --expect-slaves  --expect-workers：指定期望加入的从节点（工作节点）数量。这在分布式测试中非常重要，用于确保主节点能够正确管理所有工作节点。
            --loglevel：设置日志的级别。日志级别包括DEBUG、INFO、WARNING、ERROR和CRITICAL，默认为INFO。根据需要调整日志级别可以帮助更好地控制日志输出
        例子1：无头模式运行并保存CSV结果
            locust -f test_script.py --headless --users 100 --spawn-rate 10 --run-time 5m --csv=test_results

    locust中的性能指标：
        RPS（Requests per Second）：每秒请求数
        平均响应时间（Average Response Time）：每个请求的平均响应时间
        用户数（Number of Users）

        TPS、QPS、RPS的区别：
            TPS：每秒事务数。是指服务器在单位时间内（一秒）能够处理的事务数量。事务是一个或多个操作的集合，可以是一个接口、多个接口、一个业务或多个业务的组合。
                计算公式：总事务数/总时间
            QPS：每秒的查询数。是指服务器在单位时间内（通一秒）能够响应的查询次数。这里的查询通常指的是数据库中的SQL查询操作。
                计算公式： 并发数/平均响应时间
            RPS：每秒请求数

"""




