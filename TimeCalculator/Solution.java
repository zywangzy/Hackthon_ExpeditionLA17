import java.io.FileNotFoundException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.Scanner;

public class Solution {

	public static void main(String[] args) throws FileNotFoundException, ParseException {
		 
		
		  

		  
		  
		 int identifier = 1001;
			  
	      SimpleDateFormat ft = new SimpleDateFormat ("yyyy-MM-dd hh:mm:ss");

		
		java.io.File file = new java.io.File("/Users/Chenggu/Desktop/routeTest.txt");
		Scanner input = new Scanner(file);
		
		
		int outfileNum = 1;
		
		
		while(input.hasNextLine()){
			String filenum = String.valueOf(outfileNum);
			String fileName = "/Users/Chenggu/Desktop/animation_final"+filenum+".txt";
			java.io.File outFile = new java.io.File(fileName);
			java.io.PrintWriter output = new java.io.PrintWriter(outFile);
			
			String buffer = input.nextLine();
			String[] colon = buffer.split(":");
			int production = Integer.parseInt(colon[0].trim());
			String process = colon[1].replaceAll("\\[", "");
			String process2 = process.replaceAll("\\]", "");
			String[] comma = process2.split(",");
			
			Calendar date = Calendar.getInstance();
			long t= date.getTimeInMillis();
			
			int count = comma.length;
			for(int i=0;i<count-1;i+=2){
				String a = comma[i].trim();
				String b = comma[i+1].trim();
				t += 8000;
				Date afterAdding8Seconds=new Date(t);
			    output.println(a+","+b+","+ft.format(afterAdding8Seconds)+","+production+","+identifier);
			}
			identifier += 1;
			outfileNum += 1;
			
			output.close();
			
			
			
		}
		

		input.close();
		System.out.println("success!");
		
		
	}

}
