#include <iostream>

int main(){

    //integer (Whole number)
    int age =21;
    int year = 2023;
    int days = 7.5;

    std::cout << age <<std::endl;

    //double (number including decimal)
    double price = 10.99;
    double gpa = 2.5;
    double temperature = 25.1;
    std::cout << price <<std::endl;

    //single character
    char grade = 'A';
    char initial = 'B';
    char currency = '$';

    std::cout << initial <<std::endl;
    std::cout << currency <<std::endl;

    //boolean (true or false)
    bool student = true;
    bool forSale = false;
    bool power = true;

    //string (object representing sequence of text)
    std::string name = "Himanshu";
    std::string day = "Monday";
    std::string food = "pizza";
    std::string address = "Darekwar wadi";

    std::cout << "Hello " << name <<'\n';
    std::cout << "You are " << age << " years old" <<'\n';
    std::cout << food <<'\n';
    std::cout << address <<'\n';
    return 0;
}