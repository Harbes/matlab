#
#===========================================================
#
#Program to generate realized random numbers from the
#       1. Time invariant model
#       2. Count model
#       3. Linear regression model
#       4. Exponential regression model
#       5. Autoregressive model
#       6. Bilinear model
#       7. Autoregressive and heteroskedastic model
#       8. ARCH model
#
#   The realizations of the random draws from the models will be
#   different to those reported in the text as the random numbers
#   generated by the Gauss random number generator differ from those
#   generated by Matlab. Consequently the realizations are not printed
#   in this program and the PICTURE WILL BE DIFFERENT TO THE FIGURES
#   IN CHAPTER 1.
#
#
#==============================================================

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

np.random.seed(1234567)

t=5

### Time invariant model
mu  = 0;                            # Mean
sig = 2;                            # Standard deviation
#z   = stats.norm(0,1).rvs((t,))          # Standard normal random numbers
#y   = sig*z;                        # Generate realizations of y
s   = np.arange(-10,10.01,0.1)
fz  = stats.norm(0,1).pdf(s)                   # Probability distribution of z
fy  = stats.norm(0,1).pdf((s-mu)/sig)*(1/sig)  # Probability distribution of y
plt.plot(s,fz,label='norm(0,1)')
plt.plot(s,fy,label='norm(0,2)')
plt.title('Time invariant model')
plt.legend()
plt.show()

### count model
theta   = 2;
s       = np.arange(0,9.1,1)
fy2     = stats.poisson(theta).pmf(s)
plt.bar(s,fy2);
plt.title('Count Model');
plt.show()

# Linear regression model
beta = 3;
sig  = 2;
z    = randn(t,1);
x    = (0:1:t-1)
y    = beta*x + sig*z;
s    = (-10:0.1:20)';
fz   = normpdf(s);
tmp0 = repmat(s,1,length(beta*x'));
tmp1 = repmat(beta*x',length(s),1);
fy   = normpdf( (tmp0-tmp1)./sig )*(1/sig);