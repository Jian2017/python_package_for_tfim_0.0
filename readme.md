# create a new Hamltonian with 
'''
M=simplePureHamiltonian(L,h,lambda1,lambba2)
'''
# create an object for that Hamltonian
t=tfim(M)

# calculate some physical quantities for that object
mat=t.correlator_equal_time_Matrix()

# plot your result
plt.matshow(mat)
plt.colorbar()
plt.show()
