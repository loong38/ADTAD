import psutil


class ProcessManage(object):
    def __init__(self, port):
        self.port = port
        self.process = self.find_process_by_port()

    def find_process_by_port(self):
        for connect in psutil.net_connections():
            if connect.laddr.port == self.port:
                return psutil.Process(connect.pid)

    def is_process_use_port(self):
        if self.process:
            return True
        else:
            return False

    def stop_process_by_port(self, port):
        if self.is_process_use_port():
            self.process.terminate()
            return True

        return False

        #
        #     print(f"发现端口号 {port} 被进程 {self.process.name()} 占用，PID 为 {self.process.pid}")
        #     choice = input("是否要终止该进程？[y/n]: ").lower()
        #     if choice == 'y':
        #         print(f"正在停止进程 {self.process.name()} (PID: {self.process.pid})...")
        #         self.process.terminate()
        #         print(f"进程 {self.process.name()} (PID: {self.process.pid}) 已成功停止")
        #     else:
        #         print("已取消操作")
        # else:
        #     print(f"端口号 {port} 未被占用")

    # port = 8080  # 要查询的端口号
    # stop_process_by_port(port)