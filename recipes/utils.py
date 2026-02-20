from io import BytesIO
import base64
import matplotlib.pyplot as plt


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png).decode("utf-8")
    buffer.close()
    return graph


def get_chart(chart_type, data, labels=None):
    plt.switch_backend("AGG")
    plt.figure(figsize=(6, 3))

    names = data["name"].tolist()
    times = data["cooking_time"].tolist()

    # ---------- BAR ----------
    if chart_type == "#1":
        plt.bar(names, times)
        plt.xticks(rotation=45, ha="right")
        plt.ylabel("Cooking time (minutes)")

    # ---------- PIE ----------
    elif chart_type == "#2":
        if labels is None:
            labels = names
        plt.pie(times, labels=labels)

    # ---------- LINE (FIXED) ----------
    elif chart_type == "#3":
        plt.plot(range(len(names)), times, marker="o")
        plt.xticks(range(len(names)), names, rotation=45)
        plt.ylabel("Cooking time (minutes)")

    else:
        plt.text(0.5, 0.5, "Unknown chart type", ha="center")

    plt.tight_layout()
    chart = get_graph()
    plt.close()
    return chart
