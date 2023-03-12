#include<iostream>
using namespace std;
void printdetails(int id,string name="NA", string adress="NA"){
    cout<<"Id is "<< id<<endl;
    cout<<"Name is "<<name<<endl;
    cout<<"Adress is "<<adress<<endl;

}
int main(){
printdetails(101,"sandeep","noida");
cout<<"\n";
printdetails(301);
cout<<"\n";
printdetails(201,"nikhil");
return 0;
}