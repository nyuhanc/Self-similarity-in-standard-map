import numpy as np
from matplotlib import pyplot as plt
from random import randrange

plt.rc('font', size=11, family='serif')
plt.rc('text', usetex=0)
plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=14)
plt.rc('legend', fontsize=14)
plt.rc('figure', figsize=(10, 10))
plt.rc('lines', linewidth=0.1)
# plt.rc('lines', markersize=0.3)
plt.rc('lines', markersize=0.5)

K = 1.
initial_points_density = 20 # točk je kvadrat tega!
N_max = 1000000000000000 # max iteracija če se slučajno kje zaloopa
N = 150000 # št. točk na sliki

# scale_order = 1
# x0_lims = [0,2*np.pi]
# p0_lims = [0,2*np.pi]
# scale_order = 0.1
# x0_lims = [4.5-np.pi*scale_order,4.5+np.pi*scale_order]
# p0_lims = [1.8-np.pi*scale_order,1.8+np.pi*scale_order]
# scale_order = 0.01
# x0_lims = [4.49-np.pi*scale_order,4.49+np.pi*scale_order]
# p0_lims = [1.788-np.pi*scale_order,1.788+np.pi*scale_order]
# scale_order = 0.001
# x0_lims = [4.5035-np.pi*scale_order,4.5035+np.pi*scale_order]
# p0_lims = [1.8116-np.pi*scale_order,1.8116+np.pi*scale_order]
# scale_order = 0.0001
# x0_lims = [4.50357-np.pi*scale_order,4.50357+np.pi*scale_order]
# p0_lims = [1.81143-np.pi*scale_order,1.81143+np.pi*scale_order]
# scale_order = 0.00001
# x0_lims = [4.45568-np.pi*scale_order,4.45568+np.pi*scale_order]
# p0_lims = [3.6355-np.pi*scale_order,3.6355+np.pi*scale_order]
scale_order = 0.000001
x0_lims = [4.455702-np.pi*scale_order,4.455702+np.pi*scale_order]
p0_lims = [3.635504-np.pi*scale_order,3.635504+np.pi*scale_order]
# scale_order = 0.0000001
# x0_lims = [4.5033178-np.pi*scale_order,4.5033178+np.pi*scale_order]
# p0_lims = [1.81119    37-np.pi*scale_order,1.8111937+np.pi*scale_order]
# scale_order = 0.00000001
# x0_lims = [4.503317545-np.pi*scale_order/2,4.503317545+np.pi*scale_order/2]
# p0_lims = [1.81119372-np.pi*scale_order,1.81119372+np.pi*scale_order]

def stdmap(X):
    x, p = X[0], X[1]
    pn = np.mod(p + K*np.sin(x), 2*np.pi)
    xn = np.mod(x + pn, 2*np.pi)
    return [xn, pn]


def in_area(x_lims,y_lims,point):
    if x_lims[0] < point[0] and point[0] < x_lims[1]:
        if y_lims[0] < point[1] and point[1] < y_lims[1]:
            return True
    else: return False

x0 = np.linspace(x0_lims[0], x0_lims[1], initial_points_density)
p0 = np.linspace(p0_lims[0], p0_lims[1], initial_points_density)
in_trajs, next_xs = [], []
for ii in range(len(x0)):
    for jj in range(len(p0)):
        in_trajs.append([[x0[ii], p0[jj]]])
        next_xs.append([x0[ii], p0[jj]])

count = 1
for i in range(N_max):
    if count < N:
        for point in range(initial_points_density ** 2):
            next_xs[point] = stdmap(next_xs[point])
            if in_area(x0_lims,p0_lims,next_xs[point]):
                in_trajs[point].append(next_xs[point])
                count += 1
                print(str(count) + '/' + str(N))
    else: break

fig = plt.figure()
for in_traj in in_trajs:
    plt.plot(np.array(in_traj).T[0], np.array(in_traj).T[1],'.', color=list(np.random.choice(range(255), size=3)/255))


plt.xlim(x0_lims)
plt.ylim(p0_lims)
plt.title('k = {}, num. of  points = {}, scale order = {}'.format(K,N,scale_order))
plt.xlabel('Position (rad)')
plt.ylabel('Momentum')
np.save('stdmap_zoom' + str(scale_order) + str(x0_lims) + str(p0_lims) + 'N' + str(N_max) + 'd' + str(initial_points_density), np.asmatrix(in_trajs))
plt.savefig('stdmap_zoom' + str(scale_order) + str(x0_lims) + str(p0_lims) + 'N' + str(N_max) + 'd' + str(initial_points_density) + '.png')
plt.show()