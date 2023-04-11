!! 数组变量
program subroutine2
    implicit none
    real a(10), b(10)
    call sub(a)
    print *, a
    call subr1(a, b, 10)
    print *, b
end program subroutine2

subroutine sub(x)
    implicit none
    real x(10)
    integer i
    do i = 1, 10
        x(i) = i
    enddo
end subroutine sub

subroutine subr1(a, b, n)
    implicit none
    real a(*), b(*)
    integer n, i
    do i = 1, n
        b(i) = a(i)
    enddo
end subroutine subr1