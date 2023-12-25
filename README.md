# GaussianQuadrature
Program in python that uses a Legendre-Gaussian quadrature to perform a numerical integration of a given function on any given interval.
To use: I noted where to change the function that was being integrated(line 59). To do this delete the third and last term of the summation and replace it with your desired function (f(u(t))) and use u((t)) = ((b+a)/2) + nodesandweights[0][i]*((b-a)/2). For example x^2 would simply be (((b+a)/2) + nodesandweights[0][i]*((b-a)/2))**2, or 2x would be 2*(((b+a)/2) + nodesandweights[0][i]*((b-a)/2)).
To change the interval (a,b) use lines 64 and 65 to set a and b to the desired parameters.
To change the order of the quadrature use line 66 to set n equal to the desired order.
After running the program, all of the weights and nodes will be saved to a .csv file labeled nodes_weights.csv. This way you can use them in excel as they will create a accurate integration for many functions.
