    import time
    import RPi.GPIO as GPIO
    from twython import TwythonStreamer
    
    # Busca este Hashtag
    TERMS = '#ParanaConf'
    
    # GPIO pin number of LED
    LED = 22
    
    # Aqui van los tokens ofrecidos por Twitter
    APP_KEY = ''
    APP_SECRET = ''
    OAUTH_TOKEN = ''
    OAUTH_TOKEN_SECRET = ''
    
    # Setup callbacks from Twython Streamer
    class BlinkyStreamer(TwythonStreamer):
            def on_success(self, data):
                    if 'text' in data:
                            print data['text'].encode('utf-8')
                            print
                            GPIO.output(LED, GPIO.HIGH)
                            time.sleep(0.5)
                            GPIO.output(LED, GPIO.LOW)
    
    # Setup GPIO as output
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED, GPIO.OUT)
    GPIO.output(LED, GPIO.LOW)
    
    # Create streamer
    try:
            stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
            stream.statuses.filter(track=TERMS)
    except KeyboardInterrupt:
            GPIO.cleanup()