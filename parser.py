from grab import Grab, GrabTimeoutError

while True:
    try:
        g = Grab(log_file='out.html')
        g.go('http://etender.uzex.uz/lots/1/0')
        break
    except GrabTimeoutError:
        continue
