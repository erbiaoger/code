program subroutine3
    implicit none
    integer, parameter :: n = 4, m = 10
    real a(n, m), b(n, m), c(10*n, 10*m), d(10*n, 10*m)
    a(1:n, 1:m) = 0
    write(*, *) a
end program subroutine3

