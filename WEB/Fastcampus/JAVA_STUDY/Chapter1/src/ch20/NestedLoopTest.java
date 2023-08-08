package ch20;

public class NestedLoopTest {

	public static void main(String[] args) {
		
		System.out.println("~for LOOP~");
		int dan = 2;
		int count = 1;
		
		for(; dan <= 9; dan++) {
			for(count = 1; count <= 9; count++) {
				System.out.println(dan + "X" + count + "=" + dan * count);
			}
			System.out.println();
		}
		
		System.out.println("~while LOOP~");
		dan = 2;
		
		while(dan <= 9) {
			count = 1;
			while(count <= 9) {
				System.out.println(dan + "X" + count + "=" + dan * count);
				count++;
			}
			System.out.println();
			dan++;
		}
	}

}
