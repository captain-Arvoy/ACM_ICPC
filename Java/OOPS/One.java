//only 
class Hello{
    public    char p_b_l_i_c ='P';
              char  n_o_t_h='N';
    private   char p_r_v_t_e ='R';
    protected char p_r_o_t_c ='T';

    void display(){
        System.out.println("The world we used to know.");
    }
}
class One{
    public static void main(String args[]){
        Hello aditya = new Hello();
        aditya.display();
        System.out.println(aditya.p_b_l_i_c);
        System.out.println(aditya.n_o_t_h);
        // System.out.println(aditya.p_r_v_t_e);
        System.out.println(aditya.p_r_o_t_c);
        aditya.p_b_l_i_c = 'X';//p_b_l_i_c is an instance variable
        aditya.p_r_o_t_c = 'X';//p_r_o_t_c is an instance variable
        System.out.println("Public = "+aditya.p_b_l_i_c);
        System.out.println("Protected = "+aditya.p_r_o_t_c);
    }
}//AIM ACM_ICPC FOR NITAI HARE KRSNA!!!!!!!!!!!!!!!!!!!!!!!