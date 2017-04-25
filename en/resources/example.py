from datetime import datetime

print('{:%Y-%m-%d-%H-%M-%S}'.format(datetime.now()))
print('{:%Y-%b-%d-%H-%M-%S}'.format(datetime.now()))
print('{:%H-%M-%S}'.format(datetime.now()))
