program fortran_while
    integer n
    n = 10
    do while (n > 0)
        print *, n**2
        n = n - 1
    enddo

end program fortran_while