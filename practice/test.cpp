#include <iostream>
using namespace std;

class Circle
{
    int radius;
    public:

        Circle(int _radius): radius(_radius)
        {
            cout<<"constructor"<<endl;
        }
        Circle()
        {

        }

        void setRadius(int _radius)
        {
            radius = _radius;
        }

        double getArea()
        {
            return 3.14*radius*radius;
        }
};

int main()
{
    Circle c; //need defualt constructor to do this
    c.setRadius(5);
    cout<<c.getArea()<<endl;
    Circle c2(2);
    cout<<c2.getArea()<<endl;

}