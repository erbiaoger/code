!! 模块提供拆分多个文件之间程序的方式。
	! 模块用于：
    !
	! 	包装子程序，数据和接口块。
	! 	定义，可以使用多于一个常规全局数据。
	! 	声明可以选择的任何程序内提供的变量。
	! 	导入整个模块，可使用在另一个程序或子程序
module constants
    implicit none
    real, parameter :: pi = 3.1415926536  
    real, parameter :: e = 2.7182818285 
    contains
        subroutine show_consts()
            print *, "Pi = ", pi
            print *, "e = ", e
        end subroutine show_consts

end module constants

!! 可以控制模块代码中使用的private 和 public 属性的访问性
    ! real, parameter, private :: pi = 3.1415926536  
    ! real, parameter, private :: e = 2.7182818285


program f_module
    use constants
    implicit none

    real :: x, ePowerx, area, radius
    x = 2.0; radius = 7.0
    ePowerx = e ** x
    area = pi * radius**2

    call show_consts()

    print*, "e raised to the power of 2.0 = ", ePowerx
    print*, "Area of a circle with radius 7.0 = ", area 

end program f_module