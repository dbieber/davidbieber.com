import os

def send_message(message_text, phone_number):
    script = """
    tell application "Messages"
      send "{}" to buddy "{}" of service "E:dbieber@princeton.edu"
    end tell
    """.format(
        message_text,
        phone_number
    )
    os.system("echo '{}' | osascript".format(script))
