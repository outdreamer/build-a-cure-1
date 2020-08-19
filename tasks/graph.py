import os

def save_graph(data, graph_type, graph_label, xlabel, ylabel, zlabel):
	if not os.path.exists('graphs'):
		os.mkdir('graphs')
	formatted_graph_label = ''.join([g for g in graph_label.lower() if g in 'abcdefghijklmnopqrstuvwxyz-_ ']).replace(' ', '_')
	image_path = ''.join(['graphs/', formatted_graph_label, '_', graph_type, '.png'])
	data['x'] = array(data['x']) if 'x' in data else []
	data['y'] = array(data['y']) if 'y' in data else [] #ndarray
	data['z'] = array(data['z']) if 'z' in data else [0 for x in xs]
	fig = plt.figure()
	plt.legend()
	plt.ylabel(ylabel)
	plt.xlabel(xlabel)
	axs = Axes3D(fig) if len(data['z']) > 0 else Axes2D
	if zlabel is not None:
		plt.zlabel(zlabel)
	cm = plt.get_cmap("RdYlGn")
	colors = [cm(float(i)/len(data['x'])) for i in range(len(data['x']))]
	if graph_type in ['regression', 'scatter', 'line']:
		if graph_type == 'regression':
			scatter_fig, scatter_axs = add_graph(data, fig, axs, graph_type, graph_label, xlabel, ylabel, zlabel)
			fig, axs = add_graph(data, scatter_fig, scatter_axs, graph_type, graph_label, xlabel, ylabel, zlabel)
		elif graph_type == 'line' or graph_type == 'scatter':
			fig, axs = add_graph(data, fig, axs, graph_type, graph_label, xlabel, ylabel, zlabel)
	elif graph_type == 'bar':
		plt.figure(figsize=(8, 6))
		plt.bar(range(22), data, alpha=0.5, align='center', label=graph_label) # data is pca.explained_variance_ 
	elif graph_type == 'network':
		graph = add_graph(data, fig, axs, graph_type, graph_label, xlabel, ylabel, zlabel)
	if graph or fig:
		''' to do: detect runtime env and show if in notebook or save if not '''
		#plt.show()
		plt.savefig(image_path)
	plt.close()
	return image_path

def add_graph(data, fig, axs, graph_type, graph_label, xlabel, ylabel, zlabel):
	''' to do: determine dimensions & range '''	
	''' add options like network graph, word stats, clusters and create an image that can be retrieved by api '''
	image_url = ''
	# api_url = ''.join(['https://', instance_ip, 'api_url'])

	if graph_type in ['scatter', 'line']:
		if graph_type == 'line':
		    points = np.array([data['x'], data['y']]).T.reshape(-1, 1, 2)
		    segments = np.concatenate([points[:-1], points[1:]], axis=1)
		    fig, axs = plt.subplots(2, 1, sharex=True, sharey=True)
		    norm = plt.Normalize(0, data['y'].max())
		    lc = LineCollection(segments, cmap='viridis') #, norm=norm)
		    lc.set_array(position)
		    lc.set_linewidth(2)
		    line = axs[0].add_collection(lc)
		    fig.colorbar(line, ax=axs[0])
		    axs[0].set_xlim(0, data['x'].max())
		    axs[0].set_ylim(0, data['y'].max())
		    fig.delaxes(axs[1])
		else:
		    #default = ax.scatter3D(data['x'], data['y'], data['z'], c=colors, cmap=cm)
		    if 'class' in data:
			    plt.scatter(data[:,0], data[:,5], c=data['class'])
		    elif 'z' in data:
		    	axs.plot3D(data['x'], data['y'], data['z'], 'gray')
		    else:
		    	axs.plot2D(data['x'], data['y'], 'gray')
		return fig, axs
	elif graph_type == 'network':
		G = nx.Graph() # graph_object = nx.read_gml(data)
		for i in data:
			G.add_node(i['source'], nodelabel=i['source_label'])
			G.add_node(i['target'], nodelabel=i['target_label'])
			G.add_edge(i['source'], i['target'])
		G[i['source']][i['target']]['color'] = 'blue'
		nx.write_gml(G, data)
		graph = nx.draw(G, with_labels=True)
		return graph
	return False