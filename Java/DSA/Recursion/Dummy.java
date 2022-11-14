class dummy_subject{
	static int c = 0;
	void setmarks(){
		this.c = 1;
	}
	void set_marks(){
		this.c = 2;
	}
}
public class Dummy{ 
	public static void main(String args[]){
		dummy_subject ob = new dummy_subject();
		dummy_subject ob1 = new dummy_subject();
		ob.setmarks();
		ob1.set_marks();
		System.out.println(ob.c);
		System.out.println(ob1.c);
	}
}
