package DAO;

import java.util.ArrayList;
import java.util.List;

public class StudentDaoImpl implements StudentDAO{
	
	//LIST is working as a database
	List<Student> students;
	
	public StudentDaoImpl() {
		students = new ArrayList<Student>();
		Student st1 = new Student("Marcela", 0);
		Student st2 = new Student("Patty", 1);
		
		students.add(st1);
		students.add(st2);
	}
	
	public void deleteStudent(Student student) {
		students.remove(student.getRollNo());
		System.out.println("Student: Roll No "+ student.getRollNo() +
				", delete from database.");
	}
	
	//retrive list of students from the database
	public List<Student> getAllStudents() {
		// TODO Auto-generated method stub
		return students;
	}
	
	public Student getStudent(int rollNo) {
		// TODO Auto-generated method stub
		return students.get(rollNo);
	}
	
	public void updateStudent(Student student) {
		students.get(student.getRollNo()).setName(student.getName());;
		System.out.println("Student: Roll No "+ student.getRollNo() +
				", updated in the database.");;
	}
}
