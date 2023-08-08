package ch16;
import java.util.Scanner;

public class SwtichCaseTest {

	public static void main(String[] args) {
		
		Scanner scanner = new Scanner(System.in);
		int month = scanner.nextInt();
		
//		int day;
//		switch(month){
//		
//		case 1: case 3: case 5: case 7: case 8: case 10: case 12:
//			day = 31;
//			break;
//		case 4: case 6: case 9: case 11:
//			day = 30;
//			break;
//		case 2: 
//			day = 28;
//			break;
//		default:
//			day = 0;
//			System.out.println("존재하지 않는 달 입니다.");
//		
//		}
			int day = switch (month) {
	    	case 1, 3, 5, 7, 8, 10,12 -> 
	    		31; // 값만 대입할떈 중괄호, yield 생략가능
	    	case 4,6,9,11 -> {
	    		// 다른 문장이 존재하거나, 코드가 존재하면
	    		// 중괄호, yield 작성필요
//	    		System.out.println("한 달은 30일입니다."); 
	    		yield 30;
	    	}
	    	case 2 ->{
//	    		System.out.println("한 달은 28일입니다.");
	    		yield 28;
	    	}
	    	default->{
//	    		System.out.println("존재하지 않는 달 입니다."); 
	    		yield 0;
	    	}
		};
		
		
		System.out.println(month + "월은 " + day + "일입니다.");
	}

}
