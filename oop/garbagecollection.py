'''
Python’s memory allocation and deallocation method is automatic. The user does not have to preallocate or deallocate memory similar
to using dynamic memory allocation in languages such as C or C++. Python uses two strategies for memory allocation:
    Reference counting
    Garbage collection
Reference counting works by counting the number of times an object is referenced by other objects in the system. When references to
an object are removed, the reference count for an object is decremented. When the reference count becomes zero, the object is deallocated.

Automatic Garbage Collection of Cycles:
Because reference cycles take computational work to discover, garbage collection must be a scheduled activity. Python schedules garbage
collection based upon a threshold of object allocations and object deallocations. When the number of allocations minus the number of
deallocations is greater than the threshold number, the garbage collector is run. One can inspect the threshold for new objects
(objects in Python known as generation 0 objects) by importing the gc module and asking for garbage collection thresholds:
'''

# loading gc
import gc

# get the current collection
# thresholds as a tuple
print("Garbage collection thresholds:",
                    gc.get_threshold())
'''
Here, the default threshold on the above system is 700. This means when the number of allocations vs. the number of deallocations
is greater than 700 the automatic garbage collector will run. Thus any portion of your code which frees up large blocks of memory
is a good candidate for running manual garbage collection.
'''
# Manual Garbage collection
i = 0

# create a cycle and on each iteration x as a dictionary
# assigned to 1
def create_cycle():
    x = { }
    x[i+1] = x
    print(x)

# lists are cleared whenever a full collection or
# collection of the highest generation (2) is run
collected = gc.collect() # or gc.collect(2)
print("Garbage collector: collected %d objects." % (collected))

print("Creating cycles...")
for i in range(10):
    create_cycle()

collected = gc.collect()

print("Garbage collector: collected %d objects." % (collected))
'''There are two ways for performing manual garbage collection: time-based and event-based garbage collection.'''
