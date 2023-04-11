program array1
    implicit none
    call arrayReduction
end program array1

subroutine arrayReduction
    implicit none
    real a(3, 2)
    a = reshape((/5, 9, 6, 10, 8, 12/), (/3, 2/))

    print *, a
    print *, all(a > 5)
    print *, any(a > 5)
    print *, count(a > 5)
    print *, all(a >= 5 .and. a < 10)
    print *, maxval(a)
    print *, minval(a)
    print *, sum(a)
    print *, product(a)         ! 返回数组a中所有元素的积。
    print *, lbound(a, dim=1)   ! 返回数组a在第1维的下限（即第1维的起始索引）
    print *, ubound(a, dim=1)   ! 返回数组a在第1维的上限（即第1维的结束索引）
    print *, shape(a)           ! 形状 (3, 2)
    print *, size(a)            ! 大小 3 x 2 = 6
end subroutine arrayReduction
