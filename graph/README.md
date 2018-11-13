This directory includes

* `node.py`: which
  * defines a node class.
    * contains a name, list of children, and a count that's initially zero
    * implements a `show(graph)` method recursively prints the nodes within graph  
  * An `increment(graph)` method that increments the counts of all nodes within graph.
  * Implements a JSON Encode to create a JSON Representation of a tree.
  * Parses a dictionary to allow of the creation of a pass by reference json.


* 'jclient.py': which
  * Sends a tree with two nodes. It then calls the increment function on the server to add to the values.
  -Note that this implementation is pass by reference, so a [leaf1,leaf1,leaf2] would result in leaf1 having a value of 2.

* 'jserver.py': which
  * Recieves the encoded dictionary and tree and parses it. Stores the tree and awaits for the increment instruction coming from
  the client.
