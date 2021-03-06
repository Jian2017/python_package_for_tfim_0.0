# how to use?
```{python}
# create a new Hamltonian
L=20 # system size
h=1 # transverse field
lambda1=1 # the nearest coupling
lambda2=0 # next nearest coupling
M=simplePureHamiltonian(L,h,lambda1,lambba2)

# create an object for that Hamltonian
t=tfim(M)

# calculate some physical quantities for that object
mat=t.correlator_equal_time_Matrix()

# plot your result
plt.matshow(mat)
plt.colorbar()
plt.show()

```

equal time spin-spin correlation matrix
<img src="/image/g1.png" alt="drawing" width="200px"/>

# how does it work?

the kernel part of this program is to calculate spin-spin correlation function.

applying Jordan-Wigner transformation, the problem becomes a many fermion correlation problem

then use Pfaffian, converting many fermion problem to two fermion problem:

<img src="/image/download.png" alt="drawing" width="200px"/>


# what can it solve?


It can calculate any N-spins space-time correlation function.

Since spin correlation function (Green function) are the building block of all physical quantities. There program can therefore calculate anything about this model: from the traditional dynamical structure factor, to the fancy  concepts such as entanglement entropy, out-of-time-ordered,.

### (example 1) Light cone in a quantum spin chain

<img src="/image/cnt.png" alt="drawing" width="400px"/>


### (example 2) Single spin dynamics


<img src="/image/sigmaT.png" alt="drawing" width="400px"/>



