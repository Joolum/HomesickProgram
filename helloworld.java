class helloworld{
    Integer number = -1;
    public static void main(String[] args) {
        System.out.println("Hello,World!");
        System.out.println(" TestTestTest");
        helloworld h1 = new helloworld();
        h1.testNumber();
    }

    public void testNumber(){
        for(int i=0;i<10;i++){
            number++;
        }
        System.out.println(number);
    }
    
}