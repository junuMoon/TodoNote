# Chapter 1. Vectors 

## Section 1-1. Vectors and Matrices

- D1: League of legend, (x-coordinate of mouse pointer, y-coordinate of mouse pointer, which skill was used) can be be described by vectors in R3?.
	- The League of Legends example you provided could be described using a vector in R3, but not in the way you described it. Here’s why:
	- A vector in R3 consists of three components that represent a point or a direction in three-dimensional space. In the context of League of Legends, we could use a vector in R3 to describe the position of a champion on the map, or the direction in which a projectile is traveling.
	- However, the example you provided involves three pieces of information: the x-coordinate of the mouse pointer, the y-coordinate of the mouse pointer, and which skill was used. This is not a three-dimensional vector, but rather a three-tuple (or triple) of values.
	- To represent this information using vectors, we could assign each skill a unique vector in R3, and then use the x- and y-coordinates of the mouse pointer to define a point in two-dimensional space. We could then combine the skill vector and the mouse point vector to create a new vector in R3 that represents the skill being used at that particular point in the game.
- D2: Time can be expressed as both scaler and vector. **v**(date, hour, minute, …). Scaler: timestamps. And time can be said “5 minutes ago”
	- Your answer is partly correct. Time can be expressed as both a scalar and a vector, depending on the context and how it is being used.
	- When time is being used to represent a single point in time, such as a timestamp or a duration, it is considered a scalar quantity. For example, “10:30 AM” or “30 minutes” are scalar quantities of time.
	- On the other hand, when time is being used to represent a change or a displacement, such as the time it takes to travel from one location to another or the duration of a process, it can be represented as a vector quantity. For example, “2 hours east” or “30 minutes northwest” are vector quantities of time.
	- Your answer touches on some aspects of the time representation but could be improved for better clarity and accuracy.
	- Time is generally considered a scalar quantity rather than a vector. Scalars have only magnitude, while vectors have both magnitude and direction. In most physical applications, time is measured in units such as seconds, minutes, or hours and has no inherent direction associated with it. For example, when we say “5 minutes ago,” we refer to a duration, which is still a scalar quantity.
	- However, you mentioned representing time as a vector with components like date, hour, and minute. While it is possible to represent time-related information in this manner, it doesn’t make time itself a vector quantity. In this case, you are dealing with a structured data representation rather than the fundamental nature of time as a physical quantity.
	- So, in summary, time is generally considered a scalar quantity, with specific representations or data structures allowing for more complex descriptions of time-related information.
- D3. if the sum of three vectors in R^3 is zero, must they lie in the same plane? Explain.
	- A: x+y+z=0 -> y=-x-z. y should be expressed by combination of x and z. So that they must lie in the same plane
	- Your answer is on the right track, but it could be explained more clearly.
	- If the sum of three vectors in R^3 is zero, it means that vector x + vector y + vector z = 0. This can be re-written as vector y = - (vector x + vector z).
	- In this case, vector y is the negative sum of vectors x and z, meaning that it can be represented as a linear combination of vectors x and z. Since vector y can be expressed as a linear combination of the other two vectors, all three vectors must lie in the same plane.

## Section 1-3. Vector equations of Lines and Planes
- How can we tell v1 = (5, -1,1) and v2 = (-1, 8, 1) are not collinear?
    - D1: 5 = -k, -1 = 8k, 1 = k
    - D2: cos(θ) = (v1 • v2) / (||v1|| ||v2||) / θ = arccos(-12 / (sqrt(27) * sqrt(66)))
- what is normal vector?
    - A normal vector, often denoted as 'n', is a vector that is perpendicular (orthogonal) to a surface or a plane in 3-dimensional space. In the context of a plane, a normal vector defines the orientation of the plane, as it is orthogonal to every vector lying in the plane.
    - For example, if you have a plane with the equation Ax + By + Cz + D = 0, the normal vector can be represented as n = (A, B, C). This is because the dot product of the normal vector and any vector within the plane will be zero, indicating their perpendicular relationship.
- Check my reasoning is right. (1, 1, 4), (2, -3, 1), and (3,5, -2), point=(1,1,4) others are v1 and v2. v1 and v2 aren't collinear cause its cross product aren't (0,0,0). So k1*v1 + k2*v2 make a plane.
    - Your reasoning is correct. Let me summarize and clarify the steps:
    - Given the points (1, 1, 4), (2, -3, 1), and (3, 5, -2). Take the first point as the reference point P0 = (1, 1, 4).
    - Create two vectors using the other two points, v1 and v2:
    - v1 = (2, -3, 1) - (1, 1, 4) = (1, -4, -3) / v2 = (3, 5, -2) - (1, 1, 4) = (2, 4, -6)
    - Check if v1 and v2 are collinear by calculating their cross product. If the cross product is a zero vector (0, 0, 0), they would be collinear, but in this case: v1 x v2 = (36, 0, 8)
    - Since v1 and v2 are not collinear, they span a plane. Any linear combination of v1 and v2, i.e., k1 * v1 + k2 * v2, where k1 and k2 are scalars, will produce a vector within the plane.
    - The plane containing the given points can be represented using the point P0 and the linear combination of vectors v1 and v2: P = P0 + k1 * v1 + k2 * v2
- Check my reasoning. There is x0 and direction vector v1 and v2. if v1 and v2 are orthogonal, x0 + t1v1 + t2v2 is a line.
    - In other words, when v1 and v2 are orthogonal, moving along the direction of v1 does not affect the position in the direction of v2, and vice versa. This property ensures that you can uniquely determine any point on the line using the two orthogonal direction vectors and their scalar parameters. -> False
