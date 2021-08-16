#include <iostream>
#include <vector>
#include <algorithm>    // std::sort

int LifeRafts(std::vector<int> &people, int limit)
{
    int lifeRafts = 0;
    std::sort (people.begin(), people.end()); //sort in ascending order
    int begin = 0;
    int end = people.size()-1;

    while (begin <= end)
    {
        if ( (people[begin] + people[end]) <= limit) //can we fit two people (can we squeeze in the smallest with the largest?)
        {
            begin++;
            end--;
        }
        else
        {
            end--;
        }
        lifeRafts++;
    }    
    
 
    return lifeRafts;
}

int main()
{

    std::vector<int> people{4, 2, 3, 3};
    int result =  LifeRafts(people,5);
    std::cout<<"this many rafts needed:"<<result;
}