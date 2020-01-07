import sys
import pytest

def main():
    print("Advanced Algorithms")
    if sys.argv[1] == 'runtests':
        pytest.main(['-v', '-x', 'AdvancedAlgorithms/tests'])

if __name__ == "__main__":
    main()