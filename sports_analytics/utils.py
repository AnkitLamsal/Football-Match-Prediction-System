import matplotlib.pyplot as plt
import base64, io, urllib

# def get_graph():
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     image_png = buffer.getvalue()
#     graph = base64.b64encode(image_png)
#     buffer.close()
#     return graph


# def get_plot(x,y):
#     plt.switch_backend("AGG")
#     plt.figure(figsize=(10,5))
#     plt.plot(x,y)
#     plt.xticks(rotation=45)
#     plt.tight_layout()
#     graph = get_graph()
#     return graph

def get_plot(x,y):
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