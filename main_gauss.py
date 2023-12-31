import numpy
import scipy
from scipy import optimize


#calculates legendre polynomials
def Legendre(n,x):
    P = x
    Plast = 1
    P_new = 0
    for i in range(2, n):
        P_new = ((2*i+1)/(i+1))*x*P - ((i)/(i+1))* Plast           #Recursion relation for Legandre Polynomials
        Plast = P
        P = P_new
    return P

#calculates nodes
def nodes(n):
    def Pn(x):
        return Legendre(n, x)
    error_tol = 1e-5
    x0 = numpy.linspace(-0.99,0.99,2*n)                          #Array of initial guesses
    sol = scipy.optimize.root(Pn, x0, tol=error_tol )                             #Finds roots of Pn
    unique = numpy.unique(sol.x, axis=0)                           #Gets rid of duplicate nodes
    ret = []
    for i in unique:
        if all(numpy.abs(i - existing_root) > error_tol for existing_root in ret):
            ret.append(i)
    return ret

#calculates weights
def weights(nodes, n):
    x = numpy.linspace(-1,1,100)
    n = n-1
    w = []
    for i in range(n):
        Lagrange = 1
        for j in range(n):                                      #Computes Lagrange Polynomials
            if(j != i):
                Lagrange = Lagrange * ((x-nodes[j])/(nodes[i]-nodes[j]))
        w.append(numpy.trapz(Lagrange,x))                   #Adds the integral of the Polynomal over [-1,1] to an array
    return w

#exports weights and nodes to a csv for use in excel
def export(xi,w):
    export = numpy.array([xi, w])
    numpy.savetxt("nodes_weights.csv", export, delimiter=",")

#extracts weights and nodes from the csv file
def extract():
    extract = numpy.loadtxt("nodes_weights.csv", delimiter=",", dtype=float)
    return extract

#applies the given weights and nodes to a function
def gauss(a,b ,nodesandweights):
    #for f(x) = e^x:
    gauss = 0
    for i in range(n - 1):
        gauss = gauss + nodesandweights[1][i] * numpy.exp(((b+a)/2) + nodesandweights[0][i]*((b-a)/2))   #Change function here

    gauss = gauss * ((b-a)/2)
    return gauss

a= -1
b = 1           #change the interval of integration (a,b) here
n= 5      #Change the degree of N here
xi = nodes(n)
w = weights(xi, n)
export(xi,w)

nodesandweights = extract()
gaussresult = gauss(a,b,nodesandweights)
print("I =",gaussresult)
