program fortran_do
    integer a(10)
    integer b(10, 5)

    do n = 1, 10
        a(n) = n
    enddo
    print *, a

    do n = 1, 20, 2
        a(n/2 + 1) = n
    enddo
    print *, a

    do n = 20, 1, -2
        a(n/2) = n
    enddo
    print *, a

    do n = 1, 10
        a(n) = n 
        do m = 1, 10, 2
            b(n, nint(m/2.0)) = a(n) + m 
        enddo
    enddo
    print *, b


end program fortran_do