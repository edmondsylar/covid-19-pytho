import http.client
from flask import jsonify

conn = http.client.HTTPSConnection("covid-19-coronavirus-statistics.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "18531cc5femshe002bc3470f9b5ap1e6e98jsn2e42b35c1e99"
    }


def get_start(loc):
    conn.request("GET", "/v1/stats?country={}".format(loc), headers=headers)
    res = conn.getresponse()
    data = res.read()
    try:
        test = res.read();
        dt = jsonify(test)
        print (dt)
    except Exception as err:
        print (err)
    # print (i)

    return (data.decode("utf-8"))


# res = conn.getresponse()
# data = res.read()

# print(data.decode("utf-8"))