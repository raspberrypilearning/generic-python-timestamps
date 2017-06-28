from datetime import datetime

print('{0:%Y-%m-%d-%H-%M-%S}'.format(datetime.now()))
print('{0:%Y-%b-%d-%H-%M-%S}'.format(datetime.now()))
print('{0:%H-%M-%S}'.format(datetime.now()))
