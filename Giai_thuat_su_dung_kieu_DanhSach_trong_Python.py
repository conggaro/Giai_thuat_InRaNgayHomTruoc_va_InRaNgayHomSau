# nhập vào ngày
d = int(input())

# nhập vào tháng
m = int(input())

# nhập vào năm
y = int(input())

dom = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# đây là kiểm tra năm nhuận
if (y % 400 == 0) or ((y % 4 == 0) and (y % 100 != 0)):
    dom[1] = 29

# ĐÂY LÀ IN RA NGÀY HÔM TRƯỚC
if (d == 1):
    if (m == 1):
        print(f"31/12/{y - 1}")
    
    elif (m != 1): 
        # tức là ngày nó bằng 1 nhưng tháng nó khác một nhá
        # đây là code in ra mấy cái ngày cuối tháng của tháng trước
        # vì đang check ngày bằng 1 mà
        print(f"{dom[m - 2]}/{(m - 1):{'0'}>2}/{y}")

elif (d != 1):
    print(f"{(d - 1):{'0'}>2}/{m:{'0'}>2}/{y}")

# ĐÂY LÀ IN RA NGÀY HÔM SAU
if(d == dom[m - 1]):
    # tức là cái ngày nhập vào mà bằng ngày cuối tháng
    # nếu là tháng 12 thì "year" cộng 1
    if (m == 12):
        print(f"01/01/{y + 1}")

    elif (m != 12):
        print(f"01/{(m + 1):{'0'}>2}/{y}")

if(d != dom[m -1]):
    print(f"{(d + 1):{'0'}>2}/{m}/{y}")