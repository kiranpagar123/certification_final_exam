def street_light_coverage(L, arr):
    arr.sort()  # sort the array in increasing order of Xi
    covered_len = arr[0][1] - arr[0][0]  # length covered by first street light
    prev_end = arr[0][1]  # end point of first street light
    for i in range(1, L):
        start = arr[i][0]
        end = arr[i][1]
        if start <= prev_end:  # street lights overlap
            covered_len += end - prev_end
            prev_end = end
        else:  # street lights do not overlap
            covered_len += end - start
            prev_end = end
    return covered_len


print(street_light_coverage(1,[(5,10)]))
print(street_light_coverage(2,[(5,10),(8,12)]))