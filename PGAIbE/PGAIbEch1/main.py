from PGAIbEch1.Vector2D import Vector2D

larry = Vector2D()
print ("x = ", larry.x)
print ("y = ", larry.y)

test = Vector2D(10,20)
print ("x = ", test.x)
print ("y = ", test.y)

test2 = Vector2D(10)
print ("x = ", test2.x)
print ("y = ", test2.y)

print("Is larry zero? ", larry.isZero())
print("Is test zero? ", test.isZero())

print("test's length = ", test.Length())
print("larry's length = ", larry.Length())
print("test2's lengthSq = ", test2.LengthSq())

testNorm = test.Normalize()
print("test, normalized = ", testNorm.x, ",", testNorm.y)

test = Vector2D(10,20)
print ("x = ", test.x)
print ("y = ", test.y)

print("dot from test and test2 = ", test.Dot(test2))

new1 = Vector2D(1,2)
new2 = Vector2D(3,4)


print("signed angle between test and test2 = ", test.Sign(test2))

new1 += new2

print ("new1: x = ", new1.x, ", y = ", new1.y)

new1 -= new2

print ("new1: x = ", new1.x, ", y = ", new1.y)

new1 *= Vector2D(2,2)

print ("new1: x = ", new1.x, ", y = ", new1.y)

new1 /= Vector2D(2,2)

print ("new1: x = ", new1.x, ", y = ", new1.y)
