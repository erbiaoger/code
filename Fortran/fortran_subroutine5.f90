subroutine subrout(subr, xmin, xmax, n)
    implicit none
    real xmin, xmax, dx, y
    integer n, i
    dx = (xmax - xmin) / n
    do i = 0, n
        call subr(dx*i+xmin, y)
        print *, i, y
    enddo
end subroutine subrout

subroutine funcout(fun, xmin, xmax, n)
    implicit none
    real fun, xmin, xmax, x, dx, y
    integer n, i
    dx = (xmax - xmin) / n
    do i = 0, n
        x = dx*i + xmin
        y = fun(x) ** 3
        print *, x, y
    enddo
end subroutine funcout

subroutine sub(x, y)
    implicit none
    real y, x
    y = 2*sin(x) + cos(x**2)
end subroutine sub

function fun(x)
    implicit none
    real fun, x
    fun = sin(x) ** 3
end function fun

program test_func
    implicit none
    real, external :: fun
    external sub
    call subrout(sub, 0.0, 3.0, 10)
    call funcout(fun, 0.0, 3.0, 10)
end program test_func
! 主程序中的递归子程序调用声明只需要 external 加上子程序名即可，而主程序中的递归函数副程序
! 调用声明需要同时定义函数变量和函数名，因此写为 real, external :: 加上函数副程序名。
! 当然在直接调用函数副程序 fun 的子程序 funcout 中也需要定义函数同名变量，写为 real fun