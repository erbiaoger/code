!! Fortran基本输入输出
program ioExample
    implicit none
    ! call printPi
    call printName

end program ioExample

subroutine printPi
    pi = 3.141592653589793238 
    
    print "(f6.3)", pi      ! 3.142
    print "(f10.7)", pi     ! 3.1415927
    print "(f20.15)", pi    ! 3.141592741012573
    print "(e16.4)", pi     ! 0.3142E+01
end subroutine printPi

subroutine printName
    character(len=15) :: first_name
    print *, "Enter your first name: "
    print *, "Up to 20 characters, please"

    read *, first_name
    print "(1x,a)", first_name      ! 用于空间输出
end subroutine printName