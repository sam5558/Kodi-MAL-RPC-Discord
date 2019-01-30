from pypresence import Presence
import time
import json
import objectpath
import urllib.request

def test():
    rp = urllib.request.urlretrieve("http://127.0.0.1:8080/jsonrpc?request={%20%22jsonrpc%22:%20%222.0%22,%20%22method%22:%20%22Player.GetItem%22,%20%22params%22:%20{%20%22properties%22:%20[%20%22title%22,%20%22album%22,%20%22artist%22,%20%22season%22,%20%22episode%22,%20%22duration%22,%20%22showtitle%22,%20%22tvshowid%22,%20%22thumbnail%22,%20%22file%22,%20%22fanart%22,%20%22streamdetails%22%20],%20%22playerid%22:%201%20},%20%22id%22:%20%22VideoGetItem%22%20}", "kodi.json")
    #testfile=response.read()
    #tf=testfile.decode("utf8")
    #print(rp)
    #print(testfile)
    #print(tf)

    client_id = '539878242383241505' #change the cliend_id with your developper apps id.
    RPC = Presence(client_id)  # Initialize the client class
    RPC.connect() # Start the handshake loop
    #
    with open("kodi.json") as datafile:    data = json.load(datafile)
    data_tree = objectpath.Tree(data['result'])
    ep = tuple(data_tree.execute('$..episode'))
    season = tuple(data_tree.execute('$..season'))
    show = tuple(data_tree.execute('$..showtitle'))
    label = tuple(data_tree.execute('$..label'))
    #
    Epp = int(ep[0])
    Sea = int(season[0])
    Sho = ''.join(show)
    lab  = ''.join(label)
    print(RPC.update(state=Sho, details='S'+str(Sea)+'E'+str(Epp)+ '-' + str(lab)))
    #      time.sleep(60.0 - ((time.time() - starttime) % 60.0))

while True:
    test()
    time.sleep(60)
