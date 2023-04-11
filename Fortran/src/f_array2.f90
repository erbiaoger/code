program arrayConstruction
    implicit none
    ! 这个接口可以被用于定义一个模块中的多个子例程，这些子例程可以按照接口中声明的方式来定义它们的参数类型和个数。
    ! 接口的作用是让编译器能够在调用子例程时检查参数类型是否匹配，从而减少错误和调试时间。
    ! 需要注意的是，接口中声明的子例程并不会被编译或执行，它们只是用于告诉编译器这些子例程的参数类型和个数，
    ! 以便进行检查。在实际使用中，还需要在模块中定义这些子例程的具体实现。
    interface
        subroutine write_array(a)
            real :: a(:, :)
        end subroutine write_array

        subroutine write_1_array(a)
            logical :: a(:, :)
        end subroutine write_1_array
    end interface

    real, dimension(2, 3) :: tsource, fsource, result
    logical, dimension(2, 3) :: mask

    tsource = reshape( (/ 35, 23, 18, 28, 26, 39 /), &
                    (/ 2, 3 /) )
    fsource = reshape( (/ -35, -23, -18, -28, -26, -39 /), &
                    (/ 2,3 /) )
    mask = reshape( (/ .true., .false., .false., .true., &
                 .false., .false. /), (/ 2,3 /) )
    ! merge函数，将两个数组tsrouce和fsource按照mask中的逻辑值进行合并
    result = merge(tsource, fsource, mask)
    print *, tsource
    print *, fsource
    print *, mask
    print *, result
    ! call write_array(tsource)
    ! call write_array(fsource)
    ! call write_1_array(mask)
    ! call write_1_array(result)

end program arrayConstruction

subroutine write_array(a)
    implicit none
    real :: a(:, :)
    integer i, j
    do i = lbound(a, 1), ubound(a, 1)
        write(*, *) (a(i, j), j = lbound(a, 2), ubound(a, 2))
    end do 
    return 
end subroutine write_array

subroutine write_1_array(a)
    implicit none
    logical :: a(:, :)
    integer i, j
    do i = lbound(a, 1), ubound(a, 1)
        write(*, *) (a(i, j), j = lbound(a, 2), ubound(a, 2))
    end do 
    return 
end subroutine write_1_array