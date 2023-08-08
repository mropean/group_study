package ch10;

public class TypeConversionTest {
	public static void main(String[] args) {

		double dNum = 1.2;
		float fNum = 0.9F;
		
		int iNum1 = (int)dNum + (int)fNum;
		int iNum2 = (int)(dNum + fNum);
		
		System.out.println(iNum1);
		System.out.println(iNum2);
		
		int iNum3 = 255;
		byte bNum3 = (byte)iNum3;
		System.out.println(bNum3);
		
		double dNum4 = 3.14;
		int iNum4 = (int)dNum4;
		System.out.println(iNum4);
	}
}
