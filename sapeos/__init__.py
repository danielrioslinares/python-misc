
from sympy import Symbol,solve,Eq,oo,limit
import itertools
import termcolor
import random



""" [ Circuit ] """

class Circuit:

	def __init__(self, components, nodes):
		self.components = components
		self.nodes = nodes

	def solve(self, vis=[], vo=None):
		# 0) Get dependances (component and node)
		cmp_dep = list(itertools.chain.from_iterable( [component._dependent for component in self.components] ))
		nde_dep = [node.v for node in self.nodes if node.v not in vis]
		dep = [d for d in cmp_dep+nde_dep if d not in vis+[vo]]
		# 1) Get equations for the current's rule in a twig and voltage dependances
		eqns = []
		# Kirchhoff 1st rule (Sum of currents towards node equals zero)
		for node in self.nodes:
			eqns.append( Eq( sum( [component.get_current_from_node(node) for component in self.components] ) ) )
		# Voltage dependances
		for node in self.nodes:
			for component in self.components:
				v = component.get_voltage_from_node(node)
				if v is not node.v:
					eqns.append( Eq( v, node.v ) )
		# Solve
		sol = mysolve( eqns, vo, dep, debug=False )
		# Limits
		sol2 = sol
		for component in self.components:
			for v,l in component._limits: sol2 = limit( sol2, v, l )
		# [vo] vs vis
		sol3 = {vo : sol2}
		return sol3
################################################################################


""" [ Components ] """

class AbstractComponent:

	# Constructor
	def __init__(self, id, *nodes):
		# Internal name for internal variables
		self.id = id
		# Limits to make after solving the circuit
		self._limits = []
		# Dependent variables
		self._dependent = []

	# Current contribution (current flowing towards the node from component)
	def get_current_from_node(self, node):
		return 0

	# Voltage contribution
	def get_voltage_from_node(self, node):
		return node.v
################################################################################


# n+
#  o     v(n+)
#  |             ↑ i(n+) = ( v(n-) - v(n+) ) / z
#  █ z
#  |             ↓ i(n-) = ( v(n+) - v(n-) ) / z
#  o     v(n-)
# n-
class Impedance(AbstractComponent):

	def __init__(self, id, node_plus, node_minus):
		super().__init__(id)
		# Impedance value
		self.z = Symbol( "z_" + str(self.id) )
		# Nodes
		self.node_plus = node_plus
		self.node_minus = node_minus

	def get_current_from_node(self, node):
		# Negative node
		if node is self.node_minus:
			return ( self.node_plus.v - self.node_minus.v ) / self.z
		# Positive node
		elif node is self.node_plus:
			return ( self.node_minus.v - self.node_plus.v ) / self.z
		# That node is not connected to the component so no current flows thru
		return 0
################################################################################


class Source(AbstractComponent):

	def __init__(self, id, node_plus, node_minus):
		super().__init__(id)
		# Voltage value
		self.V = Symbol( "V_" + str(self.id) )
		# Current value
		self.I = Symbol( "I_" + str(self.id) )
		# Nodes
		self.node_plus = node_plus
		self.node_minus = node_minus
		# Dependent variables
		self._dependent = [ self.I ]

	def get_current_from_node(self, node):
		# Negative node
		if node is self.node_minus:
			return -self.I
		# Positive node
		elif node is self.node_plus:
			return self.I
		# That node is not connected to the component so no current flows thru
		return 0

	# Voltage contribution
	def get_voltage_from_node(self, node):
		# Negative node
		if node is self.node_minus:
			return self.node_minus.v
		# Positive node
		elif node is self.node_plus:
			return self.node_minus.v + self.V
		# That node is not connected to the component
		return node.v
################################################################################


