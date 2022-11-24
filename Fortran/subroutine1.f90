subroutine subr1(x, y, n)
        implicit none 
	real x, y
        integer n
        x = n
        y = y*x

end subroutine subr1

program stest1
        implicit none
        real x, y
        x = 5.0
        y = 100.0
        call subr1(x, y, 10)
        print *, x, y

end program stest1

