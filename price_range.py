# given an average stock price for a day and its variance
# calculate the porbability that tomorrow it will have a given trading range of [L, U]

import scipy.stats as stats
import math

# collect starting values
S0 = float(input('Input today\'s stock price in USD: $'))
var_usd = float(input('Input the variance in dollars squared: $'))
L = float(input('Input the lower bound of the projected range: $'))
U = float(input('Input the upper bound of the projected range: $'))
print('\nThanks\n')

# calculate std dev in dollars
sigma_usd = math.sqrt(var_usd)

# standardize lower and upper bounds
z_L = (L - S0) / sigma_usd
z_U = (U - S0) / sigma_usd

# calculate probability using CDF of the standard normal distribution
probability = stats.norm.cdf(z_U) - stats.norm.cdf(z_L)
print('The probability that tomorrow the stock will trade within the given range is:', probability)