! program fortran_continue
!     integer a, b
! 1   a = 10
!     b = 11
! 6   a = 778
!     b = 9898
!     goto 1
!     print *, a
!     print *, b
! end program fortran_continue
! 无限循环， 不可取
! 为了提高代码可读性，我们不想将 goto 语句跳转的行直接指向一个操作或者命令，这时我们就可以用 continue 来代替跳转行
program fortran_continue
    integer a, b
    a = 10
    b = 11
    a = 778
    b = 9898
    goto 1
    print *, a
1   continue
    print *, b

end program fortran_continue
