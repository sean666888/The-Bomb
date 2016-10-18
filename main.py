import os
import sys

# Add vendor directory to module search path
parent_dir = os.path.abspath(os.path.dirname(__file__))
vendor_dir = os.path.join(parent_dir, 'vendor')

sys.path.append(vendor_dir)

# Now you can import any library located in the "vendor" folder!
import requests
# Try running this locally.
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
        auth=("api", "YOUR_API_KEY"),
        data={"from": "The Bomb <thebomb@YOUR_DOMAIN_NAME>",
              "to": ["bar@example.com"],
              "subject": "BOOM!",
              "text": "BOOM!"})
import time
var = "False"
t = int(input("Time:"))
t2 = t
for i in range(t2):
  if var == "False":
    print("In {}".format(t))
    var = "True"
  else:
    print(t)
  t -= 1
  time.sleep(1)
send_simple_message()
print("BOOM!")
