program exit
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

    
end program exit