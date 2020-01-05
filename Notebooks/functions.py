import numpy as np
import matplotlib.pyplot as plt


def load_data(path, set_flag=False):
    """
    Load dataset.

    :param path: file path
    :type path: str
    :param set_flag: activation set flag
    :type set_flag: bool
    :return: data as numpy array
    """
    file = open(path, "r")
    data = []
    set_list = []
    for line in file:
        splitted_line = line.split(",")
        if not set_flag:
            data.append(list(map(float, splitted_line)))
        else:
            data.append(list(map(float, splitted_line[:-1])))
            s = splitted_line[-1].strip()
            set_list.append(int(s))
    result = np.array(data)
    if set_flag:
        set_list = np.array(set_list)
        set_list = set_list.reshape(set_list.shape[0], 1)
        result = np.concatenate((data, set_list), axis=1)
    return result


def plot_func(
        x,
        y,
        title,
        x_label,
        y_label,
        color='green',
        legend=[],
        multi=False):
    """
    Plot function.

    :param x: x-axis data
    :type x: list or numpy array
    :param y: y-axis data
    :type y: list or numpy array
    :param title: plot title
    :type title: str
    :param x_label: x-axis label
    :type x_label: str
    :param y_label: y-axis label
    :type y_label: str
    :param color: plot color
    :type color: str or list
    :param legend: plot legends
    :type legend: list
    :param multi: multi plot flag
    :type multi: bool
    :return: None
    """
    plt.figure()
    plt.grid()
    if multi:
        for index, y_item in enumerate(y):
            plt.plot(x[index], y_item, color=color[index])
    else:
        plt.plot(x, y, color=color)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    if len(legend) != 0:
        plt.legend(legend)
    plt.show()


def impedance_plot1(data, set_index):
    """
    Impedance plot function 1.

    :param data: input data
    :type data: numpy array
    :param set_index: activation set index
    :type set_index: int
    :return: None
    """
    filtered_data = data[data[:, 3] == set_index]
    data_03V = [filtered_data[filtered_data[:, 2] == 0.3][:, 0], filtered_data[filtered_data[:, 2] == 0.3][:, 1]]
    data_05V = [filtered_data[filtered_data[:, 2] == 0.5][:, 0], filtered_data[filtered_data[:, 2] == 0.5][:, 1]]
    data_07V = [filtered_data[filtered_data[:, 2] == 0.7][:, 0], filtered_data[filtered_data[:, 2] == 0.7][:, 1]]
    data_08V = [filtered_data[filtered_data[:, 2] == 0.8][:, 0], filtered_data[filtered_data[:, 2] == 0.8][:, 1]]

    x_plot_data = [data_03V[0], data_05V[0], data_07V[0], data_08V[0]]
    y_plot_data = [data_03V[1], data_05V[1], data_07V[1], data_08V[1]]

    legend = ["0.3V", "0.5V", "0.7V", "0.8V"]
    color = ["blue", "green", "red", "black"]
    x_label = "ZReal(Ohm)"
    y_label = "ZImage(Ohm)"
    title = "Set " + str(set_index)

    plot_func(
        x_plot_data,
        y_plot_data,
        title=title,
        x_label=x_label,
        y_label=y_label,
        color=color,
        legend=legend,
        multi=True)


