# convex-0.1
Welcome to Convex!

Quick note: Do not delete the temp directory

A. Usability:

(On python 2 only, default python in Debian based distros)

Given a point cloud in 3-d space, it will calculate the set of points to create the minimum volume while keeping the surface convex.
In the context of phase diagrams, it will generate, (given a list of points), all possible phases lying on the convex hull.

B. Requirements: (if you do not want to use is bundled package, "convex-0.1" present in $dir/Convex/dist/)

1. python 2 (default python in Debian based distros)
2. python 'numpy' library (pip install numpy)
3. python 'matplotlib' library (pip install matplotlib)
4. python 'plotly' library (pip install plotly)


C. How to use:

Method One: With Pre-made input file (Recommended!)
Input file format: (assume the file is ABC, see ./examples/*.in for illustration)

##################################################

5 #first line of input file, denoting number of input points/compositions

1 0 0 0.0    #parts of A = 1, B = 0, C = 0, E_f = 0 (enthalpy units), A

0 1 0 0.0    #parts of A = 0, B = 1, C = 0, E_f = 0 (enthalpy units), B

0 0 1 0.0    #parts of A = 0, B = 0, C = 1, E_f = 0 (enthalpy units), C

1 1 2 -0.75  #parts of A = 1, B = 1, C = 2, E_formation = -0.75 (enthalpy units), ABC2

2 1 1 -0.10  #parts of A = 2, B = 1, C = 1, E_formation = -0.10 (enthalpy units), A2BC, end of decompositions, last line of input file


#####################   file-end   ###############


Alternative: If you don't wish to provide an input file, the programme would interactively ask for each composition in succession.
Use this method if you're uncomfortable using the above method or the point cloud is sufficiently small.

Important: The programme would still ask for the element names, please enter them in the same order as input file, i.e. A, B and then C.

Steps to follow:

1. Download the code and put it in any directotry, say $dir.

2. Add $dir/Convex to your path in .bashrc or .zshrc file, also chmod convex-0.1 in the directory $dir/Convex/dist

3. Syntax: use one of the two below
                1. convex-0.1 ./inputfile.in      (if you've made an input file)
                2. convex-0.1                     (if you'd like to interactively create an input file)

(The above is assuming convex.py is in your path, if not it needs to be called as /path/to/convex/convex.py)

4. The output will be generated as a .out file containing the list of points lying on the hull.

(Tip: Large number of points? go to command mode in vim/vi (esc + :) and type 'se nowrap' for better visualization)

5. Another file in .html format is generated which can be opened with any internet enabled web-browser. A basic contour plot is generated where you'd be able to see points on hull as well as the colorbar indicating formation enthalpy values. Hovering over points will indicate the composition at that hull vertex.

Cutomizing the plot:

Click on 'export to plotly' and you can customize many aspects of the contour graph per your needs including things such as:
1. Captioning the points (can be done easily by hovering over the point to see the composition, having the '.out' file open helps)
2. Joining points to indicate 3-phase quilibria
3. Changing color scheme
4. Changing every font size, typeface; positions of: colorbar, title, subplot captions; remove axis tics and markers; ...etc.

In short, most of the things in your plot can be customized with plotly


Thanks for your attention! Enjoy!

D. Troubleshooting:

1. check if the number of points = the number mentioned in first line (sometimes you might forget to change it after adding/removing points)

2. check that each line only contains information on on point/composition.

Otherwise: Contact me at usingh1@ch.iitr.ac.in
