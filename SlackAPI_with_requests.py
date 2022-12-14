import requests
import sys
import getopt

#Send Slack Message Using Slack API

def send_slack_message(message):
    payload = '{"text":"%s"}' % message
    response = requests.post('https://hooks.slack.com/services/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',
    data=payload)
    print(response.text)

def main(argv):

    message = ' '

    try: opts, args = getopt.getopt(argv, "hm:", ["message="])

    except getopt.GetoptError:
        print('SlackMessage.py -m <message>')
        sys.exit(2)
    if len(opts) == 0: 
        message = "HELLO, WORLD!"
    for opt, arg in opts: 
        if opt == '-h':
            print('SlackMessage.py -m <message>')
            sys.exit()
        elif opt in ("-m", "--message"):
            message = arg 

    send_slack_message(message)


if __name__ == "__main__":
    main(sys.argv[1:])