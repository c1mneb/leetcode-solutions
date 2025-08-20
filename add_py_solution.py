#!/usr/bin/env python3
import sys
import os
from datetime import datetime

def create_solution(problem_number, problem_title, difficulty):
    problem_slug = problem_title.lower().replace(' ', '-')
    filename_py = f"{problem_number}-{problem_slug}.py"
    folder = f"problems/{difficulty}/{problem_number}-{problem_slug}"
    os.makedirs(folder, exist_ok=True)
    
    filepath_py = os.path.join(folder, filename_py)
    
    if os.path.exists(filepath_py):
        print("Файл уже существует")
        return
    
    template_py = f'''
"""
LeetCode {problem_number}. {problem_title}
Difficulty: {difficulty}
URL: https://leetcode.com/problems/{problem_slug}

Решение добавлено: {datetime.now().strftime("%Y-%m-%d")}
"""

class Solution:
    def solve(self):
        """
        Time Complexity: O()
        Space Complexity: O()
        """
        pass

# Test cases
if __name__ == "__main__":
    sol = Solution()
    print("Python template created")
'''
    
    with open(filepath_py, 'w') as f:
        f.write(template_py)
    
    print(f"Создан файл: {filepath_py}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Использование: python add_solution.py <номер> \"<название>\" <сложность>")
        print('Пример: python add_py_solution.py 1 "Two Sum" easy')
        sys.exit(1)
    
    create_solution(sys.argv[1], sys.argv[2], sys.argv[3])