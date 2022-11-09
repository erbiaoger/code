lc = 0.1;
Point(1) = {-1, -1, 0, lc};
Point(2) = {-1, 1, 0, lc};
Point(3) = {1, 1, 0, lc};
Point(4) = {1, -1, 0, lc};
Line(1) = {1, 2};
Line(2) = {2, 3};
Line(3) = {3, 4};
Line(4) = {4, 1};

//Point(5) = {0.1, 0, 0, lc};
//Point(6) = {0.1, 0.1, 0, lc};
//Point(7) = {0, 0.1, 0, lc};
//Point(8) = {0, 0, 0, lc};
//Line(5) = {5, 6};
//Line(6) = {6, 7};
//Line(7) = {7, 8};
//Line(8) = {8, 5};
Mesh.SubdivisionAlgorithm=1;
Line Loop(1) = {1, 2, 3, 4};
Plane Surface(1) = {1};
Recombine Surface{1};
//Curve Loop(2) = {5, 6, 7, 8};
//Plane Surface(2) = {2};
//Recombine Surface{1, 2};
Physical Line("Top") = {2};
Physical Line("Right") = {3};
Physical Line("Bottom") = {4};
Physical Line("Left") = {1};
Physical Surface("M1") = {1};
//Physical Surface("M2") = {2};