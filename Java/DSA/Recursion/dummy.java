class dummy_subject{
	static int c = 0;
	void setmarks(){
		this.c = 1;
	}
	void set_marks(){
		this.c = 2;
	}
public class dummy{
	public static void main(String args[]){
		dummy_subject ob = new dummy_subject();
		dummy_subject ob1 = new dummy_subject();
		System.out.println(ob.setmarks());
		System.out.println(ob1.set_marks());
	}
}
