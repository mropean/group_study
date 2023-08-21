package ch08;

public class Test {

	public static void main(String[] args) {
		Person person = new Person();
		person.age = 37;
		person.height = 180;
		person.weight = 78;
		person.sex = "남성";
		person.name = "Tomas";
		person.info();
		
		Order order = new Order("202011020003", "01023450001", "서울시 강남구 역삼동 111-333",
				"20201102", "130258", "35000", "0003");
		order.orderInfo();
	}

}
