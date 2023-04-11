program fileIO
    implicit none
    call outputdata
end program fileIO

subroutine outputdata
    real, dimension(100) :: x, y
    real, dimension(100) :: p, q
    integer :: i

    do i = 1, 100
        x(i) = i * 0.1
        y(i) = sin(x(i)) * (1 - cos(x(i)/3.0))
    end do

    open(1, file='./example/data/data1.dat', status='new')
        do i = 1, 100
            write(1, *) x(i), y(i)
        end do
    close(1)

    open(2, file='./example/data/data1.dat', status='old')
        do i = 1, 100
            read(2, *) p(i), q(i)
        end do
    close(2)
    print *, p
    print *, q
end subroutine outputdata