def impedance_plot2(data, RH=None, P=None, V=None):
    """
    Impedance plot function 2.

    :param data: input data
    :type data: numpy array
    :param RH: Relative humidity
    :type RH: int (RH%)
    :param P: Pressure (psi)
    :type P: int
    :param V: Voltage (V)
    :type V: int
    :return: None
    """
    filtered_data = data
    if RH is None:
        filtered_data = filtered_data[filtered_data[:, 2] == V]
        filtered_data = filtered_data[filtered_data[:, 3] == P]
        data1 = [filtered_data[filtered_data[:, 4] == 30][:, 0], filtered_data[filtered_data[:, 4] == 30][:, 1]]
        data2 = [filtered_data[filtered_data[:, 4] == 50][:, 0], filtered_data[filtered_data[:, 4] == 50][:, 1]]
        data3 = [filtered_data[filtered_data[:, 4] == 100][:, 0], filtered_data[filtered_data[:, 4] == 100][:, 1]]
        legend = ["30%", "50%", "100%"]
        title = "V: {}V , P: {}psig".format(str(V), str(P))
    elif P is None:
        filtered_data = filtered_data[filtered_data[:, 2] == V]
        filtered_data = filtered_data[filtered_data[:, 4] == RH]
        data1 = [filtered_data[filtered_data[:, 3] == 5][:, 0], filtered_data[filtered_data[:, 3] == 5][:, 1]]
        data2 = [filtered_data[filtered_data[:, 3] == 15][:, 0], filtered_data[filtered_data[:, 3] == 15][:, 1]]
        data3 = [filtered_data[filtered_data[:, 3] == 25][:, 0], filtered_data[filtered_data[:, 3] == 25][:, 1]]
        legend = ["5psig", "15psig", "25psig"]
        title = "RH: {}% , V: {}V".format(str(RH), str(V))
    else:
        filtered_data = filtered_data[filtered_data[:, 3] == P]
        filtered_data = filtered_data[filtered_data[:, 4] == RH]
        data1 = [filtered_data[filtered_data[:, 2] == 0.3][:, 0], filtered_data[filtered_data[:, 2] == 0.3][:, 1]]
        data2 = [filtered_data[filtered_data[:, 2] == 0.5][:, 0], filtered_data[filtered_data[:, 2] == 0.5][:, 1]]
        data3 = [filtered_data[filtered_data[:, 2] == 0.7][:, 0], filtered_data[filtered_data[:, 2] == 0.7][:, 1]]
        legend = ["0.3V", "0.5V", "0.7V"]
        title = "RH: {}% , P: {}psig".format(str(RH), str(P))

    x_plot_data = [data1[0], data2[0], data3[0]]
    y_plot_data = [data1[1], data2[1], data3[1]]
    color = ["blue", "green", "red"]
    x_label = "ZReal(Ohm)"
    y_label = "ZImage(Ohm)"

    plot_func(
        x_plot_data,
        y_plot_data,
        title=title,
        x_label=x_label,
        y_label=y_label,
        color=color,
        legend=legend,
        multi=True)


def polarization_plot1(data, RH, P):
    """
    Polarization plot function 1.

    :param data: input data
    :type data: numpy array
    :param RH: Relative humidity
    :type RH: int (RH%)
    :param P: Pressure (psi)
    :type P: int
    :return: None
    """
    filtered_data = data[data[:, 4] == RH]
    filtered_data = filtered_data[filtered_data[:, 3] == P]
    data_I = filtered_data[:, 0]
    data_V = filtered_data[:, 1]
    data_P = filtered_data[:, 2]
    color1 = "red"
    color2 = "blue"
    x_label = "Current density (mA/cm2 )"
    y_label_1 = "Cell voltage (V)"
    y_label_2 = "Power density (mw/cm2)"
    title = "RH: {}% , P: {}psig".format(str(RH), str(P))

    plot_func(
        data_I,
        data_V,
        title=title,
        x_label=x_label,
        y_label=y_label_1,
        color=color1)
    plot_func(
        data_I,
        data_P,
        title=title,
        x_label=x_label,
        y_label=y_label_2,
        color=color2)


def polarization_plot2(data, set_index):
    """
    Polarization plot function 2.

    :param data: input data
    :type data: numpy array
    :param set_index: activation set index
    :type set_index: int
    :return: None
    """
    filtered_data = data[data[:, 3] == set_index]
    data_I = filtered_data[:, 0]
    data_V = filtered_data[:, 1]
    data_P = filtered_data[:, 2]
    color1 = "red"
    color2 = "blue"
    x_label = "Current density (mA/cm2 )"
    y_label_1 = "Cell voltage (V)"
    y_label_2 = "Power density (mw/cm2)"
    title = "Set " + str(set_index)
    plot_func(
        data_I,
        data_V,
        title=title,
        x_label=x_label,
        y_label=y_label_1,
        color=color1)
    plot_func(
        data_I,
        data_P,
        title=title,
        x_label=x_label,
        y_label=y_label_2,
        color=color2)
