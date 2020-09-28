import networkx as nx
import matplotlib.pyplot as plt

"""
The main idea of this file is construct a class which hold a DG ( Direct Graph)
For doing so we will use the library networkx, which will be the main motor of this chanllenge
"""


class Database:
	def __init__(self, nodes_to_add):
		'''
		Constructor. The first value in nodes_to_add if it is a tuple must follow the this procedure (NodeName,None)
		:param nodes_to_add: Could be just a node in case of initialize the graph or a tuple of nodes (Node,Parent)
		'''
		self.Digraph = nx.DiGraph()
		self.extract = {}
		self.extract_status = {}
		if type(nodes_to_add) is list:
			self.__add__(nodes_to_add)
		else:
			self.__add__([(nodes_to_add, None)])

	def __add__(self, nodes_to_add):
		'''
		Function which adds nodes to the graph and also sets the edges.
		To create the first node put in ParentNode None
		:param nodes_to_add: list of tuples in which there are two values ( Node, ParentNode)
		:return:
		'''
		for i in nodes_to_add:
			# in case the values are not correct
			if len(i) < 2: raise ValueError("The tuple list must contain (Node, ParentNode)")
			# identify the first node
			if i[1] is None:
				# It exist one parent so the process must stop here
				if self.Digraph.number_of_nodes() > 0: raise Exception("It exists a parent node already")
				self.Digraph.add_node(i[0])
			# it's a child
			else:
				self.Digraph.add_node(i[1])
				# Taking the parent we add the child if there was any
				self.Digraph.add_edge(i[1], i[0])

	def __del__(self):
		'''
		Function made to erase all the data within the object
		:return: None
		'''
		# erase the graph
		self.Digraph.clear()
		# erase the dicts
		self.extract = {}
		self.extract_status = {}

	def draw_graph(self):
		'''
		Function to check and draw the graph
		:return: Nothing
		'''
		# nx.nx_agraph.write_dot(self.Digraph, 'test.dot')
		# nx.draw_networkx(self.Digraph, pos=nx.drawing.nx_agraph.graphviz_layout(self.Digraph, prog="dot"))
		nx.draw_networkx(self.Digraph )
		plt.show()

	def add_nodes(self, nodes_to_add):
		'''
		Function to add new nodes to the graph and update the extract if it exist one
		:param nodes_to_add: list of a tuple of two (Node, ParentNode)
		:return: Nothing
		'''
		self.__add__(nodes_to_add)
		# updates only if a extract is present
		if len(self.extract) > 0: self.update_extract(nodes_to_add)

	def add_extract(self, ext):
		'''
		Function to add the extract and its status
		:param ext: dict with imgs as keys and list as a values of node names
		:return: Nothing
		'''
		if type(ext) is not dict: raise ValueError("The argument passed must be an dictionnary")
		# save it
		self.extract = ext
		for key,value in self.extract.items():
			pre_status = "invalid"
			for i in value:
				if i in list(self.Digraph.nodes):
					pre_status = "valid"
				else:
					# if any key is missing we set to invalid and skip to the next img
					pre_status = "invalid"
					break
			self.extract_status[key] = pre_status

	def update_extract(self, nodes_to_add):
		'''
		Function to update the extract status each time that nodes are added
		:param nodes_to_add: list of the nodes added to the graph
		:return: Nothing
		'''
		childs = [i[0] for i in nodes_to_add]
		parents = [i[1] for i in nodes_to_add]
		# call add extract to check if the new additions solve the problem of invalid labels
		self.add_extract(self.extract)
		for key, value in self.extract.items():
			pre_status = self.extract_status[key]
			# skip unnecesary values and save cycles
			if pre_status == "invalid": continue
			for i in value:
				# check childs using the childs updated
				for y in self.Digraph.successors(i):
					if y in childs:
						pre_status = "granularity_staged"
						break
				# check siblings for doing so we ask for the parent and the compare with the parents updated
				for y in self.Digraph.predecessors(i):
					if y in parents:
						pre_status = "coverage_staged"
						break
				if y in parents:
					break
			self.extract_status[key] = pre_status

	def get_extract_status(self):
		'''
		Function used to return the status
		:return: list if there is a status else a string
		'''
		return self.extract_status if len(self.extract_status) > 0 else "No extracted introduced"


if "__main__" == __name__:
	# First Trial
	nodes = [("core", None), ("A","core"), ("B","core")]
	db = Database(nodes)

	# error trial
	del db
	try:
		nodes_err = [("core", None), ("A", None), ("B", "core")]
		db = Database(nodes_err)
	except Exception: print("exception caught")

	# error trial v2
	try:
		nodes_err = [("core", None), ("A"), ("B", "core")]
		db = Database(nodes_err)
	except Exception: print("exception caught")

	# Foodvisor Tests

	# Test 1
	# Initial graph
	build = [("core", None), ("A", "core"), ("B", "core"), ("C", "core"), ("C1", "C")]
	# Extract
	extract = {"img001": ["A"], "img002": ["C1"]}
	# Graph edits
	edits = [("A1", "A"), ("A2", "A")]

	# Get status (this is only an example, test your code as you please as long as it works)
	status = {}
	if len(build) > 0:
		# Build graph
		db = Database(build[0][0])
		if len(build) > 1:
			db.add_nodes(build[1:])
		# Add extract
		db.add_extract(extract)
		# Graph edits
		db.add_nodes(edits)
		# Update status
		status = db.get_extract_status()
		db.draw_graph()
	print(status)


	# Test 2
	del db
	# Initial graph
	build = [("core", None), ("A", "core"), ("B", "core"), ("C", "core"), ("C1", "C")]
	# Extract
	extract = {"img001": ["A", "B"], "img002": ["A", "C1"], "img003": ["B", "E"]}
	# Graph edits
	edits = [("A1", "A"), ("A2", "A"), ("C2", "C")]

	# Get status (this is only an example, test your code as you please as long as it works)
	status = {}
	if len(build) > 0:
		# Build graph
		db = Database(build[0][0])
		if len(build) > 1:
			db.add_nodes(build[1:])
		# Add extract
		db.add_extract(extract)
		# Graph edits
		db.add_nodes(edits)
		# Update status
		status = db.get_extract_status()
	print(status)
