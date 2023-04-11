```toc

```
- [[#[个人仓库](https://github.com/erbiaoger/code/tree/main/Fortran)|[个人仓库](https://github.com/erbiaoger/code/tree/main/Fortran)]]
- [[#数据类型|数据类型]]
- [[#判断|判断]]
- [[#循环|循环]]
- [[#数组|数组]]
- [[#获取日期和时间|获取日期和时间]]
- [[#动态数组|动态数组]]
- [[#结构|结构]]
- [[#文件输入输出|文件输入输出]]
- [[#指针|指针]]
- [[#模块|模块]]
- [[#goto|goto]]
- [[#子程序，函数|子程序，函数]]

## [个人仓库](https://github.com/erbiaoger/code/tree/main/Fortran)

## 数据类型
|类型|定义|说明|
|--|--|--|
|整型|integer :: a|整数类型只能容纳整数值|
|实型|real :: a|存储的浮点数|
|复数|complex, parameter :: b = (10, 2)|一个复杂的数字有两部分，实数部分和虚数部分|
|布尔|logical, parameter :: c = .true.|只有两个逻辑值：.true. 和.false. 关系运算符 .and. .or. .not. .eqv. .neqv.|
|字符|character(len=40), name|字符串的长度可以通过len个符来指定。如果没有指定长度，它是1|
	Fortran语言的旧版本允许一个叫做隐式类型，也就是说，不必在使用前声明变量的功能。如果一个变量没有声明，则其名称为第一个字母，将确定其类型。

	其中i的变量名以 i, j, k, l, m, 或 n 开始，被认为是为整数变量，其余都是实型变量。但是，必须声明所有的变量，因为它是良好的编程习惯。开始程序如下：
```fortran
implicit none
```

## 判断
|语句 |描述|
|--|--|
|if… then 结构|if… then… end if** 语句由一个逻辑表达式后跟一个或多个语句|
|If… then...else 结构|**if… then**语句可以后跟一个可选的 **else statement,** 它执行时，逻辑表达式为假。|
|if...else if...else 结构|**if** 语句构建体可具有一个或多个可选的 **else-if** 结构。当 **if** 条件不满足，则紧跟 **else-if** 执行。当 **else-if** 还失败，其继续 **else-if** 语句（如果有的话）被执行，依此类推。|
|内嵌 if 结构|可以使用一个 **if** 或 **else if** 语句在另外一个 **if** 或 **else if** 语句内部|
|select case 语句|Select Case语句允许一个变量的值对的列表，平等进行测试。|
|内嵌select case 结构|可以使用一个SELECT CASE语句中的另一个选择case语句。| 
```fortran
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
```

## 循环
|循环类型 |描述|
|--|--|
|do循环|该构建体使得语句或一系列语句迭代进行，当一个给定的条件为真。|
|do while循环|重复声明语句或一组，当给定的条件为真。它测试的条件执行循环体之前。|
|内嵌循环|可以使用一个或多个循环结构在其他循环结构里面。| 

|控制语句| 描述|
|--|--|
|exit|如果被执行exit语句则会退出该循环，并且该程序的继续执行第一个可执行语句结束之后的语句执行。|
|cycle|如果执行了一个循环语句，则程序继续到下一次迭代的起始位置。|
|stop|如果想执行的程序停止，可以插入声明一个stop语句|

```fortran
program fortran_do
    integer a(10)
    integer b(10, 5)

    do n = 1, 10
        a(n) = n
    enddo
    print *, a

    do n = 1, 20, 2
        a(n/2 + 1) = n
    enddo
    print *, a

    do n = 20, 1, -2
        a(n/2) = n
    enddo
    print *, a

    do n = 1, 10
        a(n) = n 
        do m = 1, 10, 2
            b(n, nint(m/2.0)) = a(n) + m 
        enddo
    enddo
    print *, b


end program fortran_do
```
```fortran
program fortran_while
    integer n
    n = 10
    do while (n > 0)
        print *, n**2
        n = n - 1
    enddo

end program fortran_while
```
```fortran
program exit_cycle
    sum = 0
    do i = 1, 10
        sum = sum + i
        if (sum > 10) exit
    enddo
    print *, i, sum

    sum = 0
    do i = 1, 10
        sum = sum + i
        if (sum > 10) goto 8
    enddo
8   print *, i, sum

    sum = 0
    do i = 1, 10
        sum = sum + i
        if (sum <= 10) cycle
        exit
    enddo
    print *, i, sum

    sum = 0
    do i = 1, 10
        do j = 1, 10
            sum = sum + i + j 
            if (sum > 10) goto 10
        enddo
    enddo
10  print *, i, j, sum

    sum = 0
    out: do i = 1, 10
            do j = 1, 10
                sum = sum + i + j 
                if (sum > 10) exit out
             enddo
        enddo out
    print *, i, j, sum 

end program exit_cycle
```

## 数组
```fortran
real a(10)
real, dimension(10, 20) :: a

a = 
```
```fortran
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
```
```fortran
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
```

## 获取日期和时间
```fortran
program  datetime
implicit none

   character(len = 8) :: dateinfo ! ccyymmdd
   character(len = 4) :: year, month*2, day*2

   character(len = 10) :: timeinfo ! hhmmss.sss
   character(len = 2)  :: hour, minute, second*6

   call  date_and_time(dateinfo, timeinfo)

   !  let’s break dateinfo into year, month and day.
   !  dateinfo has a form of ccyymmdd, where cc = century, yy = year
   !  mm = month and dd = day

   year  = dateinfo(1:4)
   month = dateinfo(5:6)
   day   = dateinfo(7:8)

   print*, 'Date String:', dateinfo
   print*, 'Year:', year
   print *,'Month:', month
   print *,'Day:', day

   !  let’s break timeinfo into hour, minute and second.
   !  timeinfo has a form of hhmmss.sss, where h = hour, m = minute
   !  and s = second

   hour   = timeinfo(1:2)
   minute = timeinfo(3:4)
   second = timeinfo(5:10)

   print*, 'Time String:', timeinfo
   print*, 'Hour:', hour
   print*, 'Minute:', minute
   print*, 'Second:', second   
   
end program  datetime
```

## 动态数组
```fortran
!! Fortran动态数组
program array_allocate
    implicit none
    ! call dynaminc_array
    ! call dataStatement
    call whereStatement
end program array_allocate


!! 动态数组的属性使用 allocatable 声明
subroutine dynaminc_array
    implicit none
    real, dimension(:, :), allocatable :: darray
    integer :: s1, s2
    integer :: i, j

    print *, "Enter the size of the array: "
    read *, s1, s2

    allocate (darray(s1, s2))

    do i = 1, s1
        do j = 1, s2
            darray(i, j) = i * j
            print *, "darray(", i, ",", j, ") = ", darray(i, j) 
        end do
    end do
    
    deallocate (darray)
end subroutine dynaminc_array

!! data 语句可用于初始化多个阵列，或用于阵列部分的初始化
subroutine dataStatement
    implicit none
    integer :: a(5), b(3, 3), c(10), i, j
    data a /7, 8, 9, 10, 11/
    data b(1,:) /1,1,1/ 
    data b(2,:)/2,2,2/ 
    data b(3,:)/3,3,3/ 
    data (c(i),i=1,10,2) /4,5,6,7,8/ 
    data (c(i),i=2,10,2)/5*2/
    print *, 'The A array: '
    do j = 1, 5
        print *, a(j)
    end do 

end subroutine dataStatement

!! where语句可以使用数组中的某些元素在一个表达式，根据一些逻辑条件的结果。
!! 它允许表达的执行在一个元素上，如果给定的条件为真
subroutine whereStatement
implicit none

   integer :: a(3,5), i , j
   
   do i = 1,3
      do j = 1, 5                
         a(i,j) = j-i          
      end do 
   end do
   
   Print *, 'The A array:'
   
   do i = lbound(a,1), ubound(a,1)
      write(*,*) (a(i,j), j = lbound(a,2), ubound(a,2))
   end do
   
   where( a<0 ) 
      a = 1 
   elsewhere
      a = 5
   end where
  
   Print *, 'The A array:'
   do i = lbound(a,1), ubound(a,1)
      write(*,*) (a(i,j), j = lbound(a,2), ubound(a,2))
   end do   
   
end subroutine whereStatement
```

## 结构
```fortran
program deriveDataType
    implicit none
    type Books
        character(len=50) :: title
        character(len=50) :: author
        character(len=150) :: subject
        integer :: book_id
    end type Books

    type(Books) :: book1
    type(Books) :: book2
    !declaring array of books
    type(Books), dimension(2) :: list 

    book1%title = "C Programming"
    book1%author = "Nuha Ali"
    book1%subject = "C Programming Tutorial"
    book1%book_id = 6495407
    book2%title = "Telecom Billing"
    book2%author = "Zara Ali"
    book2%subject = "Telecom Billing Tutorial"
    book2%book_id = 6495700

    !display book info
    Print *, book1%title 
    Print *, book1%author 
    Print *, book1%subject 
    Print *, book1%book_id
    Print *, book2%title 
    Print *, book2%author 
    Print *, book2%subject 
    Print *, book2%book_id



    !accessing the components of the structure

    list(1)%title = "C Programming"
    list(1)%author = "Nuha Ali"
    list(1)%subject = "C Programming Tutorial"
    list(1)%book_id = 6495407 

    list(2)%title = "Telecom Billing"
    list(2)%author = "Zara Ali"
    list(2)%subject = "Telecom Billing Tutorial"
    list(2)%book_id = 6495700

    !display book info

    Print *, list(1)%title 
    Print *, list(1)%author 
    Print *, list(1)%subject 
    Print *, list(1)%book_id  

    Print *, list(1)%title 
    Print *, list(2)%author 
    Print *, list(2)%subject 
    Print *, list(2)%book_id  

end program deriveDataType
```

## 文件输入输出
```fortran
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
```

## 指针
```fortran
program pointerExample
    implicit none

    !! 分配指针的空间
    integer, pointer :: p1
    integer, target :: t1
    allocate(p1)

    p1 = 1
    print *, p1
    p1 = p1 + 4
    print *, p1

    !! 目标是另一个正态变量，空间预留给它。目标变量必须与目标属性进行声明。
	!! 一个指针变量使用的关联操作符使目标变量相关联(=>)。
    p1 => t1
    p1 = 1
    print *, p1
    print *, t1
    p1 = p1 + 4
    print *, p1
    print *, t1
    t1 = 8
    print *, p1
    print *, t1


end program pointerExample
```

## 模块
```fortran
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
```

## goto
```fortran
program fortran_goto
    integer a, b
    goto 6
    a = 10
    b = 11
6   a = 778
    b = 9898
    print *, a
    print *, b

end program fortran_goto
```

## 子程序，函数
```fortran
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
```


