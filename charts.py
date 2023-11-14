import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    rects = ax.bar(labels,values,width=0.8,color="CadetBlue",edgecolor="Crimson",linewidth=0.7)
    ax.set_title("Spotify songs")
    ax.bar_label(rects,padding=0.5)
    ax.grid(visible=True,which="major",axis="y",color="black", linestyle="dashed", linewidth=0.5)
    plt.show()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, wedgeprops={"linewidth": 2, "edgecolor": "black"}, autopct='%1.1f%%', textprops=dict(color="black"))
    ax.axis("equal")
    plt.show()