class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # https://baihuqian.github.io/2018-06-23-gas-station/
        # if there is more gas in total than cost, then a solution must exist
        ''' We only need to iterate through the lists once because there is only one solution. If we reach a gas station that has has more gas than cost and we hav enot restarted, then that gas station must be part of the current string of stations. 
        
        If a route goes unbroken to the end of the list, that means it must be the solution, because there is only one solution. Ther emust be at least one route that goes to the end of the list unbroken if a solution exists becuase by iterating through all the stations we are testing each possible starting point.
        '''
        total = 0 
        route = 0 
        starting_station = 0
        for i in range(len(gas)):
            station_value = gas[i]-cost[i]
            total += station_value
            route += station_value
            if route < 0 :
                route = 0
                starting_station = i+1
            
        if total < 0:
            return -1
        return starting_station
            
        