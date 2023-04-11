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



