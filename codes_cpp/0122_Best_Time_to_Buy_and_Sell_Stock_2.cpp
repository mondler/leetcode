// # https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
// # 122. Best Time to Buy and Sell Stock II
// # Easy
// #
// # 1678
// #
// # 1574
// #
// # Add to List
// #
// # Share
// # Say you have an array for which the ith element is the price of a given stock on day i.
// #
// # Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).
// #
// # Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
// #
// # Example 1:
// #
// # Input: [7,1,5,3,6,4]
// # Output: 7
// # Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
// #              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
// # Example 2:
// #
// # Input: [1,2,3,4,5]
// # Output: 4
// # Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
// #              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
// #              engaging multiple transactions at the same time. You must sell before buying again.
// # Example 3:
// #
// # Input: [7,6,4,3,1]
// # Output: 0
// # Explanation: In this case, no transaction is done, i.e. max profit = 0.

//

#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
int maxProfit(vector<int>& prices) {
        // int sum_of_elems;
        // sum_of_elems = sumVector(prices);
        int profits, previous, current;
        profits = 0;
        previous = prices[0];
        for (auto itr = prices.begin(); itr != prices.end(); ++itr) {
                current = *itr;
                if (current > previous) {
                        profits += current - previous;
                }
                previous = current;
        }
        // cout << profits << endl;
        return profits;
}
};


//

int main() {
        std::vector<int> prices = { 7,1,5,3,6,4 };

        // prices.push_back(10);
        // prices.push_back(20);
        // prices.push_back(30);

        Solution foo = Solution();
        int num = foo.maxProfit(prices);

        cout<<"out put " <<num;
        return 0;
}


// int main()
// {
//         // Create an empty vector
//         vector<int> vect;
//
//         vect.push_back(10);
//         vect.push_back(20);
//         vect.push_back(30);
//
//         for (int x : vect)
//                 cout << x << " ";
//
//         return 0;
// }





// class Solution {
// public:
// int lengthOfLongestSubstring(std::string s) {
//         return 0;
// }
// };
//
// int main() {
//
//         Solution foo = Solution();
//         int num = foo.lengthOfLongestSubstring("abcdcdefghcde");
//         // int num1 = foo.lengthOfLongestSubstring("");
//         // int num2 = foo.lengthOfLongestSubstring("aaaaaa");
//
//         cout << "out put " << num;
//         return 0;
// }
