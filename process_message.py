def process_message(body, message):
    print('RECEIVED MESSAGE: {0!r}'.format(body))
    message.ack()
