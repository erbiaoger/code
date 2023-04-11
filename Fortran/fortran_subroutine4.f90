! Fortran 语言中全局变量必须使用 module 的方式单独定义。
! 当在主程序或子程序中需要使用这些已定义的全局变量时，首先要使用 
! use <module 名> 来声明引用，并且该声明应在 implicit none 之前
module global1
    real xais, yais
end module global1

! 有的时候子程序中可能并不需要 module 中定义的所有全局变量，只想引入几个有关的全局变量。
! 在 Fortran 语言中可以用 only 的语法来限定引入的全局变量
module global2
    real x1, x2, x3
    integer y1, y2, y3
    complex z1, z2, z3
end module global2


! 函数副程序
program func
    use global1
    ! 限定引入的全局变量
    use global2, only : x2, z1
    implicit none

    real x, y, square
    x = 4.0
    y = 3.0 * square(x+1.0) + 50.5
    print *, x, y

    xais = 5.0; yais = 100.0
    call subr1
    print *, xais, yais
end program func

! 在某种程度上，函数只是子程序的替代，但是对于 Fortran 来说，
! 函数必须将函数名作为变量进行声明，并将计算的结果赋给这个函数名同名变量。
function square(x)
    implicit none
    real square, x
    square = x * x
end function square



subroutine subr1
    use global1
    implicit none
    print *, xais, yais
    yais = 25.0
end subroutine subr1