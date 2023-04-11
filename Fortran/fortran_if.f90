program fortran_if
    integer n, i
    n = 10; i = -4
    if (i < 0) n = 5
    print *, n

    ! if then
    if (i < 0) then
        n = 5
    endif
    print *, n

    ! if else
    if (i > 0) then
        n = 8
    else 
        n = 5
    endif
    print *, n

    ! if elif else
    if (i > 0) then
        n = 8
    else if (i /= -2) then     ! /= 不等于
        n = 6
    else 
        n = 5
    endif
    print *, n

    ! .and. .or. .not.
    if (i < 0 .and. i > -2) then
        n = 5
    else 
        n = 10
    endif
    print *, n

end program fortran_if