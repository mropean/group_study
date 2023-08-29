package ch15;

public class TakeTest {

	public static void main(String[] args) {
		Person personE = new Person("Edward", 20000);
		Taxi taxi = new Taxi("잘나간다 운수");
		
		personE.takeTaxi(taxi);
		
		personE.showPeronInfo();
		taxi.showTaxiInfo();
	}

}
