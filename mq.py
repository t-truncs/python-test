import time

import stomp


def connect_and_subscribe(conn):
    conn.start()
    conn.connect('admin', 'admin', wait=True)
    # conn.subscribe(destination='/queue/test', id=1, ack='auto')
    conn.subscribe(destination='/queue/siji_class', id=1,
                   ack='client-individual')


class MyListener(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn

    def on_error(self, headers, message):
        print('received an error %s' % message)

    def on_message(self, headers, message):
        print('received a message %s ' % (message))
        print('%s' % headers['message-id'])
        print(headers)
        if ('class-ID' in headers):
            classid = headers['class-ID']
            if (classid.startswith('class')):
                if (int(classid[5:]) % 2 == 1):
                    self.conn.ack(headers['message-id'], 1)

        # time.sleep(2)

    def on_disconnected(self):
        print('disconnected')
        connect_and_subscribe(self.conn)


conn = stomp.Connection([('127.0.0.1', 61613)])
conn.set_listener('', MyListener(conn))
connect_and_subscribe(conn)

# 发送消息到队列
i = 0
n = 50
while(i < n):
    conn.send(body='class %i' % i, destination='/queue/siji_class',
              headers={'class-ID': 'class%s' % i,'persistent':'true'})
    i += 1

i = 0
while(i < n):
    conn.send(body='student %i' % i, destination='/queue/siji_student')
    i += 1

# 发送消息到主题
# conn.send(body='456', destination='/topic/siji2')

# 从队列接受消息
# conn.subscribe(destination='/queue/siji_class', id=1,
#                ack='client-individual')

# 从主题接受消息
# conn.subscribe(destination='/topic/siji2', id=1, ack='auto')

time.sleep(10)
# conn.ack('ID:Laptop-looffy-3566-1510278246227-5:55:-1:1:50',1)
conn.disconnect()
