program fortran_type
    integer m(4)      ! 长度为 10 的整数型数组
    real x(20), y(4, 5)
    complex matrix(5, 5)

    m(1) = 1; m(2) = 2; m(3) = 3; m(4) = 4

    print *, m
    print *, m(1:3)


end program fortran_type