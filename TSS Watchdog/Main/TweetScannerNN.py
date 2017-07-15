from theano import shared, function
from theano import tensor as T

state = shared(0)
inc = T.iscalar('inc')
accumulator = function([inc], state, updates=[(state, state+inc)])


print(accumulator(30))
print(accumulator(300))