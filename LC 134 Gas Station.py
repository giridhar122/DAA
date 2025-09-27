class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        st = 0
        bal = 0
        for i in range(len(gas)):
            bal += gas[i] - cost[i]
            if bal < 0:
                st = i + 1
                bal = 0
        return st