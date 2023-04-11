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