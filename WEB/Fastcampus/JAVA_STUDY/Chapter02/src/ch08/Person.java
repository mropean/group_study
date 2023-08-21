package ch08;

public class Person {
	public int height;
	public int weight;
	public int age;
	public String name;
	public String sex;
	
	public void info() {
		System.out.println("키가 "+height+"이고 몸무게가 "+weight+"인 "+sex+"이 있습니다."
				+ " 이름은 " + name + " 이고 나이는 " + age +"세입니다.");
	}
}
