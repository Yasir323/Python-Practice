'''
Array in Python can be created by importing array module.
array(data_type, value_list) is used to create an array
with data type and value list specified in its arguments.

Type        C Type              Python Type             Size
'b'         signed char         int                         1
'B'         unsigned char       int                         1
'u'         Py_UNICODE          unicode character           2
'h'         signed short        int                         2
'H'         unsigned short      int                         2
'i'         signed int          int                         2
'I'         unsigned int        int                         2
'l'         signed long         int                         4
'L'         unsigned long       int                         4
'q'         signed long long    int                         8
'Q'         unsigned long long  int                         8
'f'         float               float                       4
'd'         double              float                       8

ADDING ELEMENTS TO AN ARRAY:
Elements can be added to the Array by using built-in insert()
function. Insert is used to insert one or more data elements
into an array. Based on the requirement, a new element can
be added at the beginning, end, or any given index of array.
append() is also used to add the value mentioned in its
arguments at the end of the array.

REMOVING ELEMENTS FROM AN ARRAY:
Elements can be removed from the array by using built-in
remove() function but an Error arises if element doesn’t
exist in the set. Remove() method only removes one element at
a time, to remove range of elements, iterator is used.
pop() function can also be used to remove

SLICING ARRAY:
In Python array, there are multiple ways to print the whole
array with all the elements, but to print a specific range of
elements from the array, we use Slice operation. Slice operation
is performed on array with the use of colon(:). To print elements
from beginning to a range use [:Index], to print elements from
end use [:-Index], to print elements from specific Index till the
end use [Index:], to print elements within a range, use
[Start Index:End Index] and to print whole List with the use of
slicing operation, use [:]. Further, to print whole array in
reverse order, use [::-1].

SEARCHING ELEMETNS:
In order to search an element in the array we use a python in-built
index() method. This function returns the index of the first
occurrence of value mentioned in arguments.
'''
