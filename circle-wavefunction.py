import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('fivethirtyeight')

from matplotlib import animation

'''
free particle on a circle of radius 1
'''

# ---------------------------------------------------------------------------

# constants
m_e 	= 9.11e-28							# electron mass
hbar	= 1.05e-27							# reduced Planck's constant

# points on circle
X 		= np.linspace(0, 2 * np.pi, 200) 	# position
x, y 	= np.sin(X), np.cos(X)

# ---------------------------------------------------------------------------

# figure setup
fig = plt.figure(figsize=(18,6))
plt.suptitle('Energy eigenfunctions of a free electron on a circle')

ax_re, ax_im 		= [None]*4, [None]*4
lines_re, lines_im 	= [None]*4, [None]*4
for n in range(4):
	ax_re[n] = fig.add_subplot(int(241 + n), projection='3d')
	ax_re[n].set_title('$n={}$'.format(n), pad=3)
	ax_re[n].set_xlim3d([-1.25, 1.25])
	ax_re[n].set_ylim3d([-1.25, 1.25])
	ax_re[n].set_zlim3d([-1.25, 1.25])
	ax_re[n].set_zlabel('$Re(\psi_{}(x,t))$'.format(n), labelpad=10)

	ax_im[n] = fig.add_subplot(int(245 + n), projection='3d')
	ax_im[n].set_xlim3d([-1.25, 1.25])
	ax_im[n].set_ylim3d([-1.25, 1.25])
	ax_im[n].set_zlim3d([-1.25, 1.25])
	ax_im[n].set_zlabel('$Im(\psi_{}(x,t))$'.format(n), labelpad=10)

	# initialize line objects
	lines_re[n], = ax_re[n].plot(x, y, np.cos(n * X))
	lines_im[n], = ax_im[n].plot(x, y, np.sin(n * X))

N = 10
print(N)
# function to pass into FuncAnimation
def update(num, lines_re, lines_im):
	print(num)
	prog = num/N	# progress
	for n in range(4):
		k 		= n 								# quantum number
		w 		= hbar * k ** 2/(2 * m_e)			
		t 		= prog * 2 * np.pi / (w + 0.001)	# time
		wf_re 	= np.cos(k * X - w * t)				# real part of wavefunction
		wf_im 	= np.sin(k * X - w * t)				# imaginary part of wavefunction
		lines_re[n].set_data([x,y])
		lines_re[n].set_3d_properties(wf_re)
		lines_im[n].set_data([x,y])
		lines_im[n].set_3d_properties(wf_im)

ani = animation.FuncAnimation(fig, update, N, fargs=[lines_re, lines_im], interval=30)
ani.save('circle-wavefunction.gif', writer='pillow')