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

print("signed angle between test and test2 = ", test.Sign(test2))