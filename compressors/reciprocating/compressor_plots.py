import numpy as np


def plt():
    '''
    Matplotlib imports usually take a long time to run.
    This is a trick to only import plt when it actually
    need to be used.
    The only difference is that now you need to call plt like a function
    like `plt().plot([1,2,3])` instead of `plt().plot([1,2,3])`
    '''
    import matplotlib.pyplot
    return matplotlib.pyplot


def plot(x, y, x_label, y_label, title, label="", _absolute=False):

    # plt().ion()

    fig = plt().figure(figsize=[8,6])
    ax_ = fig.add_subplot(1,1,1)

    if _absolute:
        y = np.abs(y)

    ax_.plot(x, y, color=[1,0,0], linewidth = 2, label = label)
    ax_.set_xlabel(x_label, fontsize = 11, fontweight = 'bold')
    ax_.set_ylabel(y_label, fontsize = 11, fontweight = 'bold')
    ax_.set_title(title, fontsize = 12, fontweight = 'bold')
    plt().grid()
    plt().show() 

def plot2(x, y, x_label, y_label, title, labels, colors, linestyles):

    plt().ion()

    fig = plt().figure(figsize=[8,6])
    ax_ = fig.add_subplot(1,1,1)

    for i, label in enumerate(labels): 
        ax_.plot(x[i], y[i], color=colors[i], linewidth=2, linestyle=linestyles[i], label=label)
    
    ax_.set_xlabel(x_label, fontsize = 11, fontweight = 'bold')
    ax_.set_ylabel(y_label, fontsize = 11, fontweight = 'bold')
    ax_.set_title(title, fontsize = 12, fontweight = 'bold')
    plt().legend()
    plt().grid()
    plt().show() 

def plot_2_yaxis(data_to_plot, title):

    plt().ion()
    fig = plt().figure(figsize=[8,6])
    ax_1 = fig.add_subplot(1,1,1)
    ax_2 = ax_1.twinx()
    
    if len(data_to_plot) == 2:
        for key, data in data_to_plot.items():

            if "axis" in data.keys():
                axis_ = data["axis"]
            if "x_data" in data.keys():
                x_data = data["x_data"]
            if"y_data" in data.keys():
                y_data = data["y_data"]
                if data["y_axis_absolute"]:
                    y_data = np.abs(y_data)
            if "x_label" in data.keys():
                x_label = data["x_label"]
            if "y_label" in data.keys():
                y_label = data["y_label"]
            if "legend_label" in data.keys():
                legend_label = data["legend_label"]
            if "color" in data.keys():
                color = data["color"]
            if "linewidth" in data.keys():
                linewidth = data["linewidth"]
            if "linestyle" in data.keys():
                linestyle = data["linestyle"]

            ax_1.set_xlabel(x_label, fontsize = 11, fontweight = 'bold')
            plots = []
            legends = []
            if axis_ == "left":
                plot_1, = ax_1.plot(x_data, y_data, color=color, linewidth=linewidth, linestyle=linestyle, label=legend_label)
                ax_1.set_ylabel(y_label, fontsize = 11, fontweight = 'bold')
                plots.append(plot_1)
                legends.append(legend_label)
            else:
                plot_2, = ax_2.plot(x_data, y_data, color=color, linewidth=linewidth, linestyle=linestyle, label=legend_label)
                ax_2.set_ylabel(y_label, fontsize = 11, fontweight = 'bold')
                plots.append(plot_2)
                legends.append(legend_label)

        ax_1.set_title(title, fontsize = 12, fontweight = 'bold')
        ax_1.grid()
        ax_2.grid()
        fig.legend(bbox_to_anchor=(1,1), bbox_transform=ax_1.transAxes)
        plt().show()
