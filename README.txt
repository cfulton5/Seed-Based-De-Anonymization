A full mapping of the node and edge pairs also required the use of the Stanford Network Analysis
Platform (SNAP). This requires the installation of "snap.py" from https://snap.stanford.edu/snappy/


The code snippet for this process is the following, where G1 and G2 are the edgelist files provided.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


file = open("G2.txt", "w+")
for NI in G2.Nodes():
    for Id in NI.GetOutEdges():
        file.write("%s %f\n" % (NI.GetId(), Id))
file.close()

file = open("G1.txt", "w+")
for NI in G2.Nodes():
    for Id in NI.GetOutEdges():
        file.write("%s %f\n" % (NI.GetId(), Id))
file.close()


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


In order to run the algorithm in this source code, the node and edge pairs must be in 
INCREMENTING from smallest node to largest node. This can be done with a simple sorting algorithm, 
or with a text editor that has this sort of function (Notepad++ has this ability).



The function of the algorithm is fairly straight forward:

Lines 4-15:
Create lists of the seeds that correspond to G1 and G2.
Create lists from G1 and G2 of nodes and of edges.

Lines 17-28:
Establish default values going into the algorithm.

Lines 29 - 40:
Proceed through each node in G1 and use list indexes to check whether its edges
appear in the mapped list, thus establishing a mapped edge.

Lines 41 - 50:
Establish default values going into the iteration of G2.

Lines 52 - 59:
Checking G2 edges if they are paired to the equivalent mapped edges from G1.

Lines 60 - 70:
Calculate and store scores and the maximum scoring nodes.

Lines 71 - 73:
Resetting values for next iteration through G2.

Lines 75 - 87:
Calculating and testing ECCE values. Storing above 3.3 into result and below 3.3
as a "wrongNode."

Lines 89 - 91:
Resetting values for next iteration through G1.

Lines 93 - 96:
Saving the results into a text file.



A few iterations must be done in order to increase accuracy. Performance of 99% accuracy found 
in the first 3 iterations.