class IdealOpAmp(AbstractComponent):

	def __init__(self, id, node_plus, node_minus, node_output):
		super().__init__(id)
		# Output current value
		self.I = Symbol( "I(no)_" + str(self.id) )
		# Open loop gain
		self.A = Symbol( "A_" + str(self.id) )
		# Nodes
		self.node_plus = node_plus
		self.node_minus = node_minus
		self.node_output = node_output
		# Dependent variables
		self._dependent = [ self.I ]
		# Limits
		self._limits = [ (self.A, oo) ]

	def get_current_from_node(self, node):
		if isinstance(node.v,int):
			return -self.I
		# Negative node
		if node is self.node_minus:
			return 0
		# Positive node
		elif node is self.node_plus:
			return 0
		# Output node
		elif node is self.node_output:
			return self.I
		# That node is not connected to the component so no current flows thru
		return 0

	def get_voltage_from_node(self, node):
		# Negative node
		if node is self.node_minus:
			return self.node_minus.v
		# Positive node
		elif node is self.node_plus:
			return self.node_plus.v
		elif node is self.node_output:
			return self.A * (self.node_plus.v - self.node_minus.v)
		# That node is not connected to the component so no current flows thru
		return node.v
################################################################################












""" [ Node ] """

class Node:

	def __init__(self, id, v=None):
		self.id = id
		self.v = Symbol( "v_" + str(self.id) ) if v is None else v
################################################################################



























def mysolve(eqns, sol_var, vars_to_remove, debug=False):
	for i in range(100 * len(eqns)):

		# Get sol_var as function of the rest (UPDATE : find the most useful)
		# THIS METHOD IS SLOW
		for eqn in eqns:
			if sol_var in eqn.free_symbols:
				sol = solve( eqn, sol_var )[0]
				eqns.pop(eqns.index(eqn))
				if debug: print("[DEBUG] The variable",termcolor.colored(str(sol_var),"red"),"has been found in",eqn,"so",sol_var,"=",sol)
				break

		"""
		# Get sol_var as function of the rest
		sol_var_eqns = [eqn for eqn in eqns if sol_var in eqn.free_symbols]
		vars_to_remove__in__sol_var_eqns = [sum([False] + [symbol in vars_to_remove for symbol in eqn.free_symbols]) for eqn in sol_var_eqns]
		blessed_eqn = sol_var_eqns[ vars_to_remove__in__sol_var_eqns.index( min( vars_to_remove__in__sol_var_eqns ) ) ]
		sol = solve( blessed_eqn, sol_var )[0]
		eqns.pop(eqns.index(blessed_eqn))
		if debug: print("[DEBUG] The variable",termcolor.colored(str(sol_var),"red"),"has been found in",eqn,"so",sol_var,"=",sol)
		"""
		# Keep removing equations until we get the solution
		while len( [symbol for symbol in sol.free_symbols if symbol in vars_to_remove] ) != 0:
			# OLD len([symbol for symbol in list(itertools.chain.from_iterable( [eqn.free_symbols for eqn in eqns] ) ) if symbol in vars_to_remove]) != 0:
			# OLD len(eqns) != 0
			for var_to_remove in vars_to_remove:

				for eqn in eqns:

					if var_to_remove in eqn.free_symbols and var_to_remove in sol.free_symbols:
						temp_sol = solve( eqn, var_to_remove )[0]
						if debug: print("[DEBUG] The variable",termcolor.colored(str(var_to_remove),"red"),"in the equation",eqn,"returns",var_to_remove in eqn.free_symbols,"so",var_to_remove,"=",temp_sol)
						if debug: print("[DEBUG] I have removed the eqn =",eqn)
						eqns.pop(eqns.index(eqn))
						for eqn in eqns:
							old_eqn_str = str(eqn)
							eqns[eqns.index(eqn)] = eqn.subs( var_to_remove, temp_sol )
							if debug: print("[DEBUG] I have substituted",var_to_remove,"in",old_eqn_str,"by",temp_sol,"obtaining",eqn)
						old_sol_str = str(sol)
						sol = sol.subs( var_to_remove, temp_sol )
						if debug: print("[DEBUG] I have substituted",var_to_remove,"in",old_sol_str,"by",temp_sol,"obtaining",sol)
						break
				else:
					continue

				break
			if debug: print("[DEBUG] Solution so far",termcolor.colored(str(sol_var) + " = " + str(sol),"red") )

		if debug: print("[DEBUG] The solution is",sol_var,"=",sol)

		# TODO : sometimes if you take an input it will return vo = vo, this
		#        statement fix it?
		if sol_var in sol.free_symbols: random.shuffle(eqns)
		else: break
	else:
		raise Exception("Circuit is unsolvable for the given inputs :( sorry")

	return sol
















#
