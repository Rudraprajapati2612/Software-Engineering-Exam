attendance = {}

def mark_attendance(student_id, status):
    attendance[student_id] = status

def test_mark_present():
    mark_attendance("S101", "Present")
    assert attendance["S101"] == "Present"
    print("Attendance marking test passed")

if __name__ == "__main__":
    test_mark_present()