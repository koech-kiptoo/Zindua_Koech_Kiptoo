import notify2 as notify2
# initialize the d-bus connection
notify2.init("Desktop Notifier")
# create Notification object
n = notify2.Notification(None, icon='')
# set urgency level
n.set_urgency(notify2.URGENCY_NORMAL)
# set timeout
# 1hr  20 mins
# 25 + 5
# 25 + 5
# 25 + 5
# 25 + 5
for i in range(1, 5):
    n.set_timeout(10000)
    n.update("Your Project", 'Project Stars Now For Next 25 minutes, Please start working...')
    n.show()
    import time
    time.sleep(secs=1500)

    n.set_timeout(10000)
    n.update("Break", 'You are on a Break for 5 minutes')
    time.sleep(secs=300)
    n.show()



