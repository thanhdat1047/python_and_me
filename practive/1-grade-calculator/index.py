# 1. Nhập số lượng môn học
# 2. Lặp để nhập điểm từng môn (validation 0-10)
# 3. Tính điểm trung bình = tổng điểm / số môn
# 4. Xác định xếp loại dựa trên điểm TB
# 5. Hiển thị kết quả chi tiết

def grade_calculator():
    while True:
        try:
            num_subs = int(input("Nhap so mon hoc: "))
            if num_subs > 0:
                break
            print('So mon hoc phai lon hon > 0')
        except ValueError:
            print('Vui long nhap so nguyen')
    
    # Buoc 2: Nhap diem tung mon
    grades = []
    
    for i in range(num_subs):
        while True:
            try:
                grade = float(input(f"Diem mon thu {i+1}: "))
                
                if 0 <= grade <= 10:
                    grades.append(grade)
                    break
                else:
                    print("Diem phai tu 0-10")
            except ValueError:
                print("Vui long nhap so hop le")
        
    average = sum(grades) / len(grades)
    
    def classify_grade(avg):
        if avg >= 9.0:
            return "A+"
        elif avg >= 8.0:
            return "A"
        elif avg >= 7.0:
            return "B"
        elif avg >= 5.0:
            return "C"
        else: 
            return "D"
    
    letter_grade = classify_grade(average)
    
    print(f"Điểm trung bình: {average:.2f}")
    print(f"Xếp loại: ({letter_grade})")
    
grade_calculator()
    
        