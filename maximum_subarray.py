# Function
def f(a, l):
    m = 0
    for i in range(len(a)):
        s = 0
        for j in range(i, len(a)):
            s += a[j]
            if s <= l:
                m = max(m, s)
    return m

# Test Case 1
a1 = [2, 1, 3, 4]
l1 = 5
n1 = len(a1)
m1 = n1 // 2
b1 = a1[:m1]
c1 = a1[m1:]
p1 = f(b1, l1)
q1 = f(c1, l1)
print("Test 1")
print("Left:", b1)
print("Right:", c1)
print("Max left:", p1)
print("Max right:", q1)
print("Best:", max(p1, q1))
print()

# Test Case 2
a2 = [2, 2, 2, 2]
l2 = 4
n2 = len(a2)
m2 = n2 // 2
b2 = a2[:m2]
c2 = a2[m2:]
p2 = f(b2, l2)
q2 = f(c2, l2)
print("Test 2")
print("Left:", b2)
print("Right:", c2)
print("Max left:", p2)
print("Max right:", q2)
print("Best:", max(p2, q2))
print()

# Test Case 3
a3 = [1, 5, 2, 3]
l3 = 5
n3 = len(a3)
m3 = n3 // 2
b3 = a3[:m3]
c3 = a3[m3:]
p3 = f(b3, l3)
q3 = f(c3, l3)
print("Test 3")
print("Left:", b3)
print("Right:", c3)
print("Max left:", p3)
print("Max right:", q3)
print("Best:", max(p3, q3))

# Test Case 4
a4 = [6, 7, 8]
l4 = 5
b4 = a4[:len(a4)//2]
c4 = a4[len(a4)//2:]
x4 = max(f(b4, l4), f(c4, l4))
print("Test 4")
print("Left:", b4)
print("Right:", c4)
print("Max left:", f(b4, l4))
print("Max right:", f(c4, l4))
print("Best:", x4 if x4 > 0 else "No feasible subarray")
print()


# Test Case 5
a5 = [1, 2, 3, 2, 1]
l5 = 5
b5 = a5[:len(a5)//2]
c5 = a5[len(a5)//2:]
print("Test 5")
print("Left:", b5)
print("Right:", c5)
print("Max left:", f(b5, l5))
print("Max right:", f(c5, l5))
print("Best:", max(f(b5, l5), f(c5, l5)))


#Test case 6
a6 = [1, 1, 1, 1, 1]
l6 = 4
b6 = a6[:len(a6)//2]
c6 = a6[len(a6)//2:]
print("Test 6")
print("Left:", b6)
print("Right:", c6)
print("Max left:", f(b6, l6))
print("Max right:", f(c6, l6))
print("Best:", max(f(b6, l6), f(c6, l6)))

# Test Case 7
a7 = [4, 2, 3, 1];
l7 = 5
b7 = a7[:len(a7)//2];
c7 = a7[len(a7)//2:]
print("Test 7");
print("Left:", b7);
print("Right:", c7)
print("Max left:", f(b7, l7));
print("Max right:", f(c7, l7))
print("Best:", max(f(b7, l7), f(c7, l7)));
print()

# Test Case 8
a8 = []; l8 = 10
b8 = a8[:len(a8)//2]; c8 = a8[len(a8)//2:]
x8 = max(f(b8, l8), f(c8, l8))
print("Test 8"); print("Left:", b8); print("Right:", c8)
print("Max left:", f(b8, l8)); print("Max right:", f(c8, l8))
print("Best:", x8 if x8 > 0 else "No subarray")

# Function to find max subarray sum under a limit
def f(a, l):
    m = 0
    for i in range(len(a)):
        s = 0
        for j in range(i, len(a)):
            s += a[j]
            if s <= l:
                m = max(m, s)
    return m

# Test Case 1
a1 = [2, 1, 3, 4]; l1 = 5
b1 = a1[:len(a1)//2]; c1 = a1[len(a1)//2:]
print("Test 1"); print("Left:", b1); print("Right:", c1)
print("Max left:", f(b1, l1)); print("Max right:", f(c1, l1))
print("Best:", max(f(b1, l1), f(c1, l1))); print()

# Test Case 2
a2 = [2, 2, 2, 2]; l2 = 4
b2 = a2[:len(a2)//2]; c2 = a2[len(a2)//2:]
print("Test 2"); print("Left:", b2); print("Right:", c2)
print("Max left:", f(b2, l2)); print("Max right:", f(c2, l2))
print("Best:", max(f(b2, l2), f(c2, l2))); print()

# Test Case 3
a3 = [1, 5, 2, 3]; l3 = 5
b3 = a3[:len(a3)//2]; c3 = a3[len(a3)//2:]
print("Test 3"); print("Left:", b3); print("Right:", c3)
print("Max left:", f(b3, l3)); print("Max right:", f(c3, l3))
print("Best:", max(f(b3, l3), f(c3, l3))); print()

# Test Case 4
a4 = [6, 7, 8]; l4 = 5
b4 = a4[:len(a4)//2]; c4 = a4[len(a4)//2:]
x4 = max(f(b4, l4), f(c4, l4))
print("Test 4"); print("Left:", b4); print("Right:", c4)
print("Max left:", f(b4, l4)); print("Max right:", f(c4, l4))
print("Best:", x4 if x4 > 0 else "No feasible subarray"); print()

# Test Case 5
a5 = [1, 2, 3, 2, 1]; l5 = 5
b5 = a5[:len(a5)//2]; c5 = a5[len(a5)//2:]
print("Test 5"); print("Left:", b5); print("Right:", c5)
print("Max left:", f(b5, l5)); print("Max right:", f(c5, l5))
print("Best:", max(f(b5, l5), f(c5, l5))); print()

# Test Case 6
a6 = [1, 1, 1, 1, 1]; l6 = 4
b6 = a6[:len(a6)//2]; c6 = a6[len(a6)//2:]
print("Test 6"); print("Left:", b6); print("Right:", c6)
print("Max left:", f(b6, l6)); print("Max right:", f(c6, l6))
print("Best:", max(f(b6, l6), f(c6, l6))); print()

# Test Case 7
a7 = [4, 2, 3, 1]; l7 = 5
b7 = a7[:len(a7)//2]; c7 = a7[len(a7)//2:]
print("Test 7"); print("Left:", b7); print("Right:", c7)
print("Max left:", f(b7, l7)); print("Max right:", f(c7, l7))
print("Best:", max(f(b7, l7), f(c7, l7))); print()

# Test Case 8
a8 = []; l8 = 10
b8 = a8[:len(a8)//2]; c8 = a8[len(a8)//2:]
x8 = max(f(b8, l8), f(c8, l8))
print("Test 8"); print("Left:", b8); print("Right:", c8)
print("Max left:", f(b8, l8)); print("Max right:", f(c8, l8))
print("Best:", x8 if x8 > 0 else "No subarray"); print()

# Test Case 9
a9 = [1, 2, 3];
l9 = 0
b9 = a9[:len(a9)//2];
c9 = a9[len(a9)//2:]
x9 = max(f(b9, l9), f(c9, l9))
print("Test 9");
print("Left:", b9);
print("Right:", c9)
print("Max left:", f(b9, l9));
print("Max right:", f(c9, l9))
print("Best:", x9 if x9 > 0 else "No subarray")

#test case 10:
resources = list(range(1, 100001))
constraint = 10**9
print("Test 10 - Stress Test")
print("Length of resources:", len(resources))
expected_sum = sum(resources)
if expected_sum <= constraint:
    print("Expected sum (entire array):", expected_sum)
else:
    print("Expected sum would exceed constraint")
