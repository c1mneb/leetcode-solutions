import sys
import os
from datetime import datetime

def create_solution(problem_number, problem_title, difficulty):
    problem_slug = problem_title.lower().replace(' ', '-')
    filename_cpp = f"{problem_number}-{problem_slug}.cpp"
    folder = f"problems/{difficulty}/{problem_number}-{problem_slug}"
    os.makedirs(folder, exist_ok=True)

    filepath_cpp = os.path.join(folder, filename_cpp)
    
    if os.path.exists(filepath_cpp):
        print("Файл уже существует")
        return
    
    template_cpp = f'''
/*
LeetCode {problem_number}. {problem_title}
Difficulty: {difficulty}
URL: https://leetcode.com/problems/{problem_slug}

Решение добавлено: {datetime.now().strftime("%Y-%m-%d")}
*/

#include <iostream>
#include <vector>
using namespace std;

class Solution {{
public:
    void solve() {{
        // Time Complexity: O()
        // Space Complexity: O()
    }}
}};

int main() {{
    Solution sol;
    cout << "C++ template created" << endl;
    return 0;
}}
'''
    
    with open(filepath_cpp, 'w') as f:
        f.write(template_cpp)
    
    print(f"Создан файл: {filepath_cpp}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: python add_solution.py <номер> \"<название>\" <сложность>")
        print('Пример: python add_cpp_solution.py 1 "Two Sum" easy')
        sys.exit(1)
    
    create_solution(sys.argv[1], sys.argv[2], sys.argv[3])