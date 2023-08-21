package ch08;

public class Order {
	public String orderNumber;
	public String orderPhoneNumber;
	public String orderAddress;
	public String orderDate;
	public String orderTime;
	public String orderPrice;
	public String orderMenu;
	
	public Order(String orderNumber, String orderPhoneNumber, String orderAddress,
			String orderDate, String orderTime, String orderPrice, String orderMenu) {
		this.orderNumber = orderNumber;
		this.orderPhoneNumber = orderPhoneNumber;
		this.orderAddress = orderAddress;
		this.orderDate = orderDate;
		this.orderTime = orderTime;
		this.orderPrice = orderPrice;
		this.orderMenu = orderMenu;
	}
	
	public void orderInfo() {
		System.out.println("주문 접수 번호 : " + orderNumber);
		System.out.println("주문 핸드폰 번호 : " + orderPhoneNumber);
		System.out.println("주문 집 주소 : " + orderAddress);
		System.out.println("주문 날짜 : " + orderDate);
		System.out.println("주문 시간 : " + orderTime);
		System.out.println("주문 가격 : " + orderPrice);
		System.out.println("주문 메뉴 : " + orderMenu);
	}
}
