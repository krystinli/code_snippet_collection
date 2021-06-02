## matplotlib_template
```py
def plot_static(data, colname, color, target_low, target_high, img_name):
    """
    plot column
    save it under img
    """
    fig, ax = plt.subplots()
    fig.set_size_inches(18, 5) # img size

    ax.plot(colname,
        data = data,
        color = "black",
        linewidth = 1,
        marker = 'o',
        markeredgecolor = color,
        markersize = 5,)

    ax.set(xlabel = "Date",
           ylabel = "Hours",
           title = colname)

    # target line
    plt.axhline(y=target_low, color='r', linestyle='dashed')
    plt.axhline(y=target_high, color='g', linestyle='dashed')
    plt.legend()

    plt.savefig("img/" + img_name + ".png")
    print("Generated plot for", colname)
```
