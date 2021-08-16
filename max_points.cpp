/*
You are given a bag of coins, an initial energy of E, and want to maximize your number of points 
(which starts at zero). To gain a single point you can exchange coins[i] amount of energy 
(i.e. if I have 100 energy and a coin that has a value 50 I can exchange 50 energy to gain a point). 
If you do not have enough energy you can give away a point in exchange for an increase in energy by coins[i] 
amount (i.e. you give away a point and your energy is increased by the value of that coin: energy += coins[i]).
 Return the maximum number of points you can gain.
Note: Each coin may only be used once.
*/
#include <iostream>
#include <vector>
#include <algorithm>    // std::sort

int MaxPoints(std::vector<int>& coins, int energy)
{
    //first sort bag of coins
    std::sort (coins.begin(), coins.end()); 
    int points = 0;
    int maxPoints = 0;
    

    while (!coins.empty())
    {
        // try to get a point
        if (coins.front() <= energy)
        {
            energy -= coins.front();
            points++;
            coins.erase(coins.begin()); //this is linear :(
        }
        //we don't have enough energy to get the next point. We need to trade
        else
        {
            //if we have nothing left to trade, we are done
            if (points == 0 ) break;
            points--;
            energy += coins.back();
            coins.pop_back();
        }

        //keep track of max because we might trade points later
        if (points > maxPoints) maxPoints = points;
        
    }
    return maxPoints;
}

int main()
{
    std::vector<int> coins{100,200,300,400};    
    std::cout<<MaxPoints(coins, 200);

}