program subroutine_program  
    integer m
    m = 21

    ! 调用子程序
    call subr1
    call subr2(1, 2, 3, m*5+1)

end program subroutine_program

! 带初始化变量的子程序
subroutine subr2(x1, x2, x3, x4)
    integer x1, x2, x3, x4
    print *, x1, x2, x3, x4
end subroutine subr2

! 不带初始化变量的子程序
subroutine subr1
    integer x
    x = 10
    print *, x
end subroutine subr1