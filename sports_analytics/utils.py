import matplotlib
import matplotlib.pyplot as plt
import base64, io, urllib

def get_plot(x,y,team1_name, team2_name):
    matplotlib.use('Agg')
    plt.clf()
    plt.plot(x,color='#9acd32')
    plt.plot(y,color='#40e0d0')
    plt.legend([f"{team1_name}",f"{team2_name}"])
    # plt.figure(figsize=(10,10))
    plt.xlabel("Itreation")
    plt.ylabel("Number of Goals")
    fig = plt.gcf()
    but = io.BytesIO()
    fig.savefig(but, format = 'png')
    but.seek(0)
    string = base64.b64encode(but.read())
    but.close()
    uri = urllib.parse.quote(string)
    return uri 