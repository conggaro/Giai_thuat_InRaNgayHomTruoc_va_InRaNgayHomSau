# Yêu cầu:
# 1. nhập vào ngày
# 2. nhập vào tháng
# 3. nhập vào năm

# 4. in ra ngày/tháng/năm hôm qua
# 5. in ra ngày/tháng/năm ngày mai

ngay = int(input())

thang = int(input())

nam = int(input())

# việc 1:
# kiểm tra xem có phải năm nhuận không
# năm nhuận             --> 29 ngày (tháng 2)
# năm không nhuận       --> 28 ngày (tháng 2)

def KiemTraNamNhuan(thamSo):
    kiemTra1 = True if thamSo % 400 == 0 else False
    kiemTra2 = True if thamSo % 4 == 0 else False
    kiemTra3 = True if thamSo % 100 != 0 else False
    
    if kiemTra1 or (kiemTra2 and kiemTra3):
        return True
    else:
        return False

# việc 2:
# viết 1 cái hàm thêm số 0 ở đầu
def Them_So_0(thamSo):
    if thamSo < 10:
        return "0" + str(thamSo)
    else:
        return thamSo

# trường hợp năm nhuận
if KiemTraNamNhuan(nam) == True:
        
        if thang == 1:
            tong_ngay = 31
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 30
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"31/12/{nam - 1}")           # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")  # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 31)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/{Them_So_0(thang + 1)}/{nam}")
        elif thang == 2:
            tong_ngay = 29 # vì năm nhuận có 29 ngày
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 29
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"31/{Them_So_0(thang - 1)}/{nam}")          # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")      # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 29)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/{Them_So_0(thang + 1)}/{nam}")
        elif thang == 3:
            tong_ngay = 31
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 30
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"29/{Them_So_0(thang - 1)}/{nam}")          # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")      # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 31)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/{Them_So_0(thang + 1)}/{nam}")
        elif thang == 4:
            tong_ngay = 30
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 29
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"31/{Them_So_0(thang - 1)}/{nam}")          # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")      # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 30)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/{Them_So_0(thang + 1)}/{nam}")
        elif thang == 5:
            tong_ngay = 31
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 30
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"30/{Them_So_0(thang - 1)}/{nam}")          # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")      # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 31)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/{Them_So_0(thang + 1)}/{nam}")
        elif thang == 6:
            tong_ngay = 30
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 29
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"31/{Them_So_0(thang - 1)}/{nam}")          # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")      # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 31)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/{Them_So_0(thang + 1)}/{nam}")
        elif thang == 7:
            tong_ngay = 31
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 30
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"30/{Them_So_0(thang - 1)}/{nam}")          # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")      # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 31)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/{Them_So_0(thang + 1)}/{nam}")
        elif thang == 8:
            tong_ngay = 31
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 30
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"31/{Them_So_0(thang - 1)}/{nam}")          # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")      # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 31)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/{Them_So_0(thang + 1)}/{nam}")
        elif thang == 9:
            tong_ngay = 30
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 29
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"31/{Them_So_0(thang - 1)}/{nam}")          # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")      # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 30)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/{Them_So_0(thang + 1)}/{nam}")
        elif thang == 10:
            tong_ngay = 31
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 30
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"30/{Them_So_0(thang - 1)}/{nam}")          # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")      # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 31)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/{Them_So_0(thang + 1)}/{nam}")
        elif thang == 11:
            tong_ngay = 30
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 29
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"31/{Them_So_0(thang - 1)}/{nam}")          # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")      # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 31)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/{Them_So_0(thang + 1)}/{nam}")
        elif thang == 12:
            tong_ngay = 31
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 30
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"30/{Them_So_0(thang - 1)}/{nam}")          # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")      # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 31)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/01/{nam + 1}")
# trường hợp năm không nhuận
elif KiemTraNamNhuan(nam) == False:

        if thang == 1:
            tong_ngay = 31
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 30
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"31/12/{nam - 1}")           # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")  # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 31)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/{Them_So_0(thang + 1)}/{nam}")
        elif thang == 2:
            tong_ngay = 28 # vì năm không nhuận có 28 ngày
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 27
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"31/{Them_So_0(thang - 1)}/{nam}")          # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")      # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 28)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/{Them_So_0(thang + 1)}/{nam}")
        elif thang == 3:
            tong_ngay = 31
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 30
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"28/{Them_So_0(thang - 1)}/{nam}")          # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")      # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 31)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/{Them_So_0(thang + 1)}/{nam}")
        elif thang == 4:
            tong_ngay = 30
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 29
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"31/{Them_So_0(thang - 1)}/{nam}")          # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")      # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 30)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/{Them_So_0(thang + 1)}/{nam}")
        elif thang == 5:
            tong_ngay = 31
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 30
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"30/{Them_So_0(thang - 1)}/{nam}")          # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")      # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 31)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/{Them_So_0(thang + 1)}/{nam}")
        elif thang == 6:
            tong_ngay = 30
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 29
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"31/{Them_So_0(thang - 1)}/{nam}")          # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")      # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 31)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/{Them_So_0(thang + 1)}/{nam}")
        elif thang == 7:
            tong_ngay = 31
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 30
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"30/{Them_So_0(thang - 1)}/{nam}")          # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")      # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 31)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/{Them_So_0(thang + 1)}/{nam}")
        elif thang == 8:
            tong_ngay = 31
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 30
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"31/{Them_So_0(thang - 1)}/{nam}")          # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")      # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 31)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/{Them_So_0(thang + 1)}/{nam}")
        elif thang == 9:
            tong_ngay = 30
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 29
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"31/{Them_So_0(thang - 1)}/{nam}")          # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")      # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 30)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/{Them_So_0(thang + 1)}/{nam}")
        elif thang == 10:
            tong_ngay = 31
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 30
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"30/{Them_So_0(thang - 1)}/{nam}")          # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")      # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 31)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/{Them_So_0(thang + 1)}/{nam}")
        elif thang == 11:
            tong_ngay = 30
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 29
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"31/{Them_So_0(thang - 1)}/{nam}")          # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")      # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 31)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/{Them_So_0(thang + 1)}/{nam}")
        elif thang == 12:
            tong_ngay = 31
            # trường hợp 1:
            # trong khoảng từ ngày 2
            # đến tong_ngay - 1 = 30
            if 2 <= ngay and ngay <= (tong_ngay - 1):
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")
            
            # trường hợp 2:
            # rơi vào ngày 1
            elif ngay == 1:
                print(f"30/{Them_So_0(thang - 1)}/{nam}")          # in ra ngày hôm qua
                print(f"{Them_So_0(ngay + 1)}/{Them_So_0(thang)}/{nam}")      # in ra ngày mai

            # trường hợp 3:
            # rơi vào ngày cuối tháng (ngày 31)
            elif ngay == tong_ngay:
                print(f"{Them_So_0(ngay - 1)}/{Them_So_0(thang)}/{nam}")
                print(f"01/01/{nam + 1}")