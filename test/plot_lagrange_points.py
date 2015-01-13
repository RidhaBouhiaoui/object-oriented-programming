from matplotlib import pyplot as plt
from fe_utils.finite_elements import lagrange_points
from fe_utils import ReferenceTriangle
from argparse import ArgumentParser

parser = ArgumentParser(description="""Plot the nodes on the reference triangle""")
parser.add_argument("degree", type=int, nargs=1)
args = parser.parse_args()

fig = plt.figure()
ax = fig.add_subplot(111)

p = lagrange_points(ReferenceTriangle, args.degree[0])

plt.plot(p[:, 0], p[:, 1], 'bo')

for i, x in enumerate(p):
    ax.annotate(str(i), xy=x, xytext=(10, 0), textcoords='offset points')

ax.axis([-.1, 1.1, -.1, 1.1])

plt.show()
