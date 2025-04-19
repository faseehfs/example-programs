#include <iostream>
#include <string>

class Solution
{
public:
    bool isPalindrome(int x)
    {
        std::string num = std::to_string(x);
        int left = 0;
        int right = num.length() - 1;

        while (left < right)
        {
            if (num[left] != num[right])
            {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};

int main()
{
    std::cout << "Enter an integer: ";
    int input;
    std::cin >> input;
    bool output = Solution().isPalindrome(input);

    if (output)
    {
        std::cout << "This integer is a palindrome.";
    }
    else
    {
        std::cout << "This integer is not a palindrome.";
    }
    std::cout << std::endl;

    return 0;
}
