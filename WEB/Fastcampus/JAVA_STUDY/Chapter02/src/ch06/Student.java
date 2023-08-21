package ch06;

public class Student {
	public int studentNumber;
	public String studentName;
	public int grade;
	
	// default 생성자
	public Student() {}
	
	// 매개변수가 있는 생성자
	public Student(int studentNumber, String studentName, int grade) {
		// 입력된 매개변수로 초기화
		// Student 클래스의 멤버 변수 / 매개변수
		this.studentNumber = studentNumber; 
		this.studentName = studentName;
		this.grade = grade;
	}
	
	public String showStudentInfo() {
		// 멤버 변수와 지역 변수는 다르다.
		// 객체가 생성될 때 멤버 변수는 초기화 된다.
		// 해당 지역에서 초기화 되지 않는 변수는 return 할 수 없다.
		return studentName + "학생의 학번은 " + studentNumber + "이고, " + grade + "학년 입니다."; 
	}
}
