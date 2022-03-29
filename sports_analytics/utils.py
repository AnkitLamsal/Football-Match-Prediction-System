import matplotlib
import matplotlib.pyplot as plt
import base64, io, urllib

def get_plot(x,y):
    matplotlib.use('Agg')
    plt.clf()
    plt.scatter(x,y)
    # plt.figure(figsize=(10,10))
    plt.xlabel("Goals by team1")
    plt.ylabel("Goals By team2")
    fig = plt.gcf()
    but = io.BytesIO()
    fig.savefig(but, format = 'png')
    but.seek(0)
    string = base64.b64encode(but.read())
    but.close()
    uri = urllib.parse.quote(string)
    return uri 