import http.client

conn = http.client.HTTPSConnection("api.sendgrid.com")

payload = "{}"

headers = {
    'authorization': "Bearer <<YOUR_API_KEY",
    'on-behalf-of': "Imtiaz"
    }

conn.request("GET", "/v3/suppression/spam_reports?limit=12&end_time=1569542399&start_time=1569456000", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

#[
#  {
#    "created": 1443651141,
#    "email": "user1@example.com",
#    "ip": "10.63.202.100"
#  },
#  {
#    "created": 1443651154,
#    "email": "user2@example.com",
#    "ip": "10.63.202.100"
#  }
#]
