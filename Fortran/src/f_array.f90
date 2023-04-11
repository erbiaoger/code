program array
    implicit none
    ! call arraySubsection
    ! call arrayDotProduct
    call matMulProduct
end program array

subroutine arraySubsection
    implicit none
    real, dimension(10) :: a, b
    integer :: i, asize, bsize

    a(1:7) = 5.0
    a(8:) = 0.0
    b(2:10:2) = 3.9
    b(1:9:2) = 2.5

    asize = size(a)
    bsize = size(b)

    do i = 1, asize
        Print *, a(i)
    enddo

    do i = 1, bsize
        print *, b(i)
    enddo

end subroutine arraySubsection

subroutine arrayDotProduct
    ! 内积
    implicit none
    real, dimension(5) :: a, b
    integer :: i, asize, bsize

    asize = size(a)
    bsize = size(b)

    do i = 1, asize
        a(i) = i
    end do

    do i = 1, bsize
        b(i) = i*2
    end do

    do i = 1, asize
        print *, a(i)
    end do

    do i = 1, bsize
        print *, b(i)
    end do

    print *, 'Vector Multiplicatioon: Dot Product: '
    print *, dot_product(a, b)
end subroutine arrayDotProduct

subroutine matMulProduct
    implicit none
    integer, dimension(3, 3) :: a, b, c

    call dodo(a, 1)
    call dodo(b, 2)
    c = matmul(a, b)
    print *, 'a: ', a
    print *, 'b: ', b
    print *, 'c: ', c
end subroutine matMulProduct

subroutine dodo(a, n)
    implicit none
    integer, dimension(3, 3) :: a
    integer :: i, j, n
    do i = 1, 3
        do j = 1, 3
            if (n == 1) then
                a(i, j) = i + j 
            else if (n == 2) then
                a(i, j) = i * j
            end if
        end do
    end do 
end subroutine dodo