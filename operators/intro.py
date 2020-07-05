'''
Floor division -> //
2/3=0.6666
2//3=0
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
BITWISE OPERATORS:
OPERATORS       DESCRIPTION        SYNTAX
    &           Bitwise AND         x&y
    |           Bitwise OR          x|y
    ~           Bitwise NOT         ~x
    ^           Bitwise XOR         x^y
    >>          Bitwise right       x>>
                shift
    <<          Bitwise left        x<<
                shift
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Special Operators:
1. Identity operators:
'is' and 'is not' are identity operators.  both are
used to check if two values are located on the
same part of the memory. Two variables that are equal
does not imply that they are identical.
2. Membership operators:
in and not in are the membership operators; used to
test whether a value or variable is in a sequence.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ternary Operators:
1. Simple method- [on_true] if [expression] else [on_false]
2. Using tuple- (on_false, on_true) [expression]
3. Using Dict- {True: a, Flase: b} [expression]
4. Using lambda- (lambda: on_true, lambda: on_false)[expression]()

Ternary operator can be written as nested if-else:
print ("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
OPERATOR OVERLOADING:
Operator Overloading means giving extended meaning beyond their
predefined operational meaning. For example operator + is used
to add two integers as well as join two strings and merge two
lists. It is achievable because ‘+’ operator is overloaded by
int class and str class. You might have noticed that the same
built-in operator or function shows different behavior for
objects of different classes, this is called Operator Overloading.
We can overload all existing operators but we can’t create a new
operator.
To perform operator overloading, Python provides some special
function or magic function that is automatically invoked when
it is associated with that particular operator. For example,
when we use + operator, the magic method __add__ is automatically
invoked in which the operation for + operator is defined.
Python magic methods or special functions for operator overloading:

1. Binary Operators:
Operator    Magic Method
+           __add__(self, other)
–           __sub__(self, other)
*           __mul__(self, other)
/           __truediv__(self, other)
//          __floordiv__(self, other)
%           __mod__(self, other)
**          __pow__(self, other)

2. Comparison Operators :
Operator    Magic Method
<           __lt__(self, other)
>           __gt__(self, other)
<=          __le__(self, other)
>=          __ge__(self, other)
==          __eq__(self, other)
!=          __ne__(self, other)

3. Assignment Operators :
Operator    Magic Method
-=          __isub__(self, other)
+=          __iadd__(self, other)
*=          __imul__(self, other)
/=          __idiv__(self, other)
//=         __ifloordiv__(self, other)
%=          __imod__(self, other)
**=         __ipow__(self, other)

4. Unary Operators :
Operator    Magic Method
–           __neg__(self, other)
+           __pos__(self, other)
~           __invert__(self, other)
------------------------------------------------------------------------------------------------------------------------------------------------------------------
Any All in Python:
Any and All are two built ins provided in python used for
successive And/Or.

Any:
Returns true if any of the items is True. It returns False
if empty or all are false. Any can be thought of as a sequence
of OR operations on the provided iterables.
All:
Returns true if all of the items are True (or if the
iterable is empty). All can be thought of as a sequence of
AND operations on the provided iterables.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Operator Functions:

1. add(a, b) :- This functions returns addition of the given arguments.
Operation – a + b.

2. sub(a, b) :- This functions returns difference of the given arguments.
Operation – a – b.

3. mul(a, b) :- This functions returns product of the given arguments.
Operation – a * b.

4. truediv(a,b) :- This functions returns division of the given arguments.
Operation – a / b.

5. floordiv(a,b) :- This functions also returns division of the given arguments. But the value is floored value i.e. returns greatest small integer.
Operation – a // b.

6. pow(a,b) :- This functions returns exponentiation of the given arguments.
Operation – a ** b.

7. mod(a,b) :- This functions returns modulus of the given arguments.
Operation – a % b.

8. lt(a, b) :- This function is used to check if a is less than b or not. Returns true if a is less than b, else returns false.
Operation – a < b.

9. le(a, b) :- This function is used to check if a is less than or equal to b or not. Returns true if a is less than or equal to b, else returns false.
Operation – a <= b.

10. eq(a, b) :- This function is used to check if a is equal to b or not. Returns true if a is equal to b, else returns false.
Operation – a == b.

11. gt(a,b) :- This function is used to check if a is greater than b or not. Returns true if a is greater than b, else returns false.
Operation – a > b.

12. ge(a,b) :- This function is used to check if a is greater than or equal to b or not. Returns true if a is greater than or equal to b, else returns false.
Operation – a >= b.

13. ne(a,b) :- This function is used to check if a is not equal to b or is equal. Returns true if a is not equal to b, else returns false.
Operation – a != b.

14. setitem(ob, pos, val) :- This function is used to assign the value at a particular position in the container.
Operation – ob[pos] = val

15. delitem(ob, pos) :- This function is used to delete the value at a particular position in the container.
Operation – del ob[pos]

16. getitem(ob, pos) :- This function is used to access the value at a particular position in the container.
Operation – ob[pos]

17. setitem(ob, slice(a,b), vals) :- This function is used to set the values in a particular range in the container.
Operation – obj[a:b] = vals

18. delitem(ob, slice(a,b)) :- This function is used to delete the values from a particular range in the container.
Operation – del obj[a:b]

19. getitem(ob, slice(a,b)) :- This function is used to access the values in a particular range in the container.
Operation – obj[a:b]

20. concat(ob1,obj2) :- This function is used to concatenate two containers.
Operation – obj1 + obj2

21. contains(ob1,obj2) :- This function is used to check if obj2 in present in obj1.
Operation – obj2 in obj1

22. and_(a,b) :- This function is used to compute bitwise and of the mentioned arguments.
Operation – a & b

23. or_(a,b) :- This function is used to compute bitwise or of the mentioned arguments.
Operation – a | b

24. xor(a,b) :- This function is used to compute bitwise xor of the mentioned arguments.
Operation – a ^ b

25. invert(a) :- This function is used to compute bitwise inversion of the mentioned argument.
Operation – ~ a
------------------------------------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Inplace vs Standard Operators in Python

Normal operator’s “add()” method, implements “a+b” and stores
the result in the mentioned variable.
Inplace operator’s “iadd()” method, implements “a+=b” in case of
mutable targets. But in case of immutable targets normal “a+b”
is implemented i.e. the value of the first operator isn't changed.

Note: To use inplace operator, import operator library.
1. iadd() :- This function is used to assign and add the
current value. This operation does “a+=b” operation. Assigning
is not performed in case of immutable containers, such as strings,
numbers and tuples.

2. iconcat() :- This function is used to concat one string at end of second.

3. isub() :- This function is used to assign and subtract the current
value. This operation does “a-=b” operation. Assigning is not performed
in case of immutable containers, such as strings, numbers and tuples.

4. imul() :- This function is used to assign and multiply the current
value. This operation does “a*=b” operation. Assigning is not performed
in case of immutable containers, such as strings, numbers and tuples.

5. itruediv() :- This function is used to assign and divide the current
value. This operation does “a/=b” operation. Assigning is not performed
in case of immutable containers, such as strings, numbers and tuples.

6. imod() :- This function is used to assign and return remainder .
This operation does “a%=b” operation. Assigning is not performed in
case of immutable containers, such as strings, numbers and tuples.

1. ixor() :- This function is used to assign and xor the current value.
This operation does “a^ = b” operation. Assigning is not performed in
case of immutable containers, such as strings, numbers and tuples.

2. ipow() :- This function is used to assign and exponentiate the
current value. This operation does “a ** = b” operation. Assigning
is not performed in case of immutable containers, such as strings,
numbers and tuples.

3. iand() :- This function is used to assign and bitwise and the current
value. This operation does “a &= b” operation. Assigning is not performed
in case of immutable containers, such as strings, numbers and tuples.

4. ior() :- This function is used to assign and bitwise or the current
value. This operation does “a |=b ” operation. Assigning is not
performed in case of immutable containers, such as strings, numbers
and tuples.

5. ilshift() :- This function is used to assign and bitwise leftshift
the current value by second argument. This operation does “a <<=b ”
operation. Assigning is not performed in case of immutable containers,
 such as strings, numbers and tuples.

6. irshift() :- This function is used to assign and bitwise rightshift
the current value by second argument. This operation does “a >>=b ”
operation. Assigning is not performed in case of immutable containers,
such as strings, numbers and tuples.


'''
