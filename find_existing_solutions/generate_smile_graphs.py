import os, json, sys
import numpy as np
from numpy import array
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm

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

def get_item(s, index, item_type, item_position, counts):
    if (item_position == 'next' and index + 1 < len(s)):
        item_index = index + 1
    elif (item_position == 'prev' and index - 1 >= 0):
        item_index = index - 1 
    elif item_type == 'current':
        item_index = index
    else:
        item_index = None
    count = 0
    item = False
    if item_index:
        if item_position == 'current':
            item = s[index] if s[index] in alphabet else get_item(s, item_index, item_type, item_position, counts)
        else:
            item = s[item_index] if s[item_index] in alphabet else get_item(s, item_index, item_type, item_position, counts)
        if item:
            if not item.isnumeric and item.lower() in alphabet:
                next_item = s[index + 1] if len(s) > (index + 1) and s[index + 1].lower() == s[index + 1] and s[index + 1] in alphabet else ''
                element_name = ''.join([item, next_item])
                return get_electron_count(element_name, electron_counts)
            #else:
                # to do: handle numbers in smile formula
    return False

def get_electron_count(element_name, counts):
    if element_name in counts:
        return counts[element_name]
    return 0

def graph_smile_formula_bond_pairs(s, xs, ys, position):
    cm = plt.get_cmap("RdYlGn")
    mkdir('graphs')
    label = ''.join(['Smile Formula Graph: ', s])
    zeros = [0.0 for x in xs]
    complete_set = [xs[0]]
    complete_set.extend(ys)
    complete_position = [0]
    complete_position.extend(position)
    complete_zeros = [0.0]
    complete_zeros.extend(zeros)
    for graph_type in ['scatter', 'line']: #line
        if graph_type == 'line':
            # convert to ndarray
            xs = array(xs)
            ys = array(ys)
            position = array(position)
            points = np.array([xs, ys]).T.reshape(-1, 1, 2)
            segments = np.concatenate([points[:-1], points[1:]], axis=1)
            #print('segments', segments.shape)
            fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
            norm = plt.Normalize(0, position.max())
            lc = LineCollection(segments, cmap='viridis', norm=norm)
            lc.set_array(position)
            lc.set_linewidth(2)
            line = axs[0].add_collection(lc)
            fig.colorbar(line, ax=axs[0])
            axs[0].set_xlim(0, xs.max())
            axs[0].set_ylim(0, ys.max())
            fig.delaxes(axs[1])
            #plt.show()
            image_path = ''.join(['graphs/', s, '_', graph_type, '.png'])
            plt.savefig(image_path)
            plt.close()       
        elif graph_type == 'scatter':
            colors = [cm(float(i)/len(zeros)) for i in range(len(zeros))]
            complete_colors = [cm(float(i)/len(complete_zeros)) for i in range(len(complete_zeros))]
            image_path = ''.join(['graphs/', s, '_', graph_type, '.png'])
            scatters = {
                'default': {
                    'xs': xs,
                    'ys': ys,
                    'zs': zeros,
                    'colors': colors,
                    'xlabel': '1st electron count',
                    'ylabel': '2nd electron count',
                    'zlabel': 'N/A',
                    'title': 'Bond Pair Electron Counts',
                    'path': ''.join(['graphs/', s, '_default_', graph_type, '.png'])
                },
                'position': {
                    'xs': complete_position,
                    'ys': complete_set,
                    'zs': complete_zeros,
                    'colors': complete_colors,
                    'xlabel': 'Position of element',
                    'ylabel': 'Electron count',
                    'zlabel': 'N/A',
                    'title': 'Electron counts by position in smile formula',
                    'path': ''.join(['graphs/', s, '_position_', graph_type, '.png'])
                },
                'all': {
                    'xs': xs,
                    'ys': ys,
                    'zs': position,
                    'colors': colors,
                    'xlabel': '',
                    'ylabel': '',
                    'zlabel': '',
                    'title': '',
                    'path': ''.join(['graphs/', s, '_all_', graph_type, '.png'])
                }
            }
            for scatter, value in scatters.items():
                make_plot(value, cm)
            plt.close()
        
        '''
        # comment in one of the following sections if you want to use plotly which has a nice browser UI
        default = go.Scatter3d(x=xs, y=ys, z=zeros) if graph_type == 'scatter' else px.line_3d(x=xs, y=ys, z=zeros)
        change = go.Scatter3d(x=complete_position, y=complete_set, z=zeros) if graph_type == 'scatter' else px.line_3d(x=complete_position, y=complete_set, z=zeros)
        all_changes = go.Scatter3d(x=xs, y=ys, z=position) if graph_type == 'scatter' else px.line_3d(x=xs, y=ys, z=position)
        fig = go.Figure()
        fig.add_trace(default)
        fig.add_trace(change) 
        fig.add_trace(all_changes)
        fig.update_layout(title = label)
        fig.show()
        # comment in the following section if youre using plotly & working offline to view graph in the browser
        plotly.offline.plot(
            {
                "data": traces,
                "layout": go.Layout(title=label)
            },
            image='jpeg',
            image_filename=image_path
        )
        traces = [default, change, all_changes]
        py.image.save_as({'data':traces}, image_path, format='png')
        '''

    return True

def make_plot(s, cm):
    fig = plt.figure()
    ax = Axes3D(fig)
    default = ax.scatter3D(s['xs'], s['ys'], s['zs'], c=s['colors'], cmap=cm)
    ax.plot3D(s['xs'], s['ys'], s['zs'], 'gray')
    plt.savefig(s['path'])
    return s['path']

def convert_smile_to_bond_pairs(s, electron_counts):
    ''' to do:
    - encode rings as pairs of bonds - ensuring last item connects to original
    - encode bond strength 
    - encode bond type
    '''
    xs = []
    ys = []
    position = []
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
        position.append(i)
    print('bonded pairs', bonded_pairs)
    print('xs', xs, 'ys', ys, 'position', position)
    ''' 
    graphing:

    - xs by ys compares tells you how the first & second electron count in each bond pair relate 
    (may be useful as a predictor for elements an element bonds with)
        this leaves out information about distortions,
        but if you include the bond type with enough detail, that should clarify it

    - comparing the full sequential position (complete_position) by the full electron count sequence (complete_set) 
        tells you how the number of electrons changes as the sequence position progresses

    - xs by ys by position tells you how the first & second electron count & position relate 
    '''
    return xs, ys, position

def calculate_bond_strength(element1, element2):
    return False

smile_formula = 'O=C=O=C=ONHO' #C(=O)=O is another way of saying CO2
if len(sys.argv) > 0:
    for arg in sys.argv:
        if '-' not in arg:
            ''' assume this is the chemical formula '''
            smile_formula = arg
print('formula', smile_formula)
electron_counts = {}
with open('electron_counts.json', 'r') as f:
    electron_counts = json.load(f)
    f.close()
if electron_counts:
    xs, ys, position = convert_smile_to_bond_pairs(smile_formula, electron_counts)
    if len(xs) > 0 and len(ys) > 0 and len(position) > 0:
        graphed = graph_smile_formula_bond_pairs(smile_formula, xs, ys, position)
        if graphed:
            print('graph complete')