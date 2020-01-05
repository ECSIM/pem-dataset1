import numpy as np
import matplotlib.pyplot as plt


def load_data(path,set_flag=False):
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
        set_list = set_list.reshape(set_list.shape[0],1)
        result = np.concatenate((data,set_list),axis=1)
    return result


def plot_func(x,y,title,x_label,y_label,color='green',legend=[],multi=False):
    plt.figure()
    plt.grid()
    if multi==True:
        for index,y_item in enumerate(y):
            plt.plot(x[index],y_item,color=color[index])
    else:
        plt.plot(x,y,color=color)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    if len(legend)!=0:
        plt.legend(legend)
    plt.show()

def impedance_plot1(data,set_index):
    act_data = data[data[:,3]==set_index]

    data_03V = [act_data[act_data[:,2]==0.3][:,0],act_data[act_data[:,2]==0.3][:,1]]
    data_05V = [act_data[act_data[:,2]==0.5][:,0],act_data[act_data[:,2]==0.5][:,1]]
    data_07V = [act_data[act_data[:,2]==0.7][:,0],act_data[act_data[:,2]==0.7][:,1]]
    data_08V = [act_data[act_data[:,2]==0.8][:,0],act_data[act_data[:,2]==0.8][:,1]]

    x_plot_data = [data_03V[0],data_05V[0],data_07V[0],data_08V[0]]
    y_plot_data = [data_03V[1],data_05V[1],data_07V[1],data_08V[1]]

    legend = ["0.3V","0.5V","0.7V","0.8V"]
    color = ["blue","green","red","black"]
    x_label = "ZReal(Ohm)"
    y_label = "ZImage(Ohm)"
    title = "act set"+str(set_index)

    plot_func(x_plot_data,y_plot_data,title=title,x_label=x_label,y_label=y_label,color=color,legend=legend,multi=True)

def impedance_plot2(data,RH,P):
    act_data = data[data[:,4]==RH]
    act_data = act_data[act_data[:,3]==P]
    data_03V = [act_data[act_data[:,2]==0.3][:,0],act_data[act_data[:,2]==0.3][:,1]]
    data_05V = [act_data[act_data[:,2]==0.5][:,0],act_data[act_data[:,2]==0.5][:,1]]
    data_07V = [act_data[act_data[:,2]==0.7][:,0],act_data[act_data[:,2]==0.7][:,1]]

    x_plot_data = [data_03V[0],data_05V[0],data_07V[0]]
    y_plot_data = [data_03V[1],data_05V[1],data_07V[1]]

    legend = ["0.3V","0.5V","0.7V"]
    color = ["blue","green","red"]
    x_label = "ZReal(Ohm)"
    y_label = "ZImage(Ohm)"
    title = "RH: {}% , P: {}psig".format(str(RH),str(P))

    plot_func(x_plot_data,y_plot_data,title=title,x_label=x_label,y_label=y_label,color=color,legend=legend,multi=True)

def polarization_plot1(data,RH,P):
    act_data = data[data[:,4]==RH]
    act_data = act_data[act_data[:,3]==P]
    data_I = act_data[:,0]
    data_V = act_data[:,1]
    data_P = act_data[:,2]
    color1 = "red"
    color2 = "blue"
    x_label = "Current density (mA/cm2 )"
    y_label_1 = "Cell voltage (V)"
    y_label_2 = "Power density (mw/cm2)"
    title = "RH: {}% , P: {}psig".format(str(RH),str(P))

    plot_func(data_I,data_V,title=title,x_label=x_label,y_label=y_label_1,color=color1)
    plot_func(data_I,data_P,title=title,x_label=x_label,y_label=y_label_2,color=color2)

def polarization_plot2(data,set_index):
    act_data = data[data[:,3]==set_index]
    data_I = act_data[:,0]
    data_V = act_data[:,1]
    data_P = act_data[:,2]
    color1 = "red"
    color2 = "blue"
    x_label = "Current density (mA/cm2 )"
    y_label_1 = "Cell voltage (V)"
    y_label_2 = "Power density (mw/cm2)"
    title = "act set"+str(set_index)
    plot_func(data_I,data_V,title=title,x_label=x_label,y_label=y_label_1,color=color1)
    plot_func(data_I,data_P,title=title,x_label=x_label,y_label=y_label_2,color=color2)

















