program subroutine1
    implicit none
    real x, y, p
    x = 10.0
    y = 30.0

    call subr1
    call subr2(x, y)

    call subr3(x, y, p)
    print *, x, y, p
end program subroutine1

subroutine subr1
    implicit none
    real x, y
    print *, x, y
end subroutine subr1

subroutine subr2(x, y)
    implicit none
    real x, y
    print *, x, y
end subroutine subr2

subroutine subr3(x, y, z)
    implicit none
    real x, y, z
    z = x * y
end subroutine subr3