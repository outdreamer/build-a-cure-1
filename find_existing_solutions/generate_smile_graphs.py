import os, json
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

import plotly.offline
import plotly.express as px
import plotly.graph_objects as go

alphabet = 'abcdefghijklmnopqrstuvwxyz'
chars = '()[]1234567890@#$\/.:=-+'
mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=["r", "k", "c"]) 

def mkdir(dirname):
    cwd = os.getcwd()
    data_directory = '/'.join([cwd, dirname])
    if not os.path.exists(data_directory):
        os.mkdir(data_directory)
    return True

def get_item(s, index, item_type, item_order, counts):
    print('getting item', index, s[index], item_type, item_order)
    item_index = index + 1 if (item_order == 'next' and index + 1 < len(s)) else index - 1 if (item_order == 'prev' and index - 1 >= 0) else index if item_type == 'current' else None
    count = 0
    item = False
    if item_index:
        if item_order == 'current':
            item = s[index] if s[index] in alphabet else get_item(s, item_index, item_type, item_order, counts)
            print('3', item)
        else:
            item = s[item_index] if s[item_index] in alphabet else get_item(s, item_index, item_type, item_order, counts)
            print('1', item)
        if item:
            if not item.isnumeric and item.lower() in alphabet:
                next_item = s[index + 1] if len(s) > (index + 1) and s[index + 1].lower() == s[index + 1] and s[index + 1] in alphabet else ''
                element_name = ''.join([item, next_item])
                return get_electron_count(element_name, electron_counts)
            #else:
                # to do: handle numbers in smile formula
    return False

def get_electron_count(element_name, counts):
    print('looking for element', element_name)
    if element_name in counts:
        print('found count', counts[element_name])
        return counts[element_name]
    return 0

def graph_smile_formula_bond_pairs(s, xs, ys, order):
    mkdir('graphs')
    label = ''.join(['Smile Formula Graph: ', s])
    zeros = [0.0 for x in xs]
    complete_set = [xs[0]]
    complete_set.extend(ys)
    complete_order = [0.0]
    complete_order.extend(order)
    complete_zeros = [0.0]
    complete_zeros.extend(zeros)
    print('default', xs, ys, order)
    print('complete', complete_set, complete_order, complete_zeros)
    for graph_type in ['scatter', 'line']:
        fig = plt.figure()
        ax = Axes3D(fig)
        cm = plt.get_cmap("RdYlGn")
        colors = [cm(float(i)/len(zeros)) for i in range(len(zeros))]
        complete_colors = [cm(float(i)/len(complete_zeros)) for i in range(len(complete_zeros))]
        if graph_type == 'line':
            default = ax.plot3D(xs, ys, zeros, 'gray')
            change = ax.plot3D(complete_order, complete_set, complete_zeros, 'gray')
            all_changes = ax.plot3D(xs, ys, order, 'gray')
            #ax.set_color_cycle([cm(1.*i/(len(zeros)-1)) for i in range(len(zeros)-1)])
            #for i in range(len(zeros)-1):
            #    ax.plot(xs[i:i+2],ys[i:i+2])        
        elif graph_type == 'scatter':
            # compare just bond pairs
            default = ax.scatter3D(xs, ys, zeros, c=colors, cmap=cm)
            # change tells you how the number of electrons changes as the sequence order progresses
            change = ax.scatter3D(complete_order, complete_set, complete_zeros, c=complete_colors, cmap=cm) 
            # includes all dimensions
            all_changes = ax.scatter3D(xs, ys, order, c=colors, cmap=cm)
        ''' # plotly 
            default = go.Scatter3d(x=xs, y=ys, z=zeros) if graph_type == 'scatter' else px.line_3d(x=xs, y=ys, z=zeros)
            change = go.Scatter3d(x=complete_order, y=complete_set, z=zeros) if graph_type == 'scatter' else px.line_3d(x=complete_order, y=complete_set, z=zeros)
            all_changes = go.Scatter3d(x=xs, y=ys, z=order) if graph_type == 'scatter' else px.line_3d(x=xs, y=ys, z=order) 
        '''
        ''' this is how the first & second number of electrons in each pair relate 
            (may be useful as a predictor for elements an element bonds with)
            this leaves out information about distortions,
            but if you include the bond type with enough detail, that should clarify it
        '''
        # comment in one of the following sections if you want to show the graph rather than save it
        '''
        # plotly:
        fig = go.Figure()
        fig.add_trace(default)
        fig.add_trace(change) 
        fig.add_trace(all_changes)
        fig.update_layout(title = label)
        fig.show()

        # matplotlib:
        ax.plot3D(xs, ys, order, 'gray')
        ax.scatter3D(xs, ys, order, c=order, cmap='hsv')
        plt.show()
        '''
        ax.set_xlabel('1st electron count')
        ax.set_ylabel('2nd electron count')
        ax.set_zlabel('Order')
        title = 'Bond Pair Electron Counts, by Order'
        ax.set_title(label)
        # comment in the following section if youre using plotly & working offlinem to view graph in the browser
        '''plotly.offline.plot(
            {
                "data": traces,
                "layout": go.Layout(title=label)
            },
            image='jpeg',
            image_filename=image_path
        )'''

        # save graph
        image_path = ''.join(['graphs/', s, '_', graph_type, '.png'])

        ''' plotly 
        traces = [default, change, all_changes]
        py.image.save_as({'data':traces}, image_path, format='png')
        '''

        # matplotlib
        plt.savefig(image_path)

    return True

def convert_smile_to_bond_pairs(s, electron_counts):
    ''' to do:
    - encode rings as pairs of bonds - ensuring last item connects to original
    - encode bond strength 
    - encode bond type
    '''
    xs = []
    ys = []
    order = []
    new_sequence = [x for x in s if x.lower() in alphabet]
    element_sequence = []
    for i, x in enumerate(new_sequence):
        if x.lower() in alphabet:
            if x.upper() == x:
                if i < (len(new_sequence) - 1):
                    next = new_sequence[i + 1]
                    if next.lower() in alphabet:
                        el_name = ''.join([x, next]) if next.upper() != next else x
                        element_sequence.append(el_name)
                else:
                    element_sequence.append(x)
    pairs = zip(element_sequence, element_sequence[1:]) # creates a list of tuples
    bonded_pairs = []
    for i, pair in enumerate(pairs):
        bonded_pair = ''.join([pair[0], pair[1]])
        bonded_pairs.append(bonded_pair)
        x_count = get_electron_count(pair[0], electron_counts)
        y_count = get_electron_count(pair[1], electron_counts)
        xs.append(x_count)
        ys.append(y_count)
        order.append(i)
    print('bonded pairs', bonded_pairs)
    print('xs', xs, 'ys', ys, 'order', order)
    return xs, ys, order

def calculate_bond_strength(element1, element2):
    return False

s = 'O=C=O' #C(=O)=O is another way of saying CO2
electron_counts = {}
with open('electron_counts.json', 'r') as f:
    electron_counts = json.load(f)
    f.close()
print('electron_counts', electron_counts)

xs, ys, order = convert_smile_to_bond_pairs(s, electron_counts)
if len(xs) > 0 and len(ys) > 0 and len(order) > 0:
    graphed = graph_smile_formula_bond_pairs(s, xs, ys, order)
    if graphed:
        print('done graphing